import os
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from distutils.dir_util import copy_tree
from distutils.dir_util import remove_tree
import webbrowser


class HomePage:
    def __init__(self, root, controller, data):
        self.root = root
        self.controller = controller
        self.data = data
        self.myFrame = Frame(self.root)
        self.homePageStyles = ttk.Style()
        #self.myFrame.grid_columnconfigure(0, minsize=30)#empty left column?
        self.lblHomeTitle = ttk.Label(self.myFrame, text="Game Profile Manager", font=("Helvetica", 28))
        self.lblHomeTitle.place(x=120, y=20)
        #self.lblHomeTitle.grid(row=1, column=2, pady=10, columnspan=2)
        self.lblSelectGame = ttk.Label(self.myFrame, text="Select game", font=("Helvetica", 10))
        self.lblSelectGame.place(x=133, y=90)
        #self.lblSelectUser.grid(row=2, column=1, sticky=W)
        self.cmbGame = ttk.Combobox(self.myFrame, state="readonly", values=self.data.getGameList(), width=16, font="Helvetica 12")
        self.cmbGame.place(x=130, y=110)
        #self.cmbUser.grid(row=3, column=1)
        self.lblSelectUser = ttk.Label(self.myFrame, text="Select user", font=("Helvetica", 10))
        self.lblSelectUser.place(x=133, y=150)
        self.cmbUser = ttk.Combobox(self.myFrame, state="readonly", values=self.data.getUserList(), width=16, font="Helvetica 12")
        self.cmbUser.place(x=130, y=170)
        self.homePageStyles.configure('mgm.TButton', font=('Helvetica', 10))
        self.btnGamePage = ttk.Button(self.myFrame, text="Game management", style='mgm.TButton', command=lambda:self.controller.raise_frame('GamePage'))
        self.btnGamePage.place(x=345, y=90, width=140, height=45)
        self.btnUserPage = ttk.Button(self.myFrame, text="Profile management", style='mgm.TButton', command=lambda:self.controller.raise_frame('UserPage'))
        self.btnUserPage.place(x=345, y=150, width=140, height=45)
        self.homePageStyles.configure('runGame.TButton', font=('Helvetica', 14))
        self.btnRunGame = ttk.Button(self.myFrame, text="Play game", style='runGame.TButton', command=lambda:self.runGame(self.cmbUser,self.cmbGame))
        self.btnRunGame.place(x=130, y=235, width=140, height=45)
        #self.btnAddGame = ttk.Button(self.myFrame, text="Add game 3 to this list", command=self.addGame)
        #self.btnAddGame.pack()

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
            print("Select a valid game and user from the list")


    def updateUserList(self, userList):
        self.cmbUser['values'] = userList
    
    def updateGameList(self, gameList):
        self.cmbGame['values'] = gameList
    
    def clearForm(self):
        self.cmbUser.set('')
        self.cmbGame.set('')