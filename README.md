# SCheck

SizeCheck (or SCheck) is a simple python-based program that calculates the size of folders and files in a specified directory.

## Usage

```
$ scheck check [folder] --exclude <none | files | folders> --size-type [b | kb | kib | mb | mib | gb | gib]
```

[folder], `--exclude` and `--size-type` are optional.

Their default values are:

- [folder] = The current working directory
- --exclude none
- --size-type b

# Installation

Download the correct installer or binary package for your OS, and then follow the steps below.

## Windows

On Windows, all you have to do, is double click the installer, and restart your PC.
All the installer does is install the program to C:\Program Files, and then adds it to PATH (which requires a restart).

## Linux

You have to manually unzip the `scheck-linux.tar.gz` file from the releases page using `tar -xzf`, and add the directory in which the `_internal` and `scheck` files were extracted to the $PATH variable manually.
This is because my install script does not load in cURL, so there is no one-liner. Sorry! :/
