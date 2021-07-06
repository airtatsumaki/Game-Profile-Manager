from tkinter import *
from tkinter import filedialog
from tkinter import ttk

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
        self.lblAddUser.place(x=95, y=117)
        self.entUsername = Entry(self.myFrame, font="Helvetica 12")
        self.entUsername.place(x=92, y=137, width=135)
        self.btnAddUser = ttk.Button(self.myFrame, text="Add profile", command=lambda:self.addUser(self.entUsername))
        self.btnAddUser.place(x=92, y=177)
        self.lblDeleteUser = ttk.Label(self.myFrame, text="Delete profile", font=("Helvetica", 10))
        self.lblDeleteUser.place(x=300, y=117)
        self.cmbUserList = ttk.Combobox(self.myFrame, state="readonly", values=self.data.getUserList(), width=16, font="Helvetica 12")
        self.cmbUserList.place(x=297, y=137)
        self.btnDeleteUser = ttk.Button(self.myFrame, text="Delete profile", command=lambda:self.deleteUser(self.cmbUserList))
        self.btnDeleteUser.place(x=297, y=177)
        self.btnHomePage = ttk.Button(self.myFrame, text="Home", command=lambda:self.controller.raise_frame('HomePage'))
        self.btnHomePage.place(x=0, y=0)

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
            else:
                print("User already exists")
        else:
            print("Please provide a username to add. The Entry box should be cleared")
            user.delete(0,END)

    def deleteUser(self, user):
        if user.get():
            print("user provided")
            if self.data.hasUser(user.get()):
                updatedList = self.data.deleteUser(user.get())
                self.cmbUserList['values'] = updatedList
                #self.controller.pages[HomePage].updateUserList(updatedUserList)
                self.controller.updateHomePageUserList(updatedList)
                self.cmbUserList.set('')
            else:
                print("User does not exist")
        else:
            print("No user provided")
    
    def clearForm(self):
        self.entUsername.delete(0,END)
        self.cmbUserList.set('')