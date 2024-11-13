# Main function to diplay menu and handle user input
from brokencode import ContactBook
def main():
    contact_book = ContactBook() #Initialize ContactBook object 
 
    while True:
        # Display menu options
        print("\n--- Contact Book Menu ---")
        print("1. Add New Contact")
        print("2. Display all contacts")
        print("3. Search for a contact")
        print("4. Update an existing contact")
        print("5. Delete a contact")
        print("0. Exit")
 
        # Get user choice
        choice = input("Enter your choice: ")
 
        # Handle each menu option
        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")    
            email = input("Enter email: ")
            contact_book.add_contact(name, phone_number, email)
        elif choice == "2":
            contact_book.display_all_contacts()

        elif choice == "3":
            name = input("Enter the name to search: ")
            contact_book.search_contact(name)
        elif choice == "4":
            name = input("Enter the name to update: ")
            new_phone_number = input("Enter the new phone number: ")
            new_email = input("Enter the new email: ")
            contact_book.update_contact((name, new_phone_number, new_email))
        elif choice == "5":
            name = input("Enter the name to delete: ")
            contact_book.delete_contact(name)
        elif choice == "0":
            print("Exiting Contact Book. Goodbye!")
            break
    
        else:
            print("Invalid choice. Please enter a valid option.")

#  Start the program by calling the main function
if __name__ == "__main__":
    main()