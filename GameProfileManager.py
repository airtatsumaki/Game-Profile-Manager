#create .exe file with...
#pyinstaller --noconsole guiClass.py

import os
import json
import pylnk3
import webbrowser
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from Data import Data
from HomePage import HomePage
from UserPage import UserPage
from GamePage import GamePage
from AboutPage import AboutPage

class MyApp:
    def __init__(self, root):
        self.root = root
        self.pages = {}
        if not os.path.exists("resources/"):
            os.makedirs("resources/")
        dataObj = Data()
        print("user list is: {}".format(dataObj.userList))
        print("game list is: {}".format(dataObj.gameList))

        for x in (HomePage, UserPage, GamePage, AboutPage):
            page = x(self.root, self, dataObj)
            self.pages[type(page).__name__] = page
            page.myFrame.place(x=0, y=0, width=616, height=381)

        self.raise_frame('HomePage')

        #missing files msgbox
        flags = dataObj.sendFlags()
        #print(flags)
        self.msgText = ""
        if flags["profileFlag"] == 0 and flags["gameFlag"] == 0:
            self.msgText += "Profile or Game"
        elif not(flags["profileFlag"]):
            self.msgText += "Profile"
        elif not(flags["gameFlag"]):
            self.msgText += "Game"
        if self.msgText:
            messagebox.showinfo("File(s) missing","It seems you do not have a {0} file. Not to worry, one will be created for you within the app/resources folder when you add a new {0}.".format(self.msgText))

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
    root.resizable(False, False)
    MyApp(root)
    root.mainloop()

main()

