import tkinter as tk
from tkinter import messagebox
class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.contacts = []
        self.name_label = tk.Label(root, text="Name:")
        self.name_entry = tk.Entry(root)
        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_entry = tk.Entry(root)
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.name_label.grid(row=0, column=0, sticky="E")
        self.name_entry.grid(row=0, column=1)
        self.phone_label.grid(row=1, column=0, sticky="E")
        self.phone_entry.grid(row=1, column=1)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)
        self.view_button.grid(row=3, column=0, columnspan=2, pady=5)
        self.search_button.grid(row=4, column=0, columnspan=2, pady=5)
        self.update_button.grid(row=5, column=0, columnspan=2, pady=5)
        self.delete_button.grid(row=6, column=0, columnspan=2, pady=5)
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name and phone:
            self.contacts.append({"Name": name, "Phone": phone})
            messagebox.showinfo("Success", "Contact added successfully.")
        else:
            messagebox.showerror("Error", "Please enter both name and phone number.")
    def view_contacts(self):
        if self.contacts:
            contact_list = "\n".join([f"{contact['Name']}: {contact['Phone']}" for contact in self.contacts])
            messagebox.showinfo("Contacts", contact_list)
        else:
            messagebox.showinfo("Contacts", "No contacts available.")
    def search_contact(self):
        name_to_search = self.name_entry.get()
        phone_to_search = self.phone_entry.get()

        if name_to_search or phone_to_search:
            found_contacts = [contact for contact in self.contacts if
                              (name_to_search.lower() in contact['Name'].lower() if name_to_search else True) and
                              (phone_to_search in contact['Phone'] if phone_to_search else True)]

            if found_contacts:
                contact_list = "\n".join([f"{contact['Name']}: {contact['Phone']}" for contact in found_contacts])
                messagebox.showinfo("Search Results", contact_list)
            else:
                messagebox.showinfo("Search Results", "No matching contacts found.")
        else:
            messagebox.showerror("Error", "Please enter either name or phone number to search.")
    def update_contact(self):        
        name_to_update = self.name_entry.get()
        phone_to_update = self.phone_entry.get()

        if name_to_update and phone_to_update:
            
            for contact in self.contacts:
                if contact['Name'].lower() == name_to_update.lower():
                   contact['Phone'] = phone_to_update
                   messagebox.showinfo("Update", f"Contact updated successfully: {contact['Name']}: {contact['Phone']}")
                break
            else:
                messagebox.showinfo("Update", f"No matching contact found for updating: {name_to_update}")
        else:
            messagebox.showerror("Error", "Please enter both name and phone number for updating.")
    def delete_contact(self):
        name_to_delete = self.name_entry.get()

        if name_to_delete:
            for contact in self.contacts:
               
                if contact['Name'].lower() == name_to_delete.lower():
                    self.contacts.remove(contact)
                messagebox.showinfo("Delete", f"Contact deleted successfully: {contact['Name']}: {contact['Phone']}")
                break
            else:
                messagebox.showinfo("Delete", f"No matching contact found for deletion: {name_to_delete}")
        else:
            messagebox.showerror("Error", "Please enter the name for deleting a contact.")
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
