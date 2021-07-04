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
        #self.myFrame.grid_columnconfigure(0, minsize=30)#empty left column?
        self.lblHomeTitle = ttk.Label(self.myFrame, text="Game Profile Manager")
        self.lblHomeTitle.pack()
        #self.lblHomeTitle.grid(row=1, column=2, pady=10, columnspan=2)
        self.lblSelectGame = ttk.Label(self.myFrame, text="select game")
        self.lblSelectGame.place(x=20, y=20)
        #self.lblSelectUser.grid(row=2, column=1, sticky=W)
        self.cmbGame = ttk.Combobox(self.myFrame, state="readonly", values=self.data.getGameList())
        self.cmbGame.place(x=20, y=40)
        #self.cmbUser.grid(row=3, column=1)
        self.lblSelectUser = ttk.Label(self.myFrame, text="select user")
        self.lblSelectUser.place(x=20, y=65)
        self.cmbUser = ttk.Combobox(self.myFrame, state="readonly", values=self.data.getUserList())
        self.cmbUser.place(x=20, y=85)
        self.btnRunGame = ttk.Button(self.myFrame, text="Run the game", command=lambda:self.runGame(self.cmbUser,self.cmbGame))
        self.btnRunGame.place(x=20, y=120)
        self.btnGamePage = ttk.Button(self.myFrame, text="Go to game page", command=lambda:self.controller.raise_frame('GamePage'))
        self.btnGamePage.place(x=175, y=38)
        self.btnUserPage = ttk.Button(self.myFrame, text="Go to user page", command=lambda:self.controller.raise_frame('UserPage'))
        self.btnUserPage.place(x=175, y=83)
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