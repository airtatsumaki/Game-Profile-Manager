import os
from tkinter import *
from tkinter import filedialog
import pylnk3
import subprocess
import webbrowser

selectedFile = ""

root = Tk()
root.title("Open file app")
root.minsize(300,200)


lblDir = Label(root, text="select a directory and this text will update")
lblFile = Label(root, text="select a file and this text will update")
lblDir.pack()

def getDir():
    path = filedialog.askdirectory(initialdir = "/",title = "Select directory",mustexist=True)
    #print(path)
    if len(path) > 0:
        lblDir.config(text=path)

def getFile():
    filepath = filedialog.askopenfilename(parent=root, initialdir="/", filetypes=(("shortcuts", ".lnk .url"), ("all files", "*.*")))
    if filepath.lower().endswith(('.url')):
        #FIND THE TARGET OF THE LNK OR URL
        url = ''
        with open(filepath, "r") as infile:
            for line in infile:
                if (line.startswith('URL')):
                    url = line[4:]
                    break
        print(url)
    elif filepath.lower().endswith(('.lnk')):
        target = pylnk3.parse(filepath).path.replace('\\','/')
        print(target)
    global selectedFile
    #print(filepath)
    if len(filepath) > 0:
        selectedFile = filepath
        print(selectedFile)
        lblFile.config(text=filepath)
        
def openFile(filePath):
    print("inside openFile function")
    print(filePath)
    if filePath:
        #subprocess.Popen(filePath)
        os.startfile(filePath)
    else:
        print("You need to select a file before running it")

def runSteamGame():
    #subprocess.Popen("C:/Program Files (x86)/Steam/Steam.exe -applaunch 750920")
    webbrowser.open('steam://rungameid/861650')
    

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