import docker
import click
from subprocess import call
from pathlib import Path


def get_docker_images(ctx, args, incomplete):
    client = docker.from_env()
    tags = [tag for tags in [x.tags for x in client.images.list()] for tag in tags]
    if len(incomplete) > 0:
        return [t for t in tags if incomplete in t]
    else:
        return tags


@click.command()
@click.argument("imagename", type=click.STRING, autocompletion=get_docker_images)
def main(imagename):
    cwd = Path.cwd()
    workspace = cwd
    tree = [cwd]
    tree.extend(cwd.parents)
    for d in tree:
        if all(x in [f.name for f in d.iterdir()] for x in [".git", "docker"]):
            workspace = d
            break
    print(f"Mounting workspace: {workspace}")
    call(
        f"docker run --rm -it -v '{workspace}':'{workspace}' -w '{cwd}' {imagename}",
        shell=True,
    )


if __name__ == "__main__":
    main()
