class contact_book:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self,name,phone_number,email,address):
        self.contacts.append(
                {
                    "name":name,
                    "phone_number":phone_number,
                    "email":email,
                    "address":address
                }
            )
        print("\nContact added successfully!")
    
    def view_contact(self):
        if len(self.contacts) == 0:
            print("No contacts available")
        else:
            for i in self.contacts:
                print("\nName: {}\nPhone Number: {}".format(i["name"],i["phone_number"]))
    
    def search_contacts(self,search_this):
        if len(self.contacts) == 0:
            print("No contacts available")
        else:
            for i in self.contacts:
                if search_this in i["name"] or search_this in str(i["phone_number"]):
                    print("\nName: {}\nPhone Number: {}".format(i["name"],i["phone_number"]))
    
    def update_contacts(self):
        if len(self.contacts) == 0:
            print("No contacts to update")
        else:
            for i,val in enumerate(self.contacts,1):
                print("{}.{}".format(i,val["name"]))
            select_contact = int(input("Select the contact: "))
            list_a = self.contacts[select_contact - 1]
            list_a["name"] = input("Enter Name: ")
            list_a["phone_number"] = int(input("Enter Ph.No: "))
            list_a["email"] = input("Enter email: ")
            list_a["address"] = input("Enter address: ")
            print("Updated successfully!")
            
            
    def delete_contact(self):
        if len(self.contacts) == 0:
            print("No contacts to delete")
        else:
            for i,val in enumerate(self.contacts,1):
                print("{}.{}".format(i,val["name"]))
            select_contact = int(input("Select the contact to delete: "))
            self.contacts.pop(select_contact - 1)
            print("contact removed successfully")
            
    # add contact, view contacts, Search Contact, Update Contact,Delete Contact
    
def main():
    phone_contacts = contact_book()
    while True:
        print("{}\nContacts Book Menu:\n{}".format("-"*18,"-"*18))
        print("\n1. Add Contact\n2. View Contact\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Quit")
        selected_option = input("Select an option: ")
        print("{}".format("-"*17))
        if selected_option == "1":
            name = input("Enter name: ")
            phone_number = int(input("Enter Ph.No: "))
            email = input("Enter email: ")
            address = input("Enter address: ")
            phone_contacts.add_contact(name,phone_number,email,address)
        
        elif selected_option == "2":
            phone_contacts.view_contact()
        
        elif selected_option == "3":
            search_this = input("Enter contact number ")
            phone_contacts.search_contacts(search_this)
            
        elif selected_option == "4":
            phone_contacts.update_contacts()
        
        elif selected_option == "5":
            phone_contacts.delete_contact()
        
        elif selected_option == "6":
            break

main()