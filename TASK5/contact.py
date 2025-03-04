class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    # Add a new contact
    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        address = input("Enter address: ")
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print(f"Contact {name} added successfully!")

    # View all contacts
    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for contact in self.contacts:
                print(contact)

    # Search for a contact by name or phone
    def search_contact(self):
        search_term = input("Enter the name or phone number to search: ")
        found_contacts = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        
        if found_contacts:
            for contact in found_contacts:
                print(contact)
        else:
            print("No contact found with that name or phone number.")

    # Update a contact's details
    def update_contact(self):
        search_term = input("Enter the name or phone number of the contact to update: ")
        found_contacts = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        
        if found_contacts:
            contact = found_contacts[0]  # Assuming first match for simplicity
            print(f"Updating details for {contact.name}:")
            contact.name = input(f"Enter new name (current: {contact.name}): ") or contact.name
            contact.phone = input(f"Enter new phone number (current: {contact.phone}): ") or contact.phone
            contact.email = input(f"Enter new email (current: {contact.email}): ") or contact.email
            contact.address = input(f"Enter new address (current: {contact.address}): ") or contact.address
            print(f"Contact {contact.name} updated successfully!")
        else:
            print("No contact found with that name or phone number.")

    # Delete a contact
    def delete_contact(self):
        search_term = input("Enter the name or phone number of the contact to delete: ")
        found_contacts = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        
        if found_contacts:
            contact = found_contacts[0]  # Assuming first match for simplicity
            self.contacts.remove(contact)
            print(f"Contact {contact.name} deleted successfully!")
        else:
            print("No contact found with that name or phone number.")

# Main function to interact with the user
def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            contact_book.add_contact()
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            contact_book.search_contact()
        elif choice == '4':
            contact_book.update_contact()
        elif choice == '5':
            contact_book.delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
