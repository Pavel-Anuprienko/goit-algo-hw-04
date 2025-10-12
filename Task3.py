
import sys
from pathlib import Path
from colorama import init, Fore, Style



init(autoreset=True)

def print_dir_structure(directory: Path, indent: str = ""):
    """Recursively displays the directory structure."""
    try:
        for item in sorted(directory.iterdir()):
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}{item.name}/")
                print_dir_structure(item, indent + "    ")
            else:
                print(f"{indent}{Fore.GREEN}{item.name}")
    except PermissionError:
        print(f"{indent}{Fore.RED}[ACCESS DENIED] {directory}")

def main():
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Usage: python Task3.py <directory_path>")
        sys.exit(1)

    path = Path(sys.argv[1])

    if not path.exists():
        print(f"{Fore.RED}Error: Path '{path}' does not exist.")
        sys.exit(1)
    if not path.is_dir():
        print(f"{Fore.RED}Error: '{path}' is not a directory.")
        sys.exit(1)

    print(f"{Fore.CYAN}Directory structure: {path}\n{Style.RESET_ALL}")
    print_dir_structure(path)


if __name__ == "__main__":
    main()
