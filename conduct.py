from tkinter import *
from PIL import ImageTk, Image
import customtkinter
import sys
import os

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")



class Conductpage():
    def __init__(self,window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Conduct Election')
        self.bg_frame = Image.open('images\\background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        # ====== Black Frame =========================
        self.sidebar_frame = Frame(self.window, bg='#040405', width=1000, height=600)
        self.sidebar_frame.place(x=180, y=70)
        #======Title===================================
        self.txt = "Conduct Election"
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
        self.can = Button(self.sidebar_frame, text='Back', font=("yu gothic ui", 13, "bold"), width=20, bd=0,
                          bg='#ff0000', cursor='hand2', activebackground='#3047ff', fg='white',command=self.home)
        self.can.place(x=105, y=549)
        self.add = Button(self.sidebar_frame, text='Start', font=("yu gothic ui", 13, "bold"), width=20,
                          bd=0,
                          bg='#228B22', cursor='hand2', activebackground='#3047ff', fg='white')
        self.add.place(x=635, y=549)
    def home(self):
        os.system('python home_page.py')
        sys.exit()



def page():
    window = Tk()
    Conductpage(window)
    window.mainloop()




if __name__ == '__main__':
    page()