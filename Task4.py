

def parse_input(user_input):
    """Parsing user input into command and arguments."""
    parts = user_input.strip().split()
    if not parts:
        return "", []
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args


def add_contact(args, contacts):
    """Adds a new contact to the dictionary."""
    if len(args) != 2:
        return "Invalid input. Use: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return f"Contact '{name}' added."


def change_contact(args, contacts):
    """Changes the phone number for an existing contact."""
    if len(args) != 2:
        return "Invalid input. Use: change [name] [new_phone]"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Contact '{name}' updated."
    else:
        return f"Contact '{name}' not found."


def show_phone(args, contacts):
    """Shows the phone number by name."""
    if len(args) != 1:
        return "Invalid input. Use: phone [name]"
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return f"Contact '{name}' not found."


def show_all(contacts):
    """Shows all contacts."""
    if not contacts:
        return "No contacts saved."
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)


def main():
    """The main function of the program."""
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        elif command == "":
            continue

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
