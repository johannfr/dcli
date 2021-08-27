import click


def get_docker_images(ctx, args, incomplete):
    import docker

    client = docker.from_env()
    tags = [tag for tags in [x.tags for x in client.images.list()] for tag in tags]
    return [t for t in tags if incomplete in t or len(incomplete) == 0]


@click.command()
@click.argument("imagename", type=click.STRING, autocompletion=get_docker_images)
@click.argument("docker_args", nargs=-1, type=click.UNPROCESSED)
def main(imagename):
    from subprocess import call
    from pathlib import Path

    cwd = Path.cwd()
    workspace = cwd  # Default to cwd, then see if we find a better one.
    for d in [cwd] + [p for p in cwd.parents]:
        if all(x in [f.name.lower() for f in d.iterdir()] for x in [".git", "docker"]):
            workspace = d
            break
    click.secho(f"Mounting workspace: {workspace}", fg="yellow")
    call(
        f"docker run --rm -it {' '.join(docker_args)} -v '{workspace}':'{workspace}' -w '{cwd}' '{imagename}'",
        shell=True,
    )


if __name__ == "__main__":
    main()
