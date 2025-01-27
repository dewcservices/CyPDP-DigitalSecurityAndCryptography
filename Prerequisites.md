# Prerequisites

This lab has been designed to be OS-agnostic. Instructions for different operating systems can be found below.

## OpenSSL
### Windows

1. Download Git for Windows - portable edition from the [Git webpage](https://git-scm.com/downloads/win).
2. Execute the file to extract the contents to the directory of your choosing.
3. Run the `git-bash.exe` program to bring up a bash-like interface.
4. Ensure `openssl`  works by executing the command `openssl -v`. For example, what I get is `OpenSSL 3.2.3 3 Sep 2024 (Library: OpenSSL 3.2.3 3 Sep 2024)`


### Ubuntu/Debian

1. In your favourite terminal, execute the command `sudo apt install openssl`.
2. Ensure `openssl`  works by executing the command `openssl version`. For example, what I get is `OpenSSL 3.0.15 3 Sep 2024 (Library: OpenSSL 3.0.15 3 Sep 2024)`

### CentOS/RHEL

1. In your favourite terminal, execute the command `sudo dnf install openssl`.
2. Ensure `openssl`  works by executing the command `openssl version`. For example, what I get is `OpenSSL 3.0.15 3 Sep 2024 (Library: OpenSSL 3.0.15 3 Sep 2024)`


### macOS

OpenSSL should be included by default. If that is not the case (older hardware, uninstalled on purpose, and so on), you can use the Homebrew package manager to install it:

1. Install `brew`: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
2. Install `openssl`: `brew install openssl`
3. Ensure `openssl` can be invoked as a command by adding it to the PATH environmental variable - the below assumes you are using zsh as your shell:
```
echo 'export PATH="/usr/local/opt/openssl/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```
4. Ensure `openssl`  works by executing the command `openssl version` (or `openssl -v` if the former does not work).

macOS uses LibreSSL under the hood, which may explain the inconsistent output when running the version command(s). [LibreSSL](https://www.libressl.org/) is a version of the TLS/crypto stack forked from OpenSSL in 2014, with goals of modernizing the codebase, improving security, and applying best practice development processes. It maintains the same API as OpenSSL, so for the purposes of this workshop, it will suffice.