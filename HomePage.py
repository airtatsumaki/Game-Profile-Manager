import os
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from distutils.dir_util import copy_tree
from distutils.dir_util import remove_tree
import webbrowser

class HomePage:
    def __init__(self, root, controller, data):
        self.root = root
        self.controller = controller
        self.data = data
        self.myFrame = Frame(self.root)
        menubar = Menu(self.root)
        gotoMenu = Menu(menubar, tearoff=0)
        gotoMenu.add_command(label="Home", command=lambda:self.controller.raise_frame('HomePage'))
        gotoMenu.add_command(label="Profile management", command=lambda:self.controller.raise_frame('UserPage'))
        gotoMenu.add_command(label="Game management", command=lambda:self.controller.raise_frame('GamePage'))
        menubar.add_cascade(label="Go to", menu=gotoMenu)
        aboutMenu = Menu(menubar, tearoff=0)
        aboutMenu.add_command(label="About", command=lambda:self.controller.raise_frame('AboutPage'))
        menubar.add_cascade(label="Help", menu=aboutMenu)
        self.root.config(menu=menubar)
        self.homePageStyles = ttk.Style()
        self.lblHomeTitle = ttk.Label(self.myFrame, text="Game Profile Manager", font=("Helvetica", 28))
        self.lblHomeTitle.place(x=120, y=20)
        self.lblSelectGame = ttk.Label(self.myFrame, text="Select game", font=("Helvetica", 10))
        self.lblSelectGame.place(x=228, y=90)
        self.cmbGame = ttk.Combobox(self.myFrame, state="readonly", values=self.data.getGameList(), width=16, font=("Helvetica", 12))
        self.cmbGame.place(x=225, y=110)
        self.lblSelectUser = ttk.Label(self.myFrame, text="Select user", font=("Helvetica", 10))
        self.lblSelectUser.place(x=228, y=150)
        self.cmbUser = ttk.Combobox(self.myFrame, state="readonly", values=self.data.getUserList(), width=16, font=("Helvetica", 12))
        self.cmbUser.place(x=225, y=170)
        #self.homePageStyles.configure('mgm.TButton', font=('Helvetica', 10))
        #self.btnGamePage = ttk.Button(self.myFrame, text="Game management", style="mgm.TButton", command=lambda:self.controller.raise_frame('GamePage'))
        #self.btnGamePage.place(x=345, y=90, width=140, height=45)
        #self.btnUserPage = ttk.Button(self.myFrame, text="Profile management", style="mgm.TButton", command=lambda:self.controller.raise_frame('UserPage'))
        #self.btnUserPage.place(x=345, y=150, width=140, height=45)
        self.homePageStyles.configure('runGame.TButton', font=("Helvetica", 14))
        self.btnRunGame = ttk.Button(self.myFrame, text="Play game", style="runGame.TButton", command=lambda:self.runGame(self.cmbUser,self.cmbGame))
        self.btnRunGame.place(x=239, y=230, width=140, height=45)
        #Hyperlink
        #self.hyperlink = ttk.Label(self.myFrame, text=r"http://www.google.com", cursor="hand2")
        #self.hyperlink.bind("<Button-1>", self.callback)
        #self.hyperlink.place(x=0,y=0)

    def runGame(self, currentUser, currentGame):
        gameTitle = currentGame.get()
        userName = currentUser.get()
        if gameTitle != "" and userName != "":
            gameObj = self.data.getGameObj(gameTitle)
            print(userName + " ran the game : " + gameObj["title"])
            #if the player does NOT have a save folder, create one for this game and profile
            if not os.path.exists("resources/games/" + gameObj["title"] + "/" + userName):
                os.makedirs("resources/games/" + gameObj["title"] + "/" + userName)
            #"\resources\Games\" + gameName + "\" + profile

            #if last player is blank, make current player the last player
            if gameObj["lastPlayer"] == "":
                print("First time being played. leave files in place. Set as new player")
                self.data.setLastPlayer(gameObj["title"], userName)
            elif gameObj["lastPlayer"] != userName:
                print("Another player was the lastPlayer. Backup their files first")
                #copy from game save folder to lastPlayer folder
                copy_tree(gameObj["saveLocation"], "resources/games/" + gameObj["title"] + "/" + gameObj["lastPlayer"])
                #clear save game folder
                remove_tree(gameObj["saveLocation"])
                #copy from currentPlayer to save folder
                copy_tree("resources/games/" + gameObj["title"] + "/" + userName, gameObj["saveLocation"])
                self.data.setLastPlayer(gameObj["title"], userName)
            
            #run the game
            if gameObj["executable"].lower().endswith('.exe'):
                os.startfile(gameObj["executable"])
            elif gameObj["executable"].lower().startswith('steam'):
                webbrowser.open(gameObj["executable"])
        else:
            messagebox.showerror("Error","Please select a valid game and profile.")
            print("Select a valid game and user from the list")


    def updateUserList(self, userList):
        self.cmbUser['values'] = userList
    
    def updateGameList(self, gameList):
        self.cmbGame['values'] = gameList

    def clearForm(self):
        self.cmbUser.set('')
        self.cmbGame.set('')