from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox

class UserPage:
    def __init__(self, root, controller, data):
        self.root = root
        self.controller = controller
        self.data = data
        self.userFile = self.data.userFile
        self.myFrame = Frame(self.root)
        self.lblUserTitle = ttk.Label(self.myFrame, text="Profile Management", font=("Helvetica", 28))
        self.lblUserTitle.place(x=143, y=20)
        self.lblAddUser = ttk.Label(self.myFrame, text="Add profile", font=("Helvetica", 10))
        self.lblAddUser.place(x=120, y=117)
        self.entUsername = Entry(self.myFrame, font=("Helvetica", 12))
        self.entUsername.place(x=117, y=137, width=165)
        self.btnAddUser = ttk.Button(self.myFrame, text="Add profile", command=lambda:self.addUser(self.entUsername))
        self.btnAddUser.place(x=117, y=177)

        self.lblDeleteUser = ttk.Label(self.myFrame, text="Delete profile", font=("Helvetica", 10))
        self.lblDeleteUser.place(x=335, y=117)
        self.cmbUserList = ttk.Combobox(self.myFrame, state="readonly", values=self.data.getUserList(), width=16, font=("Helvetica", 12))
        self.cmbUserList.place(x=332, y=137)
        self.btnDeleteUser = ttk.Button(self.myFrame, text="Delete profile", command=lambda:self.deleteUser(self.cmbUserList))
        self.btnDeleteUser.place(x=332, y=177)
        #self.btnHomePage = ttk.Button(self.myFrame, text="Home", command=lambda:self.controller.raise_frame('HomePage'))
        #self.btnHomePage.place(x=0, y=0)

    def addUser(self, user):
        trimmed = user.get().strip()
        if trimmed:
            if not self.data.hasUser(trimmed):
                updatedList = self.data.addUser(trimmed)
                print("updated list is {}".format(updatedList))
                self.cmbUserList['values'] = updatedList #updatedUserList#update list from addUser return
                #self.controller.pages[HomePage].updateUserList(updatedUserList)
                self.controller.updateHomePageUserList(updatedList)
                user.delete(0,END)
                messagebox.showinfo("Profile added","Profile: '" + trimmed + "' has been added successfully.")
            else:
                messagebox.showwarning("Profile not added","Profile: '" + trimmed + "' already exists. \nPlease choose another profile name.")
                print("User already exists")
        else:
            messagebox.showwarning("Profile error","Please enter a profile name.")
            print("Please provide a username to add. The Entry box should be cleared")
            user.delete(0,END)

    def deleteUser(self, user):
        if user.get():
            print("user provided")
            userToDelete = user.get()
            if self.data.hasUser(user.get()):
                updatedList = self.data.deleteUser(user.get())
                self.cmbUserList['values'] = updatedList
                #self.controller.pages[HomePage].updateUserList(updatedUserList)
                self.controller.updateHomePageUserList(updatedList)
                self.cmbUserList.set('')
                messagebox.showinfo("Profile deleted","Profile: '" + userToDelete + "' has been deleted successfully.")
            else:
                messagebox.showwarning("Profile not deleted","Profile: '" + userToDelete + "' cannot be deleted as it doesn't exist.")
                print("User does not exist")
        else:
            messagebox.showerror("Profile error", "Please select a profile name to delete.")
            print("No user provided")
    
    def clearForm(self):
        self.entUsername.delete(0,END)
        self.cmbUserList.set('')