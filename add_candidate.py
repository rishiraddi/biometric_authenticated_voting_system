from tkinter import *
from PIL import ImageTk, Image
import customtkinter
import sys
import os

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")



class Addcanpage():
    def __init__(self,window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Adding a new candidate to a constituency')
        self.bg_frame = Image.open('images\\background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        # ====== Black Frame =========================
        self.sidebar_frame = Frame(self.window, bg='#040405', width=1000, height=600)
        self.sidebar_frame.place(x=180, y=70)
        #======Title===================================
        self.txt = "Adding a new candidate to a Constituency"
        self.heading = Label(self.sidebar_frame, text=self.txt, font=('Times new Roman', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=180, y=20, width=600, height=50)
        self.mainlable=Label(self.sidebar_frame, text="Select :", font=("yu gothic ui", 13), fg='#ffffff',
                               bg='#040405')
        self.mainlable.place(x=50, y=69)
        #========Dropdownboxes==========================
        selectedstate = StringVar()
        selectedstate.set("Select State")
        state=[1,2,3,4,5,6,7,8,9]
        self.state=OptionMenu( self.sidebar_frame,selectedstate, *state)
        self.state.config(cursor='hand2')
        self.state_lable=Label(self.sidebar_frame,text="State ",font=("yu gothic ui", 13),fg='#ffffff',bg='#040405')
        self.state.place(x=120, y=99)
        self.state_lable.place(x=50, y=99)
        selecteddist = StringVar()
        selecteddist.set("Select Distict")
        dist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.dist = OptionMenu(self.sidebar_frame, selecteddist, *dist)
        self.dist.config(cursor='hand2')
        self.dist_lable = Label(self.sidebar_frame, text="District ", font=("yu gothic ui", 13), fg='#ffffff',
                                 bg='#040405')
        self.dist.place(x=120, y=139)
        self.dist_lable.place(x=50, y=139)
        selectedtq = StringVar()
        selectedtq.set("Select Constituency")
        tq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.tq = OptionMenu(self.sidebar_frame, selectedtq, *tq)
        self.tq.config(cursor='hand2')
        self.tq_lable = Label(self.sidebar_frame, text="Constituency ", font=("yu gothic ui", 13), fg='#ffffff',
                                bg='#040405')
        self.tq.place(x=160, y=179)
        self.tq_lable.place(x=50, y=179)
        # ========Textboxes==========================
        self.uid = Entry(self.sidebar_frame, width=30, font=("yu gothic ui", 13))
        self.uid.place(x=600, y=89)
        self.uid_label = Label(self.sidebar_frame, text="Party :", font=("yu gothic ui", 13), fg='#ffffff',
                                bg='#040405')
        self.uid_label.place(x=500, y=89)
        self.name = Entry(self.sidebar_frame, width=30, font=("yu gothic ui", 13))
        self.name.place(x=600, y=129)
        self.name_label = Label(self.sidebar_frame, text="Name :", font=("yu gothic ui", 13), fg='#ffffff',
                               bg='#040405')
        self.name_label.place(x=500, y=129)
        self.addr = Text(self.sidebar_frame,height=5, width=30, font=("yu gothic ui", 13))
        self.addr.place(x=600, y=169)
        self.addr_label = Label(self.sidebar_frame, text="Address :", font=("yu gothic ui", 13), fg='#ffffff',
                                bg='#040405')
        self.addr_label.place(x=500, y=169)
        self.bio = Button(self.sidebar_frame, text='Capture Fingerprint', font=("yu gothic ui", 13, "bold"), width=26, bd=0,
                          bg='#228B22', cursor='hand2', activebackground='#3047ff', fg='white')
        self.bio.place(x=605, y=309)
        self.photo = Button(self.sidebar_frame, text='Capture Photo', font=("yu gothic ui", 13, "bold"), width=26,
                          bd=0,
                          bg='#228B22', cursor='hand2', activebackground='#3047ff', fg='white')
        self.photo.place(x=605, y=369)
        self.can = Button(self.sidebar_frame, text='Back', font=("yu gothic ui", 13, "bold"), width=20, bd=0,
                          bg='#ff0000', cursor='hand2', activebackground='#3047ff', fg='white',command=self.home)
        self.can.place(x=105, y=549)
        self.add = Button(self.sidebar_frame, text='Add', font=("yu gothic ui", 13, "bold"), width=20,
                          bd=0,
                          bg='#228B22', cursor='hand2', activebackground='#3047ff', fg='white')
        self.add.place(x=635, y=549)
    def home(self):
        os.system('python home_page.py')
        sys.exit()



def page():
    window = Tk()
    Addcanpage(window)
    window.mainloop()




if __name__ == '__main__':
    page()