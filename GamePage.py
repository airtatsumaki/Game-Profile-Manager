import os
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import pylnk3

class GamePage:
    def __init__(self, root, controller, data):
        self.root = root
        self.controller = controller
        self.data = data
        self.gameFile = self.data.gameFile
        self.myFrame = Frame(self.root)
        self.lblGameTitle = ttk.Label(self.myFrame, text="WELCOME TO THE GAME PAGE")
        self.lblGameTitle.pack()
        self.lblGameName = ttk.Label(self.myFrame, text="enter game name")
        self.lblGameName.pack()
        self.entGamename = Entry(self.myFrame)
        self.entGamename.pack()
        self.lblGamePath = ttk.Label(self.myFrame, text="game path '.exe' or 'steam://rungameid/XXXXXX'")
        self.lblGamePath.pack()
        self.entGamePath = Entry(self.myFrame)
        self.entGamePath.pack()
        self.btnGameBrowse = ttk.Button(self.myFrame, text="Browse ...", command=self.getFile)
        self.btnGameBrowse.pack()
        self.lblGameSave = ttk.Label(self.myFrame, text="game save location")
        self.lblGameSave.pack()
        self.entGameSave = Entry(self.myFrame)
        self.entGameSave.pack()
        self.btnGameSaveBrowse = ttk.Button(self.myFrame, text="Browse ...", command=self.getDir)
        self.btnGameSaveBrowse.pack()
        self.btnAddGame = ttk.Button(self.myFrame, text="Add game", command=lambda:self.addGame(self.entGamename, self.entGamePath, self.entGameSave))
        self.btnAddGame.pack()
        self.lblDeleteGame = ttk.Label(self.myFrame, text="delete game")
        self.lblDeleteGame.pack()
        self.cmbGameList = ttk.Combobox(self.myFrame, state="readonly", values=self.data.getGameList())
        self.cmbGameList.pack()
        self.btnDeleteGame = ttk.Button(self.myFrame, text="Delete game", command=lambda:self.deleteGame(self.cmbGameList))
        self.btnDeleteGame.pack()

        self.btnHomePage = ttk.Button(self.myFrame, text="Go back to home page", command=lambda:self.controller.raise_frame('HomePage'))
        self.btnHomePage.pack()

    def getFile(self):
        finalPath = ''
        filepath = filedialog.askopenfilename(parent=self.root, initialdir="/", filetypes=(("shortcuts", ".lnk .url"), ("all files", "*.*")))
        if filepath.lower().endswith(('.url')):
            #FIND THE TARGET OF THE LNK OR URL
            url = ''
            with open(filepath, "r") as infile:
                for line in infile:
                    if (line.startswith('URL')):
                        url = line[4:]
                        break
            print("THIS IS A URL LINK " + url)
            finalPath = url
        elif filepath.lower().endswith(('.lnk')):
            target = pylnk3.parse(filepath).path.replace('\\','/')
            finalPath = target
            print("THIS IS AN LNK " + target)
        elif len(filepath) > 0:
            finalPath = filepath
            print("THIS IS THE SELECTED PATH " + finalPath)
            #lblFile.config(text=filepath)
        if len(finalPath) > 0:
            self.entGamePath.delete(0,END)
            self.entGamePath.insert(0,finalPath.strip())

    def getDir(self):
        path = filedialog.askdirectory(initialdir = "/", title = "Select directory", mustexist=True)
        #print(path)
        if len(path) > 0:
            #lblDir.config(text=path)
            self.entGameSave.delete(0,END)
            self.entGameSave.insert(0,path.strip())
    
    def addGame(self, title, path, savePath):
        if not self.data.hasGame(title.get().strip()):
            trimTitle = title.get().strip()
            trimGamePath = path.get().strip()
            trimSavePath = savePath.get().strip()
            if os.path.exists(trimSavePath):
                print("valid save game path")
            else:
                print("error")
            #do i need to check if the game exe/steam url etc are valid before proceeding?
            # if os.path.exists(trimGamePath):
            #     print("valid game path")
            # else:
            #     print("error")
            updatedList = self.data.addGame(trimTitle, trimGamePath, trimSavePath)
            self.cmbGameList['values'] = updatedList
            self.controller.updateHomePageGameList(updatedList)
            print("game added")
            title.delete(0,END)
            path.delete(0,END)
            savePath.delete(0,END)
        else:
            print("game already exists")

    def deleteGame(self, title):
        if title.get():
            print("game provided")
            if self.data.hasGame(title.get()):
                updatedList = self.data.deleteGame(title.get())
                self.cmbGameList['values'] = updatedList
                self.controller.updateHomePageGameList(updatedList)
                self.cmbGameList.set('')
                print("game deleted")