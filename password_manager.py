import argparse
import os
from rich import print

parser = argparse.ArgumentParser(
    prog="pm",
    description="PM CLI by Alsaleh",
)

parser.add_argument(
    "--version",
    action="version",
    version="v0.0.1",
)

parser.add_argument(
    "--vault-name",
    required=True,
    help="Name of the vault",
)

parser.add_argument(
    "--master-password",
    required=True,
    help="Password of the vault",
)


# subparser of commands
subparser = parser.add_subparsers(
    title="command",
    required=True,
    help="Command to be executed",
    dest="selected_command",
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
    help="Account password for the password",
)

# `get` command
get_command_parser = subparser.add_parser(
    "get",
    help="Get an account from the vault",
)

get_command_parser.add_argument(
    "account_name",
    help="Account name",
)

# `list` command
list_command_parser = subparser.add_parser(
    "list",
    help="List all account in the vault",
)

list_command_parser.add_argument(
    "--show-password",
    help="Show password with the list",
    action="store_true",
)

parser.parse_args()
