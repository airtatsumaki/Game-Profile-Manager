# from tkinter import *
# from tkinter import filedialog
# from tkinter import ttk

class HomePage:
    def __init__(self, root, controller, data):
        self.root = root
        self.controller = controller
        self.data = data
        self.myFrame = Frame(self.root)
        self.lblHomeTitle = Label(self.myFrame, text="WELCOME TO THE HOME PAGE")
        self.lblHomeTitle.pack()
        self.lblSelectUser = Label(self.myFrame, text="select user")
        self.lblSelectUser.pack()
        self.cmbUser = ttk.Combobox(self.myFrame, values=self.data.getUserList())
        self.cmbUser.pack()
        self.lblSelectGame = Label(self.myFrame, text="select game")
        self.lblSelectGame.pack()
        self.cmbGame = ttk.Combobox(self.myFrame, values=self.data.getGameList())
        self.cmbGame.pack()
        self.btnRunGame = ttk.Button(self.myFrame, text="Run the game", command=lambda:self.runGame(self.cmbUser,self.cmbGame))
        self.btnRunGame.pack()
        self.btnUserPage = ttk.Button(self.myFrame, text="Go to user page", command=lambda:self.controller.raise_frame('UserPage'))
        self.btnUserPage.pack()
        self.btnGamePage = ttk.Button(self.myFrame, text="Go to game page", command=lambda:self.controller.raise_frame('GamePage'))
        self.btnGamePage.pack()
        #self.btnAddGame = ttk.Button(self.myFrame, text="Add game 3 to this list", command=self.addGame)
        #self.btnAddGame.pack()
    
    # def addGame(self):
    #     self.data.gameList.append("game 3")
    #     self.cmbGame['values'] = self.gameList
    #     print(self.gameList)
    
    # def readFile(self, path):
    #     try:
    #         with open(path) as json_file:
    #             myjson = json.load(json_file) # load json file if present
    #         return myjson
    #     except Exception:
    #         return False

    def runGame(self, currentUser, currentGame):
        #self.currentGame = currentGame
        print(currentUser.get() + " ran the game : " + currentGame.get())

    def updateUserList(self, userList):
        self.cmbUser['values'] = userList
    
    def updateGameList(self, gameList):
        self.cmbGame['values'] = gameList