from tkinter import *
from PIL import ImageTk, Image
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")



class Startpage():
    def __init__(self,window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Verifing voter details')
        self.bg_frame = Image.open('images\\background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        # ====== Black Frame =========================
        self.sidebar_frame = Frame(self.window, bg='#040405', width=1000, height=600)
        self.sidebar_frame.place(x=180, y=70)
        #======Title===================================
        self.txt = "Verifing voter details"
        self.heading = Label(self.sidebar_frame, text=self.txt, font=('Times new Roman', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=180, y=20, width=600, height=50)
        # ========Textboxes==========================
        self.uid = Entry(self.sidebar_frame, width=30, font=("yu gothic ui", 13))
        self.uid.place(x=200, y=89)
        self.uid_label = Label(self.sidebar_frame, text="Enter Unique Id :", font=("yu gothic ui", 13), fg='#ffffff',
                                bg='#040405')
        self.uid_label.place(x=100, y=89)
        self.det = Button(self.sidebar_frame, text='Get Details', font=("yu gothic ui", 10, "bold"), width=26,
                          bd=0,
                          bg='#228B22', cursor='hand2', activebackground='#3047ff', fg='white')
        self.det.place(x=500, y=89)
        self.bio = Button(self.sidebar_frame, text='Capture Fingerprint', font=("yu gothic ui", 13, "bold"), width=26, bd=0,
                          bg='#228B22', cursor='hand2', activebackground='#3047ff', fg='white')
        self.bio.place(x=350, y=459)
        self.can = Button(self.sidebar_frame, text='Reject', font=("yu gothic ui", 13, "bold"), width=20, bd=0,
                          bg='#ff0000', cursor='hand2', activebackground='#3047ff', fg='white')
        self.can.place(x=105, y=549)
        self.add = Button(self.sidebar_frame, text='Allow', font=("yu gothic ui", 13, "bold"), width=20,
                          bd=0,
                          bg='#228B22', cursor='hand2', activebackground='#3047ff', fg='white')
        self.add.place(x=635, y=549)



def page():
    window = Tk()
    Startpage(window)
    window.mainloop()




if __name__ == '__main__':
    page()