contacts = []

def add_contact(name, phone, email, address):
    new_contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(new_contact)
    print("Contact added successfully!")

def view_contacts():
    print("\nContact List:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}")

def search_contact(search_term):
    search_results = []
    for contact in contacts:
        if (search_term.lower() in contact['name'].lower()) or (search_term in contact['phone']):
            search_results.append(contact)
    return search_results

def update_contact(index, name, phone, email, address):
    if 0 < index <= len(contacts):
        contacts[index - 1] = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }
        print("Contact updated successfully!")

def delete_contact(index):
    if 0 < index <= len(contacts):
        del contacts[index - 1]
        print("Contact deleted successfully!")

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        add_contact(name, phone, email, address)

    elif choice == '2':
        view_contacts()

    elif choice == '3':
        search_term = input("Enter name or phone number to search: ")
        results = search_contact(search_term)
        if results:
            print("\nSearch Results:")
            for idx, contact in enumerate(results, start=1):
                print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}")
        else:
            print("No matching contacts found.")

    elif choice == '4':
        index = int(input("Enter the index of contact to update: "))
        name = input("Enter updated name: ")
        phone = input("Enter updated phone number: ")
        email = input("Enter updated email: ")
        address = input("Enter updated address: ")
        update_contact(index, name, phone, email, address)

    elif choice == '5':
        index = int(input("Enter the index of contact to delete: "))
        delete_contact(index)

    elif choice == '6':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
