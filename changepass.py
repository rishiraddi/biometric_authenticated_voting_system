import os
import sys
from tkinter import *
from PIL import ImageTk, Image
import customtkinter
import sqlite3 as sq
import smtplib
import random

connection=sq.connect('users.db')
cursor=connection.cursor()

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")



class Changepasspage():
    def __init__(self,window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Change Password')
        self.bg_frame = Image.open('images\\background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        # ====== Black Frame =========================
        self.sidebar_frame = Frame(self.window, bg='#040405', width=600, height=600)
        self.sidebar_frame.place(x=360, y=70)
        #======Title===================================
        self.txt = "Change Password"
        self.heading = Label(self.sidebar_frame, text=self.txt, font=('Times new Roman', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=0, y=20, width=600, height=50)
        #======Textboxes=================================
        self.eid = Entry(self.sidebar_frame, width=30, font=("yu gothic ui", 13))
        self.eid.place(x=250, y=109)
        self.eid_label = Label(self.sidebar_frame, text="Email :", font=("yu gothic ui", 13), fg='#ffffff',
                               bg='#040405')
        self.eid_label.place(x=50, y=109)
        self.pss = Entry(self.sidebar_frame, width=30, font=("yu gothic ui", 13),show="*")
        self.pss.place(x=250, y=159)
        self.pss_label = Label(self.sidebar_frame, text="Password :", font=("yu gothic ui", 13), fg='#ffffff',
                               bg='#040405')
        self.pss_label.place(x=50, y=159)
        self.show_image = ImageTk.PhotoImage \
            (file='images\\show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='images\\hide.png')

        self.show_button = Button(self.sidebar_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=535, y=165)
        self.rpss = Entry(self.sidebar_frame,width=30, font=("yu gothic ui", 13), show="*")
        self.rpss.place(x=250, y=209)
        self.rpss_label = Label(self.sidebar_frame, text="Re-enter Password :", font=("yu gothic ui", 13), fg='#ffffff',
                               bg='#040405')
        self.rpss_label.place(x=50, y=209)
        self.show_image1 = ImageTk.PhotoImage \
            (file='images\\show.png')

        self.hide_image1 = ImageTk.PhotoImage \
            (file='images\\hide.png')

        self.show_button1 = Button(self.sidebar_frame, image=self.show_image1, command=self.reshow, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button1.place(x=535, y=215)
        self.otp = Entry(self.sidebar_frame,width=15, font=("yu gothic ui", 13))
        self.otp.place(x=250, y=259)
        self.otp_label = Label(self.sidebar_frame, text="Otp Revived\n       on Email :", font=("yu gothic ui", 13), fg='#ffffff',
                               bg='#040405')
        self.otp_label.place(x=45, y=259)
        self.otpbut=Button(self.sidebar_frame,text='SEND', font=("yu gothic ui", 10, "bold"), width=10, bd=0,
                         bg='#228B22', cursor='hand2', activebackground='#3047ff', fg='white',command=self.send)
        self.otpbut.place(x=400, y=259)
        self.cng=Button(self.sidebar_frame,text='Change Password', font=("yu gothic ui", 13, "bold"), width=40, bd=0,
                         bg='#228B22', cursor='hand2', activebackground='#3047ff', fg='white',command=self.change)
        self.cng.place(x=100,y=329)
        self.can=Button(self.sidebar_frame,text='Back', font=("yu gothic ui", 13, "bold"), width=20, bd=0,
                         bg='#ff0000', cursor='hand2', activebackground='#3047ff', fg='white',command=self.login)
        self.can.place(x=200, y=549)
        self.OTP=0
    def show(self):
        self.hide_button = Button(self.sidebar_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=535, y=215)
        self.pss.config(show='')

    def hide(self):
        self.show_button = Button(self.sidebar_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=535, y=215)
        self.pss.config(show='*')
    def reshow(self):
        self.hide_button1 = Button(self.sidebar_frame, image=self.hide_image1, command=self.rehide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button1.place(x=535, y=265)
        self.rpss.config(show='')

    def rehide(self):
        self.show_button1 = Button(self.sidebar_frame, image=self.show_image1, command=self.reshow, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button1.place(x=535, y=265)
        self.rpss.config(show='*')
    def login(self):
        os.system('python LoginPage.py')
        sys.exit()
    def send(self):
        self.OTP = random.randint(100000, 999999)
        un = self.eid.get()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        # server = smtplib.SMTP('64.233.184.108',587)           #IP address of smtp.gmail.com to bypass DNS resolution
        server.starttls()

        valid_receiver_email = un
        password = "cyjgbratokxettzl"
        server.login("rishiraddi@gmail.com", password)

        body = "Hello" + "," + "\n" + "\n" + "Your OTP is " + str(self.OTP) + "."
        subject = "OTP verification using python"
        message = f'subject:{subject}\n\n{body}'
        server.sendmail("rishiraddi@gmail.com", valid_receiver_email, message)
        server.quit()
    def change(self):
        un = self.eid.get()
        ps = self.pss.get()
        rps = self.rpss.get()
        if self.OTP==int(self.otp.get()):
            if ps == rps:
                try:
                    cursor.execute("UPDATE reg_users SET Password=? WHERE Email = ?", (ps, un,))
                    connection.commit()
                    self.det = Listbox(bg='#040405', font=("yu gothic ui", 13, "bold"), fg='#FF0000', borderwidth=10)
                    self.det.insert(0, "Password Successfully changed")
                    self.det.config(state='disabled')
                    self.det.place(x=400, y=459, width=300, height=60)
                except:
                    self.det = Listbox(bg='#040405', font=("yu gothic ui", 13, "bold"), fg='#FF0000',
                                       borderwidth=10)
                    self.det.insert(0, "Email id not found")
                    self.det.config(state='disabled')
                    self.det.place(x=400, y=459, width=300, height=60)

            else:
                self.det = Listbox(bg='#040405', font=("yu gothic ui", 13, "bold"), fg='#FF0000', borderwidth=10)
                self.det.insert(0, "Passwords don't match")
                self.det.config(state='disabled')
                self.det.place(x=400, y=459, width=300, height=60)

        else:
            self.det = Listbox(bg='#040405', font=("yu gothic ui", 13, "bold"), fg='#FF0000', borderwidth=10)
            self.det.insert(0, "Invalid Otp")
            self.det.config(state='disabled')
            self.det.place(x=400, y=459, width=300, height=60)



def page():
    window = Tk()
    Changepasspage(window)
    window.mainloop()




if __name__ == '__main__':
    page()