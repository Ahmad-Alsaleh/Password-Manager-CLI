import argparse
from rich import print
import os

VERSION = "0.0.1"
VAULT_FOLDER = "vaults"

os.makedirs(VAULT_FOLDER, exist_ok=True)


def get_vault_path(vault_name):
    return os.path.join(VAULT_FOLDER, vault_name + ".vault")


def authenticate_vault(vault_name, master_password):
    file_path = get_vault_path(vault_name)
    if os.path.exists(file_path):
        if get_stored_master_password(vault_name) == master_password:
            print(f"[green]Vault `{vault_name}` unlocked successfully!")
        else:
            print("[red]Incorrect master password! Exiting...")
            exit()
    else:  # vault does not exist
        create_new_vault(vault_name, master_password)
        print(f"[yellow]Vault `{vault_name}` created successfully!")


def get_stored_master_password(vault_name):
    with open(get_vault_path(vault_name), "r") as file:
        first_line = file.readline().strip()
    return first_line


def create_new_vault(vault_name, master_password):
    file_path = get_vault_path(vault_name)
    with open(file_path, "w") as file:
        file.write(master_password + "\n")


def add_new_password_to_vault(vault_name, account_name, password):
    with open(get_vault_path(vault_name), "a") as file:
        file.write(f"{account_name}:{password}\n")


def list_all_passwords_in_vault(vault_name, show_passwords):
    with open(get_vault_path(vault_name), "r") as file:
        file.readline()  # skip first line (the master password)
        for line in file.readlines():
            account_name, password = line.strip().split(":")
            if show_passwords:
                print(f"[cyan]{account_name}[/cyan]: [blue]{password}[/blue]")
            else:
                print(f"[cyan]{account_name}[/cyan]")


def get_password_from_vault(vault_name, account_name):
    with open(get_vault_path(vault_name), "r") as file:
        file.readline() # skip first line (the master password)
        for line in file.readlines():
            line = line.strip()
            if account_name == line.split(":")[0]:
                return line.split(":")[1]
    return None


parser = argparse.ArgumentParser(
    prog="pm",
    description="Password Manager CLI application. By: Ahmad Alsaleh",
)

parser.add_argument(
    "--version",
    action="version",
    version=f"Password Manager CLI v{VERSION}",
)

parser.add_argument(
    "--vault-name",
    required=True,
    metavar="<name>",
    help="Name of vault",
)

parser.add_argument(
    "--master-password",
    required=True,
    metavar="<password>",
    help="Password to unlock the vault",
)

# subparser for commands
subparser = parser.add_subparsers(
    title="command",
    dest="selected_command",
    required=True,
    help="Command to execute",
)

# `add` command
add_command_parser = subparser.add_parser(
    "add",
    help="Add a new account to the vault",
)

add_command_parser.add_argument(
    "account_name",
    help="Account name for the password",
)

add_command_parser.add_argument(
    "account_password",
    help="Password for the account",
)

# `list` command
list_command_parser = subparser.add_parser(
    "list",
    help="List all accounts in the vault",
)

list_command_parser.add_argument(
    "--show-passwords",
    action="store_true",
    help="Show passwords in the list",
)

# `get` command
list_command_parser = subparser.add_parser(
    "get",
    help="Get a password for an account",
)

list_command_parser.add_argument(
    "account_name",
    help="Account name to show the password for",
)

args = parser.parse_args()

authenticate_vault(args.vault_name, args.master_password)

if args.selected_command == "add":
    print(f"[green]Adding new account `{args.account_name}`")
    add_new_password_to_vault(
        args.vault_name,
        args.account_name,
        args.account_password,
    )

elif args.selected_command == "list":
    print(f"[green]Listing all accounts in `{args.vault_name}`")
    list_all_passwords_in_vault(args.vault_name, args.show_passwords)

elif args.selected_command == "get":
    print(f"[green]Getting password for `{args.account_name}`")
    password = get_password_from_vault(args.vault_name, args.account_name)
    if password is not None:
        print(f"[blue]{password}[/blue]")
    else:
        print(f"[red]Account `{args.account_name}` not found!")
