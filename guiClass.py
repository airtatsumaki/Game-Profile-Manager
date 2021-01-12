import os
from tkinter import *
from tkinter import filedialog
from Person import Person
import pylnk3
import subprocess
import webbrowser

selectedFile = ""

# root = Tk()
# root.title("Open file app")
# root.minsize(300,200)

def main():
    root = Tk()
    root.title("Open file app")
    root.minsize(300,200)
    runapp = MyApp(root)
    root.mainloop()
    return None



class MyApp:
    def __init__(self, root):
        self.root = root
        self.frames = {}

        for x in (HomePage, UserPage):
            page = x(self.root, self)
            self.frames[x] = page.myFrame
            page.myFrame.place(x=0, y=0, width=300, height=200)
        
        self.raise_frame(HomePage)
        #x = HomePage(self.root)
        #self.frames[HomePage] = x.homePage
        # x.homePage.pack()
        # self.raise_frame(HomePage)
        # self.root.title("Open file app")
        # self.lblDir = Label(self.root, text="select a directory and this text will update")
        # self.lblDir.pack()
        # self.btnOpenDir = Button(self.root, text="Choose directory...", fg="black", command=self.getDir)
        # self.btnOpenDir.pack()
        # self.btnUserPage = Button(self.root, text="Go to user page", fg="black", command=lambda:raise_frame(page1))
        #self.root.mainloop()
    def raise_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        return None
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
        #self.homePage.pack() 
        self.lblHomeTitle = Label(self.myFrame, text="WELCOME TO THE HOME PAGE")
        self.lblHomeTitle.pack()
        self.btnUserPage = Button(self.myFrame, text="Go to user page", fg="black", command=lambda:controller.raise_frame(UserPage))
        self.btnUserPage.pack()

class UserPage:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.myFrame = Frame(self.root)
        #self.homePage.pack() 
        self.lblUserTitle = Label(self.myFrame, text="THIS IS THE USER PAGE")
        self.lblUserTitle.pack()
        self.btnHomePage = Button(self.myFrame, text="Go back to home page", fg="black", command=lambda:controller.raise_frame(HomePage))
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

