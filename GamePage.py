import os
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import pylnk3

class GamePage:
    def __init__(self, root, controller, data):
        self.root = root
        self.controller = controller
        self.data = data
        self.gameFile = self.data.gameFile
        self.myFrame = Frame(self.root)
        self.lblGameTitle = ttk.Label(self.myFrame, text="Game Management", font=("Helvetica", 28))
        self.lblGameTitle.place(x=143, y=20)
        self.gamePageStyles = ttk.Style()
        self.gamePageStyles.configure('addGamelf.TLabelframe.Label', font=('Helvetica', 10))
        self.gamePageStyles.configure('browse.TButton', font=('Helvetica', 10))
        #self.addGameFrame = ttk.LabelFrame(self.myFrame, text='Add game', style='addGamelf.TLabelframe')
        #self.addGameFrame.place(x=20, y=100, width=290)
        self.lblAddGame = ttk.Label(self.myFrame, text="Add game", font="Helvetica 10 underline")
        self.lblAddGame.place(x=55, y=100)
        self.lblGameName = ttk.Label(self.myFrame, text="Name", font=("Helvetica", 10))
        self.lblGameName.place(x=55, y=120)
        self.entGamename = Entry(self.myFrame, font=("Helvetica", 12))
        self.entGamename.place(x=52, y=140)
        self.lblGamePath = ttk.Label(self.myFrame, text=".exe or steam URL 'steam://rungameid/XXXXXX'", font=('Helvetica', 10))
        self.lblGamePath.place(x=55, y=165)
        self.entGamePath = Entry(self.myFrame, font=("Helvetica", 12))
        self.entGamePath.place(x=52, y=185)
        self.btnGameBrowse = ttk.Button(self.myFrame, text="Browse ...", style="browse.TButton", command=self.getFile)
        self.btnGameBrowse.place(x=250, y=184)
        self.lblGameSave = ttk.Label(self.myFrame, text="Save file location", font=("Helvetica", 10))
        self.lblGameSave.place(x=55, y=210)
        self.entGameSave = Entry(self.myFrame, font=("Helvetica", 12))
        self.entGameSave.place(x=52, y=230)
        self.btnGameSaveBrowse = ttk.Button(self.myFrame, text="Browse ...", style="browse.TButton", command=self.getDir)
        self.btnGameSaveBrowse.place(x=250, y=229)
        self.btnAddGame = ttk.Button(self.myFrame, text="Add game", style="browse.TButton", command=lambda:self.addGame(self.entGamename, self.entGamePath, self.entGameSave))
        self.btnAddGame.place(x=52, y=275)

        self.lblDeleteGame = ttk.Label(self.myFrame, text="delete game", font="Helvetica 10")
        self.lblDeleteGame.place(x=395, y=100)
        self.cmbGameList = ttk.Combobox(self.myFrame, state="readonly", values=self.data.getGameList(), width=16, font=("Helvetica", 12))
        self.cmbGameList.place(x=392, y=120)
        self.btnDeleteGame = ttk.Button(self.myFrame, text="Delete game", style="browse.TButton", command=lambda:self.deleteGame(self.cmbGameList))
        self.btnDeleteGame.place(x=392, y=165)

        #self.btnHomePage = ttk.Button(self.myFrame, text="Home", command=lambda:self.controller.raise_frame('HomePage'))
        #self.btnHomePage.place(x=0, y=0)

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
            if not(trimTitle or trimGamePath or trimSavePath):
                print("no game/ path/ save provided")
            else:
                updatedList = self.data.addGame(trimTitle, trimGamePath, trimSavePath)
                self.cmbGameList['values'] = updatedList
                self.controller.updateHomePageGameList(updatedList)
                print("game added")
                title.delete(0,END)
                path.delete(0,END)
                savePath.delete(0,END)
                messagebox.showinfo("Game added","Game '" + trimTitle + "' has been added successfully.")
        else:
            messagebox.showwarning("Game not added","Game: '" + title.get().strip() + "' already exists. \nPlease choose another game name.")
            print("game already exists")

    def deleteGame(self, title):
        if title.get():
            print("game provided")
            if self.data.hasGame(title.get()):
                updatedList = self.data.deleteGame(title.get())
                self.cmbGameList['values'] = updatedList
                self.controller.updateHomePageGameList(updatedList)
                self.cmbGameList.set('')
                messagebox.showinfo("Game deleted","Game: '" + title.get() + "' has been deleted successfully.")
                print("game deleted")

    def clearForm(self):
        self.cmbGameList.set('')
        self.entGamename.delete(0,END)
        self.entGamePath.delete(0,END)
        self.entGameSave.delete(0,END)