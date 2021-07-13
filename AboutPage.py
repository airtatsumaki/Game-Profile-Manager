from tkinter import *
from tkinter import ttk
import webbrowser

class AboutPage:
    def __init__(self, root, controller, data):
        self.root = root
        self.controller = controller
        self.data = data
        self.myFrame = Frame(self.root)
        #Hyperlink
        self.hyperlink = ttk.Label(self.myFrame, text=r"https://github.com/airtatsumaki/Game-Profile-Manager", cursor="hand2")
        self.hyperlink.bind("<Button-1>", self.callback)
        self.hyperlink.place(x=0,y=0)
    
    def callback(self,event):
        webbrowser.open_new(event.widget.cget("text"))
    
    def clearForm(self):
        False