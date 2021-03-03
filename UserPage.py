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
        self.lblUserTitle = Label(self.myFrame, text="THIS IS THE USER PAGE")
        self.lblUserTitle.pack()
        self.lblAddUser = Label(self.myFrame, text="SPECIFY A USERNAME TO ADD")
        self.lblAddUser.pack()
        self.entUsername = Entry(self.myFrame)
        self.entUsername.pack()
        self.btnAddUser = ttk.Button(self.myFrame, text="ADD USER", command=lambda:self.addUser(self.entUsername))
        self.btnAddUser.pack()
        self.cmbUserList = ttk.Combobox(self.myFrame, values=self.data.getUserList())
        self.cmbUserList.pack()
        self.btnDeleteUser = ttk.Button(self.myFrame, text="DELETE USER", command=lambda:self.deleteUser(self.cmbUserList))
        self.btnDeleteUser.pack()
        self.btnHomePage = ttk.Button(self.myFrame, text="Go back to home page", command=lambda:self.controller.raise_frame('HomePage'))
        self.btnHomePage.pack()

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