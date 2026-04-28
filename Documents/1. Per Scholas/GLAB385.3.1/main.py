def add_contact():
    name=input("Enter contact name: ")
    phone=input("Enter contact phone number: ")
    with open("contacts.txt", "a") as file:
        file.write(f"{name}:{phone}\n") 

    print(f"{name} has been added to contacts.")

def view_contacts():
      with open("contacts.txt", "r") as file:
           contacts = f.readlines()
           if not contacts:
               print("Your contact list is empty.")  
           else:
               print("Your contacts:")
               for contact in contacts:
                   print(contact,end="")

def main():
    while True:
        print("n\Concact List Application")
        print( "1. Add Contact")                   
        print( "2. View Contacts")                   
        print( "3. Exit")                   
        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")