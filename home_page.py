import os
import sys
from tkinter import *
from PIL import ImageTk, Image
import customtkinter
import pymongo as mg

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class Homepage():
    def __init__(self,window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Home Page')
        # ========================================================================
        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open('images\\background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        # ====== Black Frame =========================
        self.sidebar_frame = Frame(self.window, bg='#040405', width=1200, height=600)
        self.sidebar_frame.place(x=85, y=70)

        # ========================================================================
        # ============ Left Side Buttons ================================================
        # ========================================================================
        self.sidebar_frame=Frame(self.window, bg='#040405', width=350, height=590)
        self.sidebar_frame.place(x=90,y=75)
        self.anv = Button(text='Add a New voter', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                          bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=self.add)
        self.anv.place(x=130, y=100)
        self.upd = Button(text='Update Voter details', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                          bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=self.update)
        self.upd.place(x=130, y=160)
        self.dv = Button( text='Delete a voter', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                          bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=self.delete)
        self.dv.place(x=130, y=220)
        self.cn = Button( text='Add a Candidate', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                         bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=self.addcan)
        self.cn.place(x=130, y=280)
        self.ele = Button(text='Conduct Election', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                         bg='#228B22', cursor='hand2', activebackground='#3047ff', fg='white',command=self.conduct)
        self.ele.place(x=400, y=680, width=600, height=50)
        self.det=Listbox(bg='#040405',font=("yu gothic ui", 13, "bold"),fg='#FF0000',borderwidth=10)
        self.det.insert(0,"Important Guidelines regarding the software")
        self.det.config(state='disabled')
        self.det.place(x=450, y=75,width=825, height=590)
    def add(self):
        os.system('python add.py')
        sys.exit()
    def update(self):
        os.system('python update.py')
        sys.exit()
    def delete(self):
        os.system('python delete.py')
        sys.exit()
    def addcan(self):
        os.system('python add_candidate.py')
        sys.exit()
    def conduct(self):
        os.system('python conduct.py')
        sys.exit()






def page():
    window=Tk()
    Homepage(window)
    window.mainloop()

if __name__ == '__main__':
   page()


