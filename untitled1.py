from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Private Login Page")
root.configure(background = "light grey")

label_name = Label(root, text = "Name")
label_name.place(relx = 0.35, rely = 0.2, anchor = CENTER)

name_entry = Entry(root)
name_entry.place(relx = 0.65, rely = 0.2, anchor = CENTER)

label_password = Label(root, text = "Password")
label_password.place(relx = 0.35, rely = 0.3, anchor = CENTER)

password_entry = Entry(root)
password_entry.place(relx = 0.65, rely = 0.3, anchor = CENTER)

label_captcha = Label(root, text = "Captcha")
label_captcha.place(relx = 0.35, rely = 0.4, anchor = CENTER)

captcha_entry = Entry(root)
captcha_entry.place(relx = 0.65, rely = 0.4, anchor = CENTER)

class login():
    def __init__(self):
        print("This is a class login page")
        
    def update(self):
        self.__name = name_entry.get()
        print(self.__name)
        name1 = name_entry.get
        
        
        self.__password = password_entry.get()
        print(self.__password)
        password1 = password_entry.get
        
        self.__captcha = captcha_entry.get()
        print(self.__captcha)
        captcha1 = captcha_entry.get()
        
    def showProfile(self):
        copy_name = Label(root, text = "Name: " +str(name1))
        copy_name.place(relx = 0.5, rely = 0.7, anchor = CENTER)
        
        copy_password = Label(root, text = "Password: " + str(password1))
        copy_password.place(relx = 0.5, rely = 0.8)
        
        copy_captcha = Label(root, text = "Captcha: " + str(captcha1))
        copy_captcha.place(relx = 0.5, rely = 0.9, anchor = CENTER)
        

low = login()

btn_update = Button(root, text = "Update Login Details", padx = 20, pady = 10, command = low.update)
btn_update.place(relx = 0.2, rely = 0.6, anchor = CENTER)

btn_showProfile = Button(root, text = "Show Profile", padx = 20, pady = 10, command = low.showProfile)
btn_showProfile.place(relx = 0.7, rely = 0.6, anchor = CENTER)

root.mainloop()