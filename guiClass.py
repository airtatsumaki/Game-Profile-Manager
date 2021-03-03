import os
import json
import pylnk3
import webbrowser
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from Data import Data
from HomePage import HomePage
from UserPage import UserPage
from GamePage import GamePage

def main():
    root = Tk()
    root.title("Game Profile Manager")
    root.minsize(300,400)
    runapp = MyApp(root)
    root.mainloop()

class MyApp:
    def __init__(self, root):
        self.root = root
        self.pages = {}
        dataObj = Data()
        print("user list is: {}".format(dataObj.userList))
        print("game list is: {}".format(dataObj.gameList))

        for x in (HomePage, UserPage, GamePage):
            page = x(self.root, self, dataObj)
            self.pages[type(page).__name__] = page
            page.myFrame.place(x=0, y=0, width=300, height=400)

        self.raise_frame('HomePage')

    def raise_frame(self, cont):
        page = self.pages[cont].myFrame.tkraise()

    def updateHomePageUserList(self, userList):
        self.pages['HomePage'].updateUserList(userList)
    
    def updateHomePageGameList(self, gameList):
        self.pages['HomePage'].updateGameList(gameList)

# class Data:
#     def __init__(self):
#         self.userList = []
#         self.userFile = 'resources/profiles.json'
#         self.gameList = []
#         self.gameFile = 'resources/games.json'
#         if self.readFile(self.userFile):
#             self.userJSON = self.readFile(self.userFile)
#         else:
#             self.userJSON = {"profiles":[]}
#         for x in self.userJSON["profiles"]:
#              self.userList.append(x["name"])
        
#         if self.readFile(self.gameFile):
#             self.gameJSON = self.readFile(self.gameFile)
#         else:
#             self.gameJSON = {"games":[]}
#         for x in self.gameJSON["games"]:
#              self.gameList.append(x["title"])

#     def readFile(self, path):
#         try:
#             with open(path) as json_file:
#                 myjson = json.load(json_file) # load json file if present
#             return myjson
#         except Exception:
#             return False
    
#     def writeObjToFile(self, path, jsonObj):
#         try:
#             with open(path, "w") as f:
#                 json.dump(jsonObj, f, indent=4) #write people list
#         except Exception:
#             return False
    
#     def getUserList(self):
#         return self.userList
    
#     def getGameList(self):
#         return self.gameList

#     def refreshUserList(self):
#         self.userList = []
#         for x in self.userJSON["profiles"]:
#             self.userList.append(x["name"])
#         return self.userList

#     def refreshGameList(self):
#         self.gameList = []
#         for x in self.gameJSON["games"]:
#             self.gameList.append(x["title"])
#         print("new list = {}".format(self.gameList))
#         return self.gameList

#     def hasUser(self, user):
#         return {'name': user} in self.userJSON["profiles"]

#     def hasGame(self, game):
#         result = False
#         for x in self.gameJSON["games"]:
#             if x['title'] == game:
#                 result = True
#                 break
#         return result

#     def addUser(self, user):
#         self.userJSON["profiles"].append({'name': user})
#         print("user " + user + " added to the file")
#         self.writeObjToFile(self.userFile, self.userJSON)
#         return self.refreshUserList()
    
#     def deleteUser(self, user):
#         self.userJSON["profiles"].remove({'name': user})
#         print("user " + user + " removed from file")
#         self.writeObjToFile(self.userFile, self.userJSON)
#         return self.refreshUserList()
    
#     def addGame(self, gameTitle, gamePath, savePath):
#         self.gameJSON["games"].append({"title": gameTitle, "executable": gamePath, "saveLocation": savePath, "lastPlayer": ""})
#         print("game " + gameTitle + " added to the file")
#         self.writeObjToFile(self.gameFile, self.gameJSON)
#         return self.refreshGameList()

#     def deleteGame(self, gameTitle):
#         for x in self.gameJSON["games"]:
#             print("x is {} ".format(x))
#             if x["title"] == gameTitle:
#                 print("game found, delete")
#                 self.gameJSON["games"].remove(x)
#                 self.writeObjToFile(self.gameFile, self.gameJSON)
#         return self.refreshGameList()

    # def getDir(self):
    #     self.path = filedialog.askdirectory(initialdir = "/",title = "Select directory",mustexist=True)
    #     #print(self.path)
    #     if len(self.path) > 0:
    #         self.lblDir.config(text=self.path)

# class HomePage:
#     def __init__(self, root, controller, data):
#         self.root = root
#         self.controller = controller
#         self.data = data
#         self.myFrame = Frame(self.root)
#         self.lblHomeTitle = Label(self.myFrame, text="WELCOME TO THE HOME PAGE")
#         self.lblHomeTitle.pack()
#         self.lblSelectUser = Label(self.myFrame, text="select user")
#         self.lblSelectUser.pack()
#         self.cmbUser = ttk.Combobox(self.myFrame, values=self.data.getUserList())
#         self.cmbUser.pack()
#         self.lblSelectGame = Label(self.myFrame, text="select game")
#         self.lblSelectGame.pack()
#         self.cmbGame = ttk.Combobox(self.myFrame, values=self.data.getGameList())
#         self.cmbGame.pack()
#         self.btnRunGame = ttk.Button(self.myFrame, text="Run the game", command=lambda:self.runGame(self.cmbUser,self.cmbGame))
#         self.btnRunGame.pack()
#         self.btnUserPage = ttk.Button(self.myFrame, text="Go to user page", command=lambda:self.controller.raise_frame(UserPage))
#         self.btnUserPage.pack()
#         self.btnGamePage = ttk.Button(self.myFrame, text="Go to game page", command=lambda:self.controller.raise_frame(GamePage))
#         self.btnGamePage.pack()
#         #self.btnAddGame = ttk.Button(self.myFrame, text="Add game 3 to this list", command=self.addGame)
#         #self.btnAddGame.pack()
    
#     # def addGame(self):
#     #     self.data.gameList.append("game 3")
#     #     self.cmbGame['values'] = self.gameList
#     #     print(self.gameList)
    
#     # def readFile(self, path):
#     #     try:
#     #         with open(path) as json_file:
#     #             myjson = json.load(json_file) # load json file if present
#     #         return myjson
#     #     except Exception:
#     #         return False

#     def runGame(self, currentUser, currentGame):
#         #self.currentGame = currentGame
#         print(currentUser.get() + " ran the game : " + currentGame.get())

#     def updateUserList(self, userList):
#         self.cmbUser['values'] = userList
    
#     def updateGameList(self, gameList):
#         self.cmbGame['values'] = gameList

# class UserPage:
#     def __init__(self, root, controller, data):
#         self.root = root
#         self.controller = controller
#         self.data = data
#         self.userFile = self.data.userFile
#         self.myFrame = Frame(self.root)
#         self.lblUserTitle = Label(self.myFrame, text="THIS IS THE USER PAGE")
#         self.lblUserTitle.pack()
#         self.lblAddUser = Label(self.myFrame, text="SPECIFY A USERNAME TO ADD")
#         self.lblAddUser.pack()
#         self.entUsername = Entry(self.myFrame)
#         self.entUsername.pack()
#         self.btnAddUser = ttk.Button(self.myFrame, text="ADD USER", command=lambda:self.addUser(self.entUsername))
#         self.btnAddUser.pack()
#         self.cmbUserList = ttk.Combobox(self.myFrame, values=self.data.getUserList())
#         self.cmbUserList.pack()
#         self.btnDeleteUser = ttk.Button(self.myFrame, text="DELETE USER", command=lambda:self.deleteUser(self.cmbUserList))
#         self.btnDeleteUser.pack()
#         self.btnHomePage = ttk.Button(self.myFrame, text="Go back to home page", command=lambda:self.controller.raise_frame(HomePage))
#         self.btnHomePage.pack()

#     def addUser(self, user):
#         trimmed = user.get().strip()
#         if trimmed:
#             if not self.data.hasUser(trimmed):
#                 updatedList = self.data.addUser(trimmed)
#                 print("updated list is {}".format(updatedList))
#                 self.cmbUserList['values'] = updatedList #updatedUserList#update list from addUser return
#                 #self.controller.pages[HomePage].updateUserList(updatedUserList)
#                 self.controller.updateHomePageUserList(updatedList)
#                 user.delete(0,END)
#             else:
#                 print("User already exists")
#         else:
#             print("Please provide a username to add. The Entry box should be cleared")
#             user.delete(0,END)

#     def deleteUser(self, user):
#         if user.get():
#             print("user provided")
#             if self.data.hasUser(user.get()):
#                 updatedList = self.data.deleteUser(user.get())
#                 self.cmbUserList['values'] = updatedList
#                 #self.controller.pages[HomePage].updateUserList(updatedUserList)
#                 self.controller.updateHomePageUserList(updatedList)
#                 self.cmbUserList.set('')
#             else:
#                 print("User does not exist")
#         else:
#             print("No user provided")

# class GamePage:
#     def __init__(self, root, controller, data):
#         self.root = root
#         self.controller = controller
#         self.data = data
#         self.gameFile = self.data.gameFile
#         self.myFrame = Frame(self.root)
#         self.lblGameTitle = Label(self.myFrame, text="WELCOME TO THE GAME PAGE")
#         self.lblGameTitle.pack()
#         self.lblGameName = Label(self.myFrame, text="enter game name")
#         self.lblGameName.pack()
#         self.entGamename = Entry(self.myFrame)
#         self.entGamename.pack()
#         self.lblGamePath = Label(self.myFrame, text="game path '.exe' or 'steam://rungameid/XXXXXX'")
#         self.lblGamePath.pack()
#         self.entGamePath = Entry(self.myFrame)
#         self.entGamePath.pack()
#         self.btnGameBrowse = ttk.Button(self.myFrame, text="Browse ...", command=self.getFile)
#         self.btnGameBrowse.pack()
#         self.lblGameSave = Label(self.myFrame, text="game save location")
#         self.lblGameSave.pack()
#         self.entGameSave = Entry(self.myFrame)
#         self.entGameSave.pack()
#         self.btnGameSaveBrowse = ttk.Button(self.myFrame, text="Browse ...", command=self.getDir)
#         self.btnGameSaveBrowse.pack()
#         self.btnAddGame = ttk.Button(self.myFrame, text="Add game", command=lambda:self.addGame(self.entGamename, self.entGamePath, self.entGameSave))
#         self.btnAddGame.pack()
#         self.lblDeleteGame = Label(self.myFrame, text="delete game")
#         self.lblDeleteGame.pack()
#         self.cmbGameList = ttk.Combobox(self.myFrame, values=self.data.getGameList())
#         self.cmbGameList.pack()
#         self.btnDeleteGame = ttk.Button(self.myFrame, text="Delete game", command=lambda:self.deleteGame(self.cmbGameList))
#         self.btnDeleteGame.pack()


#         self.btnHomePage = ttk.Button(self.myFrame, text="Go back to home page", command=lambda:self.controller.raise_frame(HomePage))
#         self.btnHomePage.pack()

#     def getFile(self):
#         finalPath = ''
#         filepath = filedialog.askopenfilename(parent=self.root, initialdir="/", filetypes=(("shortcuts", ".lnk .url"), ("all files", "*.*")))
#         if filepath.lower().endswith(('.url')):
#             #FIND THE TARGET OF THE LNK OR URL
#             url = ''
#             with open(filepath, "r") as infile:
#                 for line in infile:
#                     if (line.startswith('URL')):
#                         url = line[4:]
#                         break
#             print("THIS IS A URL LINK " + url)
#             finalPath = url
#         elif filepath.lower().endswith(('.lnk')):
#             target = pylnk3.parse(filepath).path.replace('\\','/')
#             finalPath = target
#             print("THIS IS AN LNK " + target)
#         elif len(filepath) > 0:
#             finalPath = filepath
#             print("THIS IS THE SELECTED PATH " + finalPath)
#             #lblFile.config(text=filepath)
#         if len(finalPath) > 0:
#             self.entGamePath.delete(0,END)
#             self.entGamePath.insert(0,finalPath.strip())

#     def getDir(self):
#         path = filedialog.askdirectory(initialdir = "/", title = "Select directory", mustexist=True)
#         #print(path)
#         if len(path) > 0:
#             #lblDir.config(text=path)
#             self.entGameSave.delete(0,END)
#             self.entGameSave.insert(0,path.strip())
    
#     def addGame(self, title, path, savePath):
#         if not self.data.hasGame(title):
#             trimTitle = title.get().strip()
#             trimPath = path.get().strip()
#             trimSavePath = savePath.get().strip()
#             updatedList = self.data.addGame(trimTitle, trimPath, trimSavePath)
#             self.cmbGameList['values'] = updatedList
#             self.controller.updateHomePageGameList(updatedList)
#             print("game added")
#             title.delete(0,END)
#             path.delete(0,END)
#             savePath.delete(0,END)

#     def deleteGame(self, title):
#         if title.get():
#             print("game provided")
#             if self.data.hasGame(title.get()):
#                 updatedList = self.data.deleteGame(title.get())
#                 self.cmbGameList['values'] = updatedList
#                 self.controller.updateHomePageGameList(updatedList)
#                 self.cmbGameList.set('')
#                 print("game deleted")



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