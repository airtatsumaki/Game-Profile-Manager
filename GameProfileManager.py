#create .exe file with...
#pyinstaller --noconsole guiClass.py

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

class MyApp:
    def __init__(self, root):
        self.root = root
        self.pages = {}
        if not os.path.exists("resources/"):
            os.makedirs("resources/")
        dataObj = Data()
        print("user list is: {}".format(dataObj.userList))
        print("game list is: {}".format(dataObj.gameList))

        for x in (HomePage, UserPage, GamePage):
            page = x(self.root, self, dataObj)
            self.pages[type(page).__name__] = page
            page.myFrame.place(x=0, y=0, width=616, height=381)

        self.raise_frame('HomePage')

    def raise_frame(self, cont):
        self.pages[cont].clearForm()
        page = self.pages[cont].myFrame.tkraise()

    def updateHomePageUserList(self, userList):
        self.pages['HomePage'].updateUserList(userList)
    
    def updateHomePageGameList(self, gameList):
        self.pages['HomePage'].updateGameList(gameList)

def main():
    root = Tk()
    root.title("Game Profile Manager")
    #root.minsize(300,400)
    root.geometry('{}x{}'.format(616, 381))
    runapp = MyApp(root)
    root.mainloop()

main()

