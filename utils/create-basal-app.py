from time import sleep
from rich.console import Console
from colorama import Fore, Style
import argparse

parser = argparse.ArgumentParser(description='A CLI program to create your Basal project.')
parser.add_argument('project_name', type=str, help="Enter a name for your project.")
args = parser.parse_args()

try:
    console = Console()
    print(Fore.GREEN + "Creating project " + args.project_name)
    tasks = [f"Task {n}." for n in range(1, 11)]

    with console.status("[bold green]Creating project...") as status:
        with open(f"{args.project_name}.bsl", 'w') as f:
            f.write('''out("Hello World")''')
        while tasks:
            task = tasks.pop(0)
            sleep(1)
            console.log(f"{task} completed.....")
except Exception:
    print(Fore.RED + "An unknown error occurred.")
    print(Style.RESET_ALL)
