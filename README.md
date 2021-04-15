# dcli

Runs an interactive Docker shell into the specified image.

It mounts the current "workspace", which is determined by locating the `.git` and `docker` folders, into the container and sets the container-shell CWD to the outside CWD.

## Installation

### pip
```
pip install --user git+https://github.com/johannfr/dcli
```

### pipx
```
pipx install git+https://github.com/johannfr/dcli
```

## Shell completion

### Zsh

Add `eval "$(_DCLI_COMPLETE=source_zsh dcli)"` to `~/.zshrc`

### Bash

Add `eval "$(_DCLI_COMPLETE=source_bash dcli)"` to `~/.bashrc`

### Fish

Add `eval (env _DCLI_COMPLETE=source_fish dcli)` to `~/.config/fish/completions/dcli.fish`

## Demo

[![asciicast](https://asciinema.org/a/2gJEIUZFeWsPRynm0nBB1yetq.svg)](https://asciinema.org/a/2gJEIUZFeWsPRynm0nBB1yetq)
