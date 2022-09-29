def main():


    CONTACTS = {}


    def input_error(handler):
        def wrapper():
            try:
                res = handler()
            except (ValueError, IndexError, UnboundLocalError):
                print("Error. Give me correct name and phone, please")
            except KeyError:
                print("Error. Enter user name, please")
        return wrapper


    def hello_func():
        print("How can I help you?")


    def quit_func():
        print("Good bye!")
        quit()


    @input_error
    def change_contact():
        name = var.split()[1]
        if (var.split()[2]).isdigit():
            phone = var.split()[2]
        CONTACTS[name] = phone
        print("Contact was changed")


    def show_contacts():
        for key, value in CONTACTS.items():
            print(f"{key}: {value}")


    @input_error
    def add_contact():
        if (var.split()[1]).isalpha():
            name = var.split()[1]
        if (var.split()[2]).isdigit():
            phone = var.split()[2]
        CONTACTS[name] = phone
        print(f"New contact was added")


    @input_error
    def find_contact():
        name = var.split()[1]
        print(f"{name}: {CONTACTS[name]}")


    COMMANDS = {
        "hello": hello_func,
        "show all": show_contacts,
        "exit": quit_func,
        "close": quit_func,
        "good bye": quit_func,
    }


    while True:
        var = (input("Enter command: ")).lower()
        if var.startswith('add'):
            add_contact()
        elif var.startswith('change'):
            change_contact()
        elif var.startswith('phone'):
            find_contact()
        elif var not in COMMANDS:
            print("Wrong command!")
            continue
        else:
            COMMANDS[var]()


if __name__ == "__main__":
    main()