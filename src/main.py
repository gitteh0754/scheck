"""
   Copyright [2025] [Parteh]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License. 
"""


import os
from math import floor

import typer
from rich import print
from typing_extensions import Annotated
from classes import Data

app = typer.Typer(context_settings={"help_option_names": ["-h", "--help"]})

def get_folder_size(folder: str):
    """
    Get size of folder in bytes. That's it.
    :param folder:
    :return:
    """
    size = 0
    for root, dirs, files in os.walk(folder):
        for i, v in enumerate(files):
            size += os.path.getsize(root + "/" + v)
    return size

@app.command(name="check", short_help="Checks the sizes of files and folders in a specified directory.")
def checkFolder(folder: Annotated[str, typer.Argument()] = ".", exclude = "none", size_type = "kb"):
    """Check the sizes of files and folders in a specified directory.
    If no directory is specified, it will use the current working directory. (e.g, "~/".)\n
    The "exclude" argument can only be "none", "files" or "folders".\n
    Also, the "size-type" argument can only be "b", "kb", "kib", "mb", "mib", "gb", or "gib"."""
    if folder == ".":
        folder = os.getcwd()

    if not folder.endswith("/") or not folder.endswith("\\"):
        folder += "/"

    if exclude.lower() not in ["none", "files", "folders"]:
        raise ValueError("The \"exclude\" argument can only be \"none\", \"files\", or \"folders\".")

    # Do the thing, Kronk!

    unfiltered = os.listdir(folder)
    filtered = {}
    if exclude not in ["files", "folders"]:
        for i, v in enumerate(unfiltered):
            if os.path.isfile(folder + v):
                filtered[v] = Data(folder + v, "File", 0)
            elif os.path.isdir(folder + v):
                filtered[v] = Data(folder + v, "Folder", 0)
            else:
                # Well what the FUCK could it be then?!
                continue
    else:
        if exclude == "files":
            for i, v in enumerate(unfiltered):
                if os.path.isfile(folder + v):
                    continue
                else:
                    filtered[v] = Data(folder + v, "Folder", 0)
        else:
            for i, v in enumerate(unfiltered):
                if os.path.isdir(folder + v):
                    continue
                else:
                    filtered[v] = Data(folder + v, "File", 0)
    for i, v in enumerate(filtered):
        if filtered[v].dataType == "Folder":
            filtered[v].size = get_folder_size(folder + v)
        else:
            filtered[v].size = os.path.getsize(folder + v)

    for i, v in enumerate(filtered):
        if size_type.lower() == "b":
            print("Name: [blue]" + filtered[v].name + "[/blue] | Size: [green]" + str(filtered[v].size) + "[/green][cyan] bytes[/cyan]")
        if size_type.lower() == "kb":
            print("Name: [blue]" + filtered[v].name + "[/blue] | Size: [green]" + str(round((filtered[v].size / 1000) * 100) / 100) + "[/green][cyan] kilobytes[/cyan]")
        if size_type.lower() == "kib":
            print("Name: [blue]" + filtered[v].name + "[/blue] | Size: [green]" + str(round((filtered[v].size / 1024) * 100) / 100) + "[/green][cyan] kibibytes[/cyan]")
        if size_type.lower() == "mb":
            print("Name: [blue]" + filtered[v].name + "[/blue] | Size: [green]" + str(round((filtered[v].size / 1e+06) * 1000) / 1000) + "[/green][cyan] megabytes[/cyan]")
        if size_type.lower() == "mib":
            print("Name: [blue]" + filtered[v].name + "[/blue] | Size: [green]" + str(round((filtered[v].size / 1048576) * 1000) / 1000) + "[/green][cyan] mebibytes[/cyan]")
        if size_type.lower() == "gb":
            print("Name: [blue]" + filtered[v].name + "[/blue] | Size: [green]" + str(round((filtered[v].size / 1e+09) * 10000) / 10000) + " [/green][cyan]gigabytes[/cyan]")
        if size_type.lower() == "gib":
            print("Name: [blue]" + filtered[v].name + "[/blue] | Size: [green]" + str(round((filtered[v].size / 1073741824) * 10000) / 10000) + "[/green][cyan] gibibytes[/cyan]")

    ''''''


@app.command()
def version():
    print("[yellow]scheck by Parteh[/yellow] [blue]--[/blue][bright_green] v1.0.0[/bright_green]")
    print("This software [bright_red]may have bugs![/bright_red] If you find any, report them to me on [cyan][link=https://www.github.com/gitteh0754/scheck/issues]GitHub[/link][/cyan]!")

if __name__ == "__main__":
    app()
