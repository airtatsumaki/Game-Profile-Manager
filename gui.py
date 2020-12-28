#test git change
import os
from tkinter import *
from tkinter import filedialog
from Person import Person
import subprocess

selectedFile = ""
variable = 1

root = Tk()
root.title("Open file app")
root.minsize(300,200)

p1 = Person("Naz",35)

lblDir = Label(root, text="select a directory and this text will update")
lblFile = Label(root, text="select a file and this text will update")
lblDir.pack()

def getDir():
    path = filedialog.askdirectory(initialdir = "/",title = "Select directory",mustexist=True)
    #print(path)
    if len(path) > 0:
        lblDir.config(text=path)

def getFile():
    #path = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("application files","*.exe"),("all files","*.*")))
    #path = filedialog.askopenfilename(initialdir = "/",title = "Select file")
    path = filedialog.askopenfilename(parent=root, initialdir="/", filetypes=(("shortcuts", "*.lnk"),("internet shortcuts", "*.url"), ("all files", "*.*")))
    global selectedFile
    #print(path)
    if len(path) > 0:
        selectedFile = path
        print(selectedFile)
        lblFile.config(text=path)
        
def openFile(filePath):
    print("inside openFile function")
    print(filePath)
    if filePath:
        #subprocess.Popen(filePath)
        os.startfile(filePath)
    else:
        print("You need to select a file before running it")

def runSteamGame():
    subprocess.Popen("C:/Program Files (x86)/Steam/Steam.exe -applaunch 750920")
    

btnOpenDir = Button(root, text="Choose directory...", fg="black",command=getDir)
btnOpenDir.pack()

lblFile.pack()
btnOpenFile = Button(root, text="Choose a file...", fg="black",command=getFile)
btnOpenFile.pack()

btnRunFile = Button(root, text="Run selected file above", fg="black",command=lambda: openFile(selectedFile))
btnRunFile.pack()

btnRunSteamGame = Button(root, text="or just run a steam game id here", fg="black",command=runSteamGame)
btnRunSteamGame.pack()

#root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("application files","*.exe"),("all files","*.*")))
#root.directory = filedialog.askdirectory(initialdir = "/",title = "Select directory",mustexist=True)
#print(root.filename)
#print(root.directory)
#print(".exe" in root.filename)
#subprocess.Popen([str(root.filename)])
root.mainloop()