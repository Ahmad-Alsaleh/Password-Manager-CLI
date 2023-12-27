# Password Manager CLI

A simple command-line interface (CLI) password manager tool that was developed for a session presented during the Society of Cybersecurity (SOC) Winter Boot Camp for educational purposes. This project provides hands-on experience with Python, CLI app development, file I/O, and basic coding concepts. The recordings of the sessions can be found here: [Part 1](https://youtu.be/fbM739icFls?t=2457) and [Part 2](https://www.youtube.com/watch?v=JsLU1XCZt_o).

Want to get started? Jump to [## Getting Started]!

## Features

- **Secure Vaults:** Safely store your passwords in encrypted vaults (encryption was given as a self-task for students)
- **Simple Commands:** Easy-to-use commands for adding, listing, and retrieving passwords.
- **Colorful Terminal Output:** Utilizes the `rich` library for a visually appealing and user-friendly interface.

## Main Topics Covered

1. CLI App Development
2. Functions
3. File I/O
4. Code Organization
5. f-strings
6. Conditional Statements (if statements)

## Libraries Used

1. `argparse`: To make the CLI app.
2. `os`: To operate on files.
3. `rich` (optional): Create a colorful terminal output.

## Getting Started

### Prerequisites

Ensure your system has `Python` and `PIP` installed.

### Installation

1. Make a new directory (folder):

   ```bash
   mkdir password-manager
   ```
2. Navigate to the project directory:

   ```bash
   cd password-manager
   ```
3. Clone the repository:

   ```bash
   git clone https://github.com/Ahmad-Alsaleh/Password-Manager-CLI.git
   ```
4. (Optional, but recommended) Make a virtual environment:
    ```bash
    # Windows
    python -m venv venv # creating the virtual environment
    .\venv\Scripts\activate # activating the virtual environment
    ```
    
    ```bash
    # Mac/Linux
    python3 -m venv venv # creating the virtual environment
    source venv/bin/activate # activating the virtual environment
    ```
5. Install dependencies:

   ```bash
   # Windows
   pip install -r requirements.txt
   ```

   ```bash
   # Mac/Linux
   pip3 install -r requirements.txt
   ```

## Usage

**IMPORTANT NOTE: if you are using Mac/Linux, replace every `python` with `python3`.**

### Notation

* Square brackets `[VALUE]`: what in between is optional.
* Angular brackets `<VALUE>`: this is a placeholder. That is, a value must replace it.

### General use case

```bash
python password_manager.py --vault-name <name> --master-password <password> COMMAND [OPTIONS]
```

### CLI Commands

* `git` Retrieve the password for a specified account.

  ```bash
  python password_manager.py --vault-name <name> --master-password <password> get <account-name>
  ```
* `add` Add a new password to the vault.

  ```bash
  python password_manager.py --vault-name <name> --master-password <password> add <account-name> <password>
  ```
* `list` List all accounts in the vault (optionally displaying passwords).

  ```bash
  python password_manager.py --vault-name <name> --master-password <password> list [--show-passwords]
  ```

## Acknowledgments

This project was written during the SOC Winter Boot Camp for educational purposes.

Feel free to contribute and enhance this educational project!
