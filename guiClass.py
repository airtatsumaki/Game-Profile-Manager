import os
import json
import pylnk3
import webbrowser
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

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

    def raise_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
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
        self.lblHomeTitle = Label(self.myFrame, text="WELCOME TO THE HOME PAGE")
        self.lblHomeTitle.pack()
        self.btnUserPage = ttk.Button(self.myFrame, text="Go to user page", command=lambda:self.controller.raise_frame(UserPage))
        self.btnUserPage.pack()
        self.btnRunGame = ttk.Button(self.myFrame, text="Run the game", command=lambda:self.runGame("me","red dead 2"))
        self.btnRunGame.pack()

    def runGame(self, currentUser, currentGame):
        self.currentGame = currentGame
        print("run " + self.currentGame)
        
        return None


class UserPage:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.userFile = 'resources/profiles.json'
        if self.readFile(self.userFile):
            self.userJSON = self.readFile(self.userFile)
        else:
            self.userJSON = {"profiles":[]}
        print(self.userJSON)
        self.myFrame = Frame(self.root)
        self.lblUserTitle = Label(self.myFrame, text="THIS IS THE USER PAGE")
        self.lblUserTitle.pack()
        self.lblAddUser = Label(self.myFrame, text="SPECIFY A USERNAME TO ADD")
        self.lblAddUser.pack()
        self.entUsername = Entry(self.myFrame)
        self.entUsername.pack()
        self.btnAddUser = ttk.Button(self.myFrame, text="ADD USER", command=lambda:self.addUser(self.entUsername))
        self.btnAddUser.pack()
        self.btnHomePage = ttk.Button(self.myFrame, text="Go back to home page", command=lambda:self.controller.raise_frame(HomePage))
        self.btnHomePage.pack()
    
    def readFile(self, path):
        try:
            with open(path) as json_file:
                myjson = json.load(json_file) # load json file if present
            return myjson
        except Exception:
            return False
    
    def writeObjToFile(self, path, jsonObj):
        try:
            with open(path, "w") as f:
                json.dump(jsonObj, f, indent=4) #write people list
        except Exception:
            return False

    def addUser(self, entBox):
        #self.userJSON = self.readFile(self.userFile)
        #print(self.userJSON)
        
        trimmed = entBox.get().strip()
        if trimmed:
            found = False
            for x in self.userJSON["profiles"]:
                if x["name"] == trimmed:
                    found = True
            if not found:
                self.userJSON["profiles"].append({'name': trimmed})
                self.writeObjToFile(self.userFile, self.userJSON)
                print("user " + trimmed + " added to the file")
            else:
                print("User already exists")
        else:
            print("Please provide a username to add. The Entry box should be cleared")
            entBox.delete(0,END)
        # 
        # return None
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