from tkinter import *
from tkinter import ttk
from tkinter import *  
from PIL import ImageTk, Image
import webbrowser

class AboutPage:
    def __init__(self, root, controller, data):
        self.root = root
        self.controller = controller
        self.data = data
        self.myFrame = Frame(self.root)
        self.lblHomeTitle = ttk.Label(self.myFrame, text="About", font=("Helvetica", 28))
        self.lblHomeTitle.place(x=256, y=20)
        self.version = ttk.Label(self.myFrame, font=("Helvetica", 10), text="Game Profile Manager v0.1-alpha")
        self.version.place(x=30, y=80)
        self.decription = ttk.Label(self.myFrame, font=("Helvetica", 10), text="The solution to creating multiple profiles or playthroughs of single player games.")
        self.decription.place(x=30, y=100)
        self.lblGit = ttk.Label(self.myFrame, font=("Helvetica", 10), text="GitHub:")
        self.lblGit.place(x=30, y=120)
        self.lnkGit = ttk.Label(self.myFrame, font=("Helvetica", 10, "underline"), text=r"https://github.com/airtatsumaki/Game-Profile-Manager", cursor="hand2", foreground="blue")
        self.lnkGit.bind("<Button-1>", self.callbackURL)
        self.lnkGit.place(x=80,y=120)
        self.lblDonate = ttk.Label(self.myFrame, font=("Helvetica", 10), text="If you like Game Profile Manager please consider donating to help improve the app.")
        self.lblDonate.place(x=30,y=150)

        self.paypalCanvas = Canvas(self.myFrame, width = 150, height = 50, cursor="hand2")
        self.paypalImg = ImageTk.PhotoImage(Image.open("img/paypal_logo.png"))  
        self.paypalCanvas.create_image(0, 0, anchor=NW, image=self.paypalImg)
        self.paypalCanvas.place(x=80,y=180)
        self.paypalCanvas.bind("<Button-1>", self.callbackPaypal)
        self.donateCanvas = Canvas(self.myFrame, width = 170, height = 65, cursor="hand2")
        self.dondateImg = ImageTk.PhotoImage(Image.open("img/btn_donate.png"))  
        self.donateCanvas.create_image(0, 0, anchor=NW, image=self.dondateImg)
        self.donateCanvas.place(x=80,y=250)
        self.donateCanvas.bind("<Button-1>", self.callbackPaypal)

        self.BTCanvas = Canvas(self.myFrame, width = 125, height = 30)
        self.BTImg = ImageTk.PhotoImage(Image.open("img/BT_logo.png"))  
        self.BTCanvas.create_image(5, 5, anchor=NW, image=self.BTImg)
        self.BTCanvas.place(x=370,y=180)
        self.QRCanvas = Canvas(self.myFrame, width = 80, height = 80)
        self.QRImg = ImageTk.PhotoImage(Image.open("img/BTQR_code_small.png"))  
        self.QRCanvas.create_image(0, 0, anchor=NW, image=self.QRImg)
        self.QRCanvas.place(x=396,y=230)
        self.txtBTAddress = Text(self.myFrame, height=1)
        self.txtBTAddress.insert(1.0, "1FhJtPjgQi2SGpnWCJSBAe8iM4yDRqvhz9")
        self.txtBTAddress.configure(bg=self.myFrame.cget('bg'), relief="flat")
        self.txtBTAddress.configure(state="disabled")
        self.txtBTAddress.place(x=300,y=330)
        
        



        
    def callbackPaypal(self,event):
        webbrowser.open_new(r"https://www.paypal.com/donate?hosted_button_id=E5S4XNJWDA3Q6")

    def callbackURL(self,event):
        webbrowser.open_new(event.widget.cget("text"))
    
    def clearForm(self):
        False