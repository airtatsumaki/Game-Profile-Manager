import os
from tkinter import filedialog
from tkinter import *
from Person import Person
import subprocess

w = 350
h = 250

def raise_frame(frame):
    frame.tkraise()

root = Tk()
root.minsize(w,h)

page2 = Frame(root)
page2.place(x=0, y=0, width=w, height=h)

p2_title = Label(page2, text="THIS IS THE SECOND PAGE")
p2_title.place(anchor="n", relx=0.5, y=180)

btn_gotopage1 = Button(page2, text="Lets go to page 1", fg="black",command=lambda:raise_frame(page1))
btn_gotopage1.place(anchor="n", relx=0.5, y=210)

page1 = Frame(root)
page1.place(x=0, y=0, width=w, height=h)

p1_title = Label(page1, text="THIS IS THE FIRST PAGE")
p1_title.place(anchor="n", relx=0.5, y=20)

btn_gotopage2 = Button(page1, text="Lets go to page 2", fg="black",command=lambda:raise_frame(page2))
btn_gotopage2.place(anchor="n", relx=0.5, y=50)

root.mainloop()
""" selectedFile = ""
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
    path = filedialog.askopenfilename(initialdir = "/",title = "Select file")
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
    subprocess.Popen(r"C:\Program Files (x86)\Steam\Steam.exe -applaunch 750920")
    

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
root.mainloop() """