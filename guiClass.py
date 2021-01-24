import os
import json
import pylnk3
import webbrowser
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

def main():
    root = Tk()
    root.title("Game Profile Manager")
    root.minsize(300,400)
    runapp = MyApp(root)
    root.mainloop()

class MyApp:
    def __init__(self, root):
        self.root = root
        self.frames = {}

        for x in (HomePage, UserPage, GamePage):
            page = x(self.root, self)
            self.frames[x] = page.myFrame
            page.myFrame.place(x=0, y=0, width=300, height=400)
        
        self.raise_frame(HomePage)

    def raise_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
    # def getDir(self):
    #     self.path = filedialog.askdirectory(initialdir = "/",title = "Select directory",mustexist=True)
    #     #print(self.path)
    #     if len(self.path) > 0:
    #         self.lblDir.config(text=self.path)

class HomePage:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.myFrame = Frame(self.root)
        self.lblHomeTitle = Label(self.myFrame, text="WELCOME TO THE HOME PAGE")
        self.lblHomeTitle.pack()
        self.btnUserPage = ttk.Button(self.myFrame, text="Go to user page", command=lambda:self.controller.raise_frame(UserPage))
        self.btnUserPage.pack()
        self.btnGamePage = ttk.Button(self.myFrame, text="Go to game page", command=lambda:self.controller.raise_frame(GamePage))
        self.btnGamePage.pack()
        self.btnRunGame = ttk.Button(self.myFrame, text="Run the game", command=lambda:self.runGame("me","red dead 2"))
        self.btnRunGame.pack()

    def runGame(self, currentUser, currentGame):
        #self.currentGame = currentGame
        print("run " + currentGame)

class UserPage:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.userFile = 'resources/profiles.json'
        self.myFrame = Frame(self.root)
        self.lblUserTitle = Label(self.myFrame, text="THIS IS THE USER PAGE")
        self.lblUserTitle.pack()
        self.lblAddUser = Label(self.myFrame, text="SPECIFY A USERNAME TO ADD")
        self.lblAddUser.pack()
        self.entUsername = Entry(self.myFrame)
        self.entUsername.pack()
        self.btnAddUser = ttk.Button(self.myFrame, text="ADD USER", command=lambda:self.addUser(self.entUsername))
        self.btnAddUser.pack()
        self.userList = []
        if self.readFile(self.userFile):
            self.userJSON = self.readFile(self.userFile)
        else:
            self.userJSON = {"profiles":[]}
        print(self.userJSON)
        for x in self.userJSON["profiles"]:
            self.userList.append(x["name"])
        self.cmbUserList = ttk.Combobox(self.myFrame, values=self.userList)
        self.cmbUserList.pack()
        self.btnDeleteUser = ttk.Button(self.myFrame, text="DELETE USER", command=lambda:self.deleteUser(self.cmbUserList))
        self.btnDeleteUser.pack()
        self.btnHomePage = ttk.Button(self.myFrame, text="Go back to home page", command=lambda:self.controller.raise_frame(HomePage))
        self.btnHomePage.pack()

    def readFile(self, path):
        try:
            with open(path) as json_file:
                myjson = json.load(json_file) # load json file if present
            return myjson
        except Exception:
            return False
    
    def writeObjToFile(self, path, jsonObj):
        try:
            with open(path, "w") as f:
                json.dump(jsonObj, f, indent=4) #write people list
        except Exception:
            return False

    def addUser(self, entBox):
        trimmed = entBox.get().strip()
        if trimmed:
            # found = False
            # for x in self.userJSON["profiles"]:
            #     if x["name"] == trimmed:
            #         found = True
            if {'name': trimmed} not in self.userJSON["profiles"]:
                self.userJSON["profiles"].append({'name': trimmed})
                print("user " + trimmed + " added to the file")
                self.updateUserList()
                self.cmbUserList['values'] = self.userList
                entBox.delete(0,END)
            else:
                print("User already exists")
        else:
            print("Please provide a username to add. The Entry box should be cleared")
            entBox.delete(0,END)

    def deleteUser(self, user):
        if user.get():
            print("user provided")
            if {'name': user.get()} in self.userJSON["profiles"]:
                self.userJSON["profiles"].remove({'name': user.get()})
                print("user " + user.get() + " removed from file")
                self.updateUserList()
                self.cmbUserList['values'] = self.userList
                self.cmbUserList.set('')
            else:
                print("User does not exist")
        else:
            print("No user provided")

    def updateUserList(self):
        self.userList = []
        for x in self.userJSON["profiles"]:
            self.userList.append(x["name"])
        self.writeObjToFile(self.userFile, self.userJSON)
        self.cmbUserList['values'] = self.userList

class GamePage:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.gameFile = 'resources/games.json'
        self.myFrame = Frame(self.root)
        self.lblGameTitle = Label(self.myFrame, text="WELCOME TO THE GAME PAGE")
        self.lblGameTitle.pack()
        self.lblGameName = Label(self.myFrame, text="enter game name")
        self.lblGameName.pack()
        self.entGamename = Entry(self.myFrame)
        self.entGamename.pack()
        self.lblGamePath = Label(self.myFrame, text="game path '.exe' or 'steam://rungameid/XXXXXX'")
        self.lblGamePath.pack()
        self.entGamePath = Entry(self.myFrame)
        self.entGamePath.pack()
        self.btnGameBrowse = ttk.Button(self.myFrame, text="Browse ...")#, command=lambda:self.deleteUser(self.cmbUserList))
        self.btnGameBrowse.pack()
        self.lblGameSave = Label(self.myFrame, text="game save location")
        self.lblGameSave.pack()
        self.entGameSave = Entry(self.myFrame)
        self.entGameSave.pack()
        self.btnGameSaveBrowse = ttk.Button(self.myFrame, text="Browse ...")#, command=lambda:self.deleteUser(self.cmbUserList))
        self.btnGameSaveBrowse.pack()
        self.gameList = []
        self.gameList = ["game1","game2"]
        self.btnAddGame = ttk.Button(self.myFrame, text="Add game")#, command=lambda:self.deleteUser(self.cmbUserList))
        self.btnAddGame.pack()
        self.lblDeleteGame = Label(self.myFrame, text="delete game")
        self.lblDeleteGame.pack()
        self.cmbGameList = ttk.Combobox(self.myFrame, values=self.gameList)
        self.cmbGameList.pack()
        self.btnDeleteGame = ttk.Button(self.myFrame, text="Delete game")#, command=lambda:self.deleteUser(self.cmbUserList))
        self.btnDeleteGame.pack()


        self.btnHomePage = ttk.Button(self.myFrame, text="Go back to home page", command=lambda:self.controller.raise_frame(HomePage))
        self.btnHomePage.pack()

main()

# p1 = Person("Naz",35)

# lblDir = Label(root, text="select a directory and this text will update")
# lblFile = Label(root, text="select a file and this text will update")
# lblDir.pack()

# def getDir():
#     path = filedialog.askdirectory(initialdir = "/",title = "Select directory",mustexist=True)
#     #print(path)
#     if len(path) > 0:
#         lblDir.config(text=path)

# def getFile():
#     filepath = filedialog.askopenfilename(parent=root, initialdir="/", filetypes=(("shortcuts", ".lnk .url"), ("all files", "*.*")))
#     if filepath.lower().endswith(('.url')):
#         #FIND THE TARGET OF THE LNK OR URL
#         url = ''
#         with open(filepath, "r") as infile:
#             for line in infile:
#                 if (line.startswith('URL')):
#                     url = line[4:]
#                     break
#         print(url)
#     elif filepath.lower().endswith(('.lnk')):
#         target = pylnk3.parse(filepath).path.replace('\\','/')
#         print(target)
#     global selectedFile
#     #print(filepath)
#     if len(filepath) > 0:
#         selectedFile = filepath
#         print(selectedFile)
#         lblFile.config(text=filepath)
        
# def openFile(filePath):
#     print("inside openFile function")
#     print(filePath)
#     if filePath:
#         #subprocess.Popen(filePath)
#         os.startfile(filePath)
#     else:
#         print("You need to select a file before running it")

# def runSteamGame():
#     #subprocess.Popen("C:/Program Files (x86)/Steam/Steam.exe -applaunch 750920")
#     webbrowser.open('steam://rungameid/861650')
    

# btnOpenDir = Button(root, text="Choose directory...", fg="black",command=getDir)
# btnOpenDir.pack()

# lblFile.pack()
# btnOpenFile = Button(root, text="Choose a file...", fg="black",command=getFile)
# btnOpenFile.pack()

# btnRunFile = Button(root, text="Run selected file above", fg="black",command=lambda: openFile(selectedFile))
# btnRunFile.pack()

# btnRunSteamGame = Button(root, text="or just run a steam game id here", fg="black",command=runSteamGame)
# btnRunSteamGame.pack()

# #root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("application files","*.exe"),("all files","*.*")))
# #root.directory = filedialog.askdirectory(initialdir = "/",title = "Select directory",mustexist=True)
# #print(root.filename)
# #print(root.directory)
# #print(".exe" in root.filename)
# #subprocess.Popen([str(root.filename)])
# root.mainloop()