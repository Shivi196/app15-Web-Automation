import tkinter as tk
from main import WebAutomation
from tkinter import messagebox

class App:

    def __init__(self,root):
        self.root = root

        self.root.title("Web Automation GUI")

        # Login Frame
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(padx=10,pady=10)

        tk.Label(self.login_frame,text="Username").grid(row=0,column=0,sticky="w")
        self.entry_username = tk.Entry(self.login_frame)
        self.entry_username.grid(row=0,column=1,sticky="ew")

        tk.Label(self.login_frame,text="Password").grid(row=1,column=0,sticky="w")
        self.entry_password = tk.Entry(self.login_frame,show="*")
        self.entry_password.grid(row=1,column=1,stick="ew")

        # Form Submission Frame
        self.form_frame = tk.Frame(self.root)
        self.form_frame.pack(padx=10,pady=10)

        tk.Label(self.form_frame,text="Full Name").grid(row=0,column=0,sticky="w")
        self.entry_full_name = tk.Entry(self.form_frame)
        self.entry_full_name.grid(row=0,column=1,sticky="ew")

        tk.Label(self.form_frame,text="Email").grid(row=1,column=0,sticky="w")
        self.entry_email = tk.Entry(self.form_frame)
        self.entry_email.grid(row=1,column=1,sticky="ew")

        tk.Label(self.form_frame,text="Current Address").grid(row=2,column=0,sticky="w")
        self.entry_ca = tk.Entry(self.form_frame)
        self.entry_ca.grid(row=2,column=1,sticky="ew")

        tk.Label(self.form_frame,text="Permanent Address").grid(row=3,column=0,sticky="w")
        self.entry_pa = tk.Entry(self.form_frame)
        self.entry_pa.grid(row=3,column=1,sticky="ew")

        # Button Frame
        self.button_frame = tk.Frame()
        self.button_frame.pack(padx=10,pady=10)

        tk.Button(self.button_frame,text="Submit",command=self.submit_button).grid(row=0,column=0,padx=0)
        tk.Button(self.button_frame,text="Close Browser",command=self.close_browser).grid(row=0,column=1,padx=0)


    def submit_button(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        full_name = self.entry_full_name.get()
        email = self.entry_email.get()
        current_address = self.entry_ca.get()
        permanent_address = self.entry_pa.get()

        self.webautomation = WebAutomation()
        self.webautomation.login(username,password)
        self.webautomation.fill_form(full_name,email,current_address,permanent_address)
        self.webautomation.download_file()

    def close_browser(self):
        self.webautomation.close()
        messagebox.showinfo("Close Browser","Data Submitted Successfully")

root = tk.Tk()
app = App(root)
root.mainloop()