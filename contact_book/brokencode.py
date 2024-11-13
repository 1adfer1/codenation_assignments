# clas to represent an individual contact
class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

 # clas to manage a list of contacts
class ContactBook:
    def __init__(self):
        # Initialising with two defsult contacts
        self.contacts = [
            Contact("Alice", "1234567890", "alice@email.com"),
            Contact("Bob", "9876543210", "bob@email.com")
        ]
    # Method to add a new contact
    def add_contact(self, name, phone_number, email):
        self.contacts.append(Contact(name, phone_number, email))
        print(f"Contact '{name}' added successfully.")

     # Method to display all contacts
    def display_all_contacts(self):
        if self.contacts:
            print("All Contacts:")
            for contact in self.contacts:
                print(f"Name: {contact.name}\nPhone: {contact.phone_number}\nEmail: {contact.email}\n")
        else:
            print("No contacts found.")

    # Method to search from all contacts by name
    def search_contact(self, name):
        contact_present = False
        for contact in self.contacts:
            if contact.name == name:
                print(f"Name: {contact.name}\nPhone: {contact.phone_number}\nEmail: {contact.email}\n")
                contact_present = True
                break
            if not contact_present:
                print("Contact not found")
    
    # Method to update an existing contact
    def update_contact(self, name, new_phone_number, new_email):
        contact_present = False
        for contact in self.contacts:
            if contact.name == name:
                contact.phone_number = new_phone_number
                contact.email = new_email
                print(f"Name: {contact.name}\nPhone: {contact.phone_number}\nEmail: {contact.email}\n")
                contact_present = True
                break
            if not contact_present:
                print("Contact not found")
    
    # Method to delete an existing contact by name
    def delete_contact(self, name):
        contact_present = False
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact '{name}' deleted successfully.")
                contact_present = True
                break
            if not contact_present:
                print("Contact not found.")
 
