# SCheck

SizeCheck (or SCheck) is a simple python-based program that calculates the size of folders and files in a specified directory.

## Usage

```
$ scheck [folder] --exclude <none | files | folders> --size-type [b | kb | kib | mb | mib | gb | gib]
```

[folder], `--exclude` and `--size-type` are optional.

Their default values are:

- [folder] = The current working directory
- --exclude none
- --size-type b

# Installation

## Windows

On Windows, all you have to do, is double click the installer, and restart your PC.
All the installer does is install the program to C:\Program Files, and then adds it to PATH (which requires a restart).

## Linux

On Linux (specifically Debian-similar distros), all you have to do is run this command:
```sh
curl -sSfL https://raw.githubusercontent.com/gitteh0754/scheck/install.sh | sudo bash
```

Don't be alarmed by the sudo, the script just installs the binary to /usr/bin/ and /bin/.
