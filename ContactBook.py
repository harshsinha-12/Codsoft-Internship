
# Contact Book

## Description:
# This is a simple contact book application that allows the user to add, 
# edit and delete contacts.

# Class for contact

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address


class ContactManager:
    def __init__(self):
        self.contacts = []

# Function to add a contact

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added.")

# Function to display contacts

    def view_contacts(self):
        print("Contact List:")
        for idx, contact in enumerate(self.contacts, start=1):
            print(f"{idx}. {contact.name} - {contact.phone_number}")

# Function to search contact

    def search_contact(self, search_query):
        results = []
        for contact in self.contacts:
            if (
                search_query.lower() in contact.name.lower() or
                search_query in contact.phone_number
            ):
                results.append(contact)
        return results

# Function to update contact

    def update_contact(self, contact, new_phone_number, new_email, new_address):
        contact.phone_number = new_phone_number
        contact.email = new_email
        contact.address = new_address
        print("Contact updated.")

# Function to delete contact

    def delete_contact(self, contact):
        self.contacts.remove(contact)
        print("Contact deleted.")

# Main structure

def main():
    contact_manager = ContactManager()

    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter choice (1/2/3/4/5/6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone_number, email, address)
            contact_manager.add_contact(contact)
        elif choice == '2':
            contact_manager.view_contacts()
        elif choice == '3':
            search_query = input("Enter search query (name or phone number): ")
            results = contact_manager.search_contact(search_query)
            if results:
                print("Search results:")
                for idx, contact in enumerate(results, start=1):
                    print(f"{idx}. {contact.name} - {contact.phone_number}")
            else:
                print("No matching contacts found.")
        elif choice == '4':
            contact_manager.view_contacts()
            try:
                contact_idx = int(input("Enter index of the contact to update: ")) - 1
                if 0 <= contact_idx < len(contact_manager.contacts):
                    contact = contact_manager.contacts[contact_idx]
                    new_phone_number = input("Enter new phone number: ")
                    new_email = input("Enter new email: ")
                    new_address = input("Enter new address: ")
                    contact_manager.update_contact(contact, new_phone_number, new_email, new_address)
                else:
                    print("Invalid contact index.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '5':
            contact_manager.view_contacts()
            try:
                contact_idx = int(input("Enter index of the contact to delete: ")) - 1
                if 0 <= contact_idx < len(contact_manager.contacts):
                    contact = contact_manager.contacts[contact_idx]
                    contact_manager.delete_contact(contact)
                else:
                    print("Invalid contact index.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
