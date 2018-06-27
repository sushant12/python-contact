#! /usr/bin/python3

from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Contacts")
window.geometry('300x200')

class App:
    def __init__(self, win):
        self.name_lbl = self.create_label(win, "Name")
        self.email_lbl = self.create_label(win, "Email")
        self.contact_lbl = self.create_label(win, "Contact")

        self.name_lbl.grid(row=0, sticky=E)
        self.email_lbl.grid(row=1, sticky=E)
        self.contact_lbl.grid(row=2, sticky=E)

        self.name_field = self.create_entry(win)
        self.email_field = self.create_entry(win)
        self.contact_field = self.create_entry(win)

        self.name_field.grid(row=0, column=1)
        self.email_field.grid(row=1, column=1)
        self.contact_field.grid(row=2, column=1)
        
        save_btn = Button(window, text="Save", bg="green",
                  fg="white", command=self.save_callback)
        save_btn.grid(row=3,column=1)

        self.show_contacts(win)
        
    def create_label(self, win, text):
        return Label(win, text=text, font=("Arial Bold", 10))

    def create_entry(self, win):
        return Entry(win)

    def save_callback(self):
        try:
            self.save_info()
            self.clear_entry()
            self.show_contacts()
        except:
            messagebox.showinfo("Error",  sys.exc_info()[0])
        
    def save_info(self):
        with open("db.txt", 'a+') as f:
            f.write(self.name_field.get() + ",")
            f.write(self.email_field.get() + ",")
            f.write(self.contact_field.get() + "\n")

    def clear_entry(self):
        self.name_field.delete(0, 'end')
        self.email_field.delete(0, 'end')
        self.contact_field.delete(0, 'end')

    def show_contacts(self, win=None):
        with open("db.txt", 'r') as f:
            infos = f.read().splitlines()
            rep = len(infos)+3
            for info in infos:
                Label(win, text=info).grid(row=rep, sticky=N)
                rep += 1
                

App(window)


window.mainloop()
