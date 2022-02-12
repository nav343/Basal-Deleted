from time import sleep
from rich.console import Console
from colorama import Fore, Style
import argparse
import os

parser = argparse.ArgumentParser(
    description='A CLI program to create your Basal project.')
parser.add_argument('project_name', type=str,
                    help="Enter a name for your project.")
args = parser.parse_args()


try:
    console = Console()
    print(Fore.GREEN + "Creating project " + args.project_name)
    tasks = [f"Task {n}." for n in range(1, 11)]
    os.system("mkdir src")
    with open(f'src/{args.project_name}.basl', 'w') as f:
        f.write('''
    out("Hello World")
    ''')
    with open('init.json', 'w') as f:
        author = input("Author: ")
        description = input("Description: ")
        f.write('''{
    "project_name": "''' + args.project_name + '''",
    "author": "''' + author + '''",
    "description": "''' + description + '''",
    "version": "0.0.0"
}''')

    with console.status("[bold green]Creating project...") as status:
        while tasks:
            task = tasks.pop(0)
            sleep(1)
            console.log(f"{task} completed.....")

except Exception:
    print(Fore.RED + "An unknown error occurred.")
    print(Style.RESET_ALL)

