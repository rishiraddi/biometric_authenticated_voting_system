import os
import sys
from tkinter import *
from PIL import ImageTk, Image
import customtkinter
import sqlite3 as sq
import cv2 as im
import numpy as np
connection=sq.connect('kar.db')
cursor=connection.cursor()

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")



class Addpage():
    def __init__(self,window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Adding a new voter')
        self.bg_frame = Image.open('images\\background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        # ====== Black Frame =========================
        self.sidebar_frame = Frame(self.window, bg='#040405', width=1000, height=600)
        self.sidebar_frame.place(x=180, y=70)
        #======Title===================================
        self.txt = "Adding a new voter"
        self.heading = Label(self.sidebar_frame, text=self.txt, font=('Times new Roman', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=180, y=20, width=600, height=50)
        self.mainlable=Label(self.sidebar_frame, text="Select :", font=("yu gothic ui", 13), fg='#ffffff',
                               bg='#040405')
        self.mainlable.place(x=50, y=69)
        #========Dropdownboxes==========================
        self.selectedstate = StringVar()
        self.selectedstate.set("Select State")
        state=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
        self.state=OptionMenu( self.sidebar_frame,self.selectedstate, *state)
        self.state.config(cursor='hand2')
        self.state_lable=Label(self.sidebar_frame,text="State ",font=("yu gothic ui", 13),fg='#ffffff',bg='#040405')
        self.state.place(x=120, y=99)
        self.state_lable.place(x=50, y=99)
        self.nxt=Button(self.sidebar_frame, text='Next', font=("yu gothic ui", 8, "bold"), width=10,
                          bd=0,
                          bg='#228B22', cursor='hand2', activebackground='#3047ff', fg='white',command=self.dist)
        self.nxt.place(x=230, y=105)

        # ========Textboxes==========================
        self.uid = Entry(self.sidebar_frame, width=30, font=("yu gothic ui", 13))
        self.uid.place(x=600, y=89)
        self.uid_label = Label(self.sidebar_frame, text="Unique Id :", font=("yu gothic ui", 13), fg='#ffffff',
                                bg='#040405')
        self.uid_label.place(x=500, y=89)
        self.name = Entry(self.sidebar_frame, width=30, font=("yu gothic ui", 13))
        self.name.place(x=600, y=129)
        self.name_label = Label(self.sidebar_frame, text="Name :", font=("yu gothic ui", 13), fg='#ffffff',
                               bg='#040405')
        self.name_label.place(x=500, y=129)
        self.addr = Entry(self.sidebar_frame, width=30, font=("yu gothic ui", 13))
        self.addr.place(x=600, y=169)
        self.addr_label = Label(self.sidebar_frame, text="Address :", font=("yu gothic ui", 13), fg='#ffffff',
                                bg='#040405')
        self.addr_label.place(x=500, y=169)
        self.bio = Button(self.sidebar_frame, text='Capture Fingerprint', font=("yu gothic ui", 13, "bold"), width=26, bd=0,
                          bg='#228B22', cursor='hand2', activebackground='#3047ff', fg='white')
        self.bio.place(x=605, y=309)
        self.pto = Button(self.sidebar_frame, text='Capture Photo', font=("yu gothic ui", 13, "bold"), width=26,
                          bd=0,
                          bg='#228B22', cursor='hand2', activebackground='#3047ff', fg='white',command=self.img)
        self.pto.place(x=605, y=359)
        self.can = Button(self.sidebar_frame, text='Back', font=("yu gothic ui", 13, "bold"), width=20, bd=0,
                          bg='#ff0000', cursor='hand2', activebackground='#3047ff', fg='white',command=self.home)
        self.can.place(x=105, y=549)
        self.add = Button(self.sidebar_frame, text='Add', font=("yu gothic ui", 13, "bold"), width=20,
                          bd=0,
                          bg='#228B22', cursor='hand2', activebackground='#3047ff', fg='white',command=self.add)
        self.add.place(x=635, y=549)

    def home(self):
        os.system('python home_page.py')
        sys.exit()
    def img(self):
        uq=self.uid.get()
        self.ph=im.VideoCapture(0)
        self.result, self.image = self.ph.read()
        im.imshow("Photo",self.image)
        fpath="E:\Tkinter Login Page\\New folder\\" + uq+ ".png"
        im.imwrite(fpath,self.image)



    def add(self):
        ui=self.uid.get()
        nm=self.name.get()
        ad=self.addr.get()
        st=self.selectedstate.get()
        dst=self.selecteddist.get()
        con=self.selectedtq.get()
        try:
            cursor.execute('INSERT INTO voters (Unique_id,Name,Address,State,District,Constiuency) VALUES (?,?,?,?,?,?)', (ui, nm, ad,st,dst,con))
            connection.commit()
            self.det = Listbox(bg='#040405', font=("yu gothic ui", 13, "bold"), fg='#FF0000', borderwidth=10)
            self.det.insert(0, "Added Successfully")
            self.det.config(state='disabled')
            self.det.place(x=300, y=559, width=300, height=60)
        except:
            self.det = Listbox(bg='#040405', font=("yu gothic ui", 13, "bold"), fg='#FF0000', borderwidth=10)
            self.det.insert(0, "Unable to add")
            self.det.config(state='disabled')
            self.det.place(x=300, y=559, width=300, height=60)

    def dist(self):
        if self.selectedstate.get() == "Karnataka":
            self.selecteddist = StringVar()
            self.selecteddist.set("Select District")
            dist = ["Bagalkot", "Bangalore Rural", "Bangalore Urban", "Belgaum", "Bellary", "Bidar", "Chamarajanagar", "Chikballapur", "Chikkamagaluru", "Chitradurga", "Dakshina Kannada", "Davanagere", "Dharwad", "Gadag", "Gulbarga", "Hassan", "Haveri", "Kodagu", "Kolar"]

            self.dist = OptionMenu(self.sidebar_frame, self.selecteddist, *dist, )
            self.dist.config(cursor='hand2')
            self.dist_lable = Label(self.sidebar_frame, text="District ", font=("yu gothic ui", 13), fg='#ffffff',
                                    bg='#040405')
            self.dist.place(x=120, y=139)
            self.dist_lable.place(x=50, y=139)
            self.nxt1 = Button(self.sidebar_frame, text='Next', font=("yu gothic ui", 8, "bold"), width=10,
                               bd=0,
                               bg='#228B22', cursor='hand2', activebackground='#3047ff', fg='white', command=self.con)
            self.nxt1.place(x=240, y=150)
    def con(self):
        if self.selecteddist.get() == "Bagalkot":
            self.selectedtq = StringVar()
            self.selectedtq.set("Select Constituency")
            tq = ["Bagalkot","Badami","Jamakhandi","Mudhol","Hungund","Terdal","Bilagi"]
            tq.sort()
            self.tq = OptionMenu(self.sidebar_frame, self.selectedtq, *tq)
            self.tq.config(cursor='hand2')
            self.tq_lable = Label(self.sidebar_frame, text="Constituency ", font=("yu gothic ui", 13), fg='#ffffff',
                              bg='#040405')
            self.tq.place(x=160, y=179)
            self.tq_lable.place(x=50, y=179)




def page():
    window = Tk()
    Addpage(window)
    window.mainloop()



if __name__ == '__main__':
    page()