from tkinter import *
from PIL import ImageTk, Image
import customtkinter
import sys
import os
import sqlite3 as sq
import base64
from PIL import Image
import io
import numpy as np
import cv2 as im

connection=sq.connect('kar.db')
cursor=connection.cursor()

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")



class Updatepage():
    def __init__(self,window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Updating voter details')
        self.bg_frame = Image.open('images\\background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        # ====== Black Frame =========================
        self.sidebar_frame = Frame(self.window, bg='#040405', width=1000, height=600)
        self.sidebar_frame.place(x=180, y=70)
        #======Title===================================
        self.txt = "Updating voter details"
        self.heading = Label(self.sidebar_frame, text=self.txt, font=('Times new Roman', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=180, y=20, width=600, height=50)
        # ========Textboxes==========================
        self.uid = Entry(self.sidebar_frame, width=20, font=("yu gothic ui", 13))
        self.uid.place(x=250, y=89)
        self.uid_label = Label(self.sidebar_frame, text="Enter Unique Id :", font=("yu gothic ui", 13), fg='#ffffff',
                                bg='#040405')
        self.uid_label.place(x=100, y=89)
        self.det = Button(self.sidebar_frame, text='Get Details', font=("yu gothic ui", 10, "bold"), width=26,
                          bd=0,
                          bg='#228B22', cursor='hand2', activebackground='#3047ff', fg='white',command=self.get_det)
        self.det.place(x=500, y=89)
        self.detiet_label = Label(self.sidebar_frame, text="Update", font=("yu gothic ui", 13), fg='#ffffff',
                               bg='#040405')
        self.detiet_label.place(x=850, y=89)
        detit1=IntVar
        detit2 = IntVar
        self.detitems1=Button(self.sidebar_frame, text = "Name", height = 0, width = 10,bg='#228B22',fg='#ffffff',font=("yu gothic ui", 13, "bold"),command=self.cng_name)
        self.detitems1.place(x=840, y=119)
        self.detitems2 = Button(self.sidebar_frame, text="Address",  height=0,width=10,bg='#228B22',fg='#ffffff',font=("yu gothic ui", 13, "bold"),command=self.cng_addr)
        self.detitems2.place(x=840, y=259)
        self.bio = Button(self.sidebar_frame, text='Capture Fingerprint', font=("yu gothic ui", 13, "bold"), width=26, bd=0,
                          bg='#228B22', cursor='hand2', activebackground='#3047ff', fg='white')
        self.bio.place(x=350, y=459)
        self.can = Button(self.sidebar_frame, text='Back', font=("yu gothic ui", 13, "bold"), width=20, bd=0,
                          bg='#ff0000', cursor='hand2', activebackground='#3047ff', fg='white',command=self.home)
        self.can.place(x=105, y=549)
        self.add = Button(self.sidebar_frame, text='Update', font=("yu gothic ui", 13, "bold"), width=20,
                          bd=0,
                          bg='#228B22', cursor='hand2', activebackground='#3047ff', fg='white',command=self.done)
        self.add.place(x=635, y=549)
    def home(self):
        os.system('python home_page.py')
        sys.exit()
    def get_det(self):
        uq=self.uid.get()
        cursor.execute("SELECT * FROM voters WHERE Unique_id = ?", (uq,))
        em = cursor.fetchone()
        self.voter_image = Image.open("E:\Tkinter Login Page\\New folder\\" + uq+ ".png")
        self.original_width, self.original_height = self.voter_image.size
        ratio = min(200 / self.original_width, 200 / self.original_height)
        self.new_width = int(self.original_width * ratio)
        self.new_height = int(self.original_height * ratio)
        self.new_image=self.voter_image.resize((self.new_width,self.new_height),Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.new_image)
        self.voter_image_lbl=Label(self.sidebar_frame,image=self.photo)
        self.voter_image_lbl.place(x=500, y=129)
        self.det = Listbox(self.sidebar_frame,bg='#040405', font=("yu gothic ui", 13, "bold"), fg='#FF0000', borderwidth=10)
        cursor.execute("SELECT * from voters WHERE Unique_id=?",(uq,))
        nm=cursor.fetchone()
        self.det.insert(0, "Name-"+nm[1])
        self.det.insert(1,"Address-"+nm[2])
        self.det.insert(2, "State-" + nm[3])
        self.det.insert(3, "District-" + nm[4])
        self.det.insert(4, "Constituency-" + nm[5])
        self.det.config(state='disabled')
        self.det.place(x=100, y=129, width=300, height=150)
    def cng_name(self):
        self.new_nm = Entry(self.sidebar_frame, width=20, font=("yu gothic ui", 13))
        self.new_nm.place(x=800, y=189)
    def cng_addr(self):
        self.new_addr = Entry(self.sidebar_frame, width=20, font=("yu gothic ui", 13))
        self.new_addr.place(x=800, y=329)

    def done(self):
        self.nm=self.new_nm.get()
        self.ad=self.new_addr.get()
        self.uq=self.uid.get()
        if self.nm!='\0' and self.ad=='\0':
            try:
                cursor.execute("UPDATE voters SET Name=? WHERE Unique_id = ?", (self.nm, self.uq,))
                connection.commit()
                self.det = Listbox(bg='#040405', font=("yu gothic ui", 13, "bold"), fg='#FF0000', borderwidth=10)
                self.det.insert(0, "Successfully changed Name")
                self.det.config(state='disabled')
                self.det.place(x=350, y=359, width=350, height=60)
            except:
                self.det = Listbox(bg='#040405', font=("yu gothic ui", 13, "bold"), fg='#FF0000', borderwidth=10)
                self.det.insert(0, "Unable to change name")
                self.det.config(state='disabled')
                self.det.place(x=350, y=359, width=350, height=60)

        if self.nm=='\0' and self.ad!='\0':
            try:
                cursor.execute("UPDATE voters SET Address=? WHERE Unique_id = ?", (self.ad, self.uq,))
                connection.commit()
                self.det = Listbox(bg='#040405', font=("yu gothic ui", 13, "bold"), fg='#FF0000', borderwidth=10)
                self.det.insert(0, "successfully address changed")
                self.det.config(state='disabled')
                self.det.place(x=350, y=359, width=350, height=60)
            except:
                self.det = Listbox(bg='#040405', font=("yu gothic ui", 13, "bold"), fg='#FF0000', borderwidth=10)
                self.det.insert(0, "Unable to change address")
                self.det.config(state='disabled')
                self.det.place(x=350, y=359, width=350, height=60)
        if self.nm!='\0' and self.ad!='\0':
            try:
                cursor.execute("UPDATE voters SET Name=? WHERE Unique_id = ?", (self.nm, self.uq,))
                cursor.execute("UPDATE voters SET Address=? WHERE Unique_id = ?", (self.ad, self.uq,))
                connection.commit()
                self.det = Listbox(bg='#040405', font=("yu gothic ui", 13, "bold"), fg='#FF0000', borderwidth=10)
                self.det.insert(0, "Successfully changed name and address")
                self.det.config(state='disabled')
                self.det.place(x=350, y=359, width=350, height=60)
            except:
                self.det = Listbox(bg='#040405', font=("yu gothic ui", 13, "bold"), fg='#FF0000', borderwidth=10)
                self.det.insert(0, "Unable to change name and address")
                self.det.config(state='disabled')
                self.det.place(x=350, y=359, width=350, height=60)


def page():
    window = Tk()
    Updatepage(window)
    window.mainloop()




if __name__ == '__main__':
    page()