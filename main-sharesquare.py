import psycopg2
import tkinter
from tkinter import messagebox
from tkinter.ttk import *
from PIL import ImageTk, Image

def loginpage():
    conn = psycopg2.connect(
        host="localhost",
        database="sharesquare1",
        user="postgres",
        password="welcome1234")
    cur = conn.cursor()

    check_login = (f"SELECT username FROM public.loginpage WHERE username = '{email_Entry.get()}'")
    check_password = (f"SELECT password FROM public.loginpage WHERE username = '{email_Entry.get()}'")

    cur.execute(check_login)
    username_result = cur.fetchone()[0]
    cur.execute(check_password)
    password_result = cur.fetchone()[0]

    passwordr = password_result
    usernamer = username_result

    if email_Entry.get()==username_result and pwd_Entry.get()==password_result:
        mainwindow()        
    else:
        messagebox.showinfo(title="Login",message="Incorrect Email or password")

#colors
bg1='#1b1b1b'
c1='#212121'
c2='#71758F'

root = tkinter.Tk()
frame=tkinter.Frame(bg=bg1)

#login window
root.title("Login")
root.geometry('450x450')
root['background']=bg1

#main window
def mainwindow():
    window = tkinter.Toplevel(root)
    window.title("ShareSquare")
    window['background']=bg1
    window.geometry('1200x700')
    cv=tkinter.Canvas(window,width=1200,height=700,bg=bg1,highlightthickness=0)
    cv.pack()

    #header
    cv.create_rectangle(0,0,1200,80,fill=c1)
    img = ImageTk.PhotoImage(Image.open("D:\\Compproj\\Image.png"))
    cv.create_image(15, 22.5,anchor=tkinter.NW, image=img)

    
    window.mainloop()

#login function
def login():
    loginpage()

#login widget
login_label=tkinter.Label(frame,text="Login",bg=bg1,fg="White",font=("Arial",16))
email_label=tkinter.Label(frame,text="Username",bg=bg1,fg="White")
email_Entry=tkinter.Entry(frame)
pwd_label=tkinter.Label(frame,text="Password",bg=bg1,fg="White")
pwd_Entry=tkinter.Entry(frame,show="*")
login_button=tkinter.Button(frame,text="Login",bg=c2,fg="White",command=login)

login_label.grid(row=0,column=0,columnspan=2,pady=40)
email_label.grid(row=1,column=0)
email_Entry.grid(row=1,column=1)
pwd_label.grid(row=2,column=0)
pwd_Entry.grid(row=2,column=1)
login_button.grid(row=3,column=0,columnspan=2,pady=20)

frame.pack()
root.mainloop()

"""
class App:
    def __init__(self, root):
        #setting title
        root.title("Login")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GMessage_439=tk.Message(root)
        ft = tkFont.Font(family='Times',size=23)
        GMessage_439["font"] = ft
        GMessage_439["fg"] = "#333333"
        GMessage_439["justify"] = "center"
        GMessage_439["text"] = "Sign In"
        GMessage_439.place(x=250,y=70,width=80,height=25)

        GLineEdit_622=tk.Entry(root)
        GLineEdit_622["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_622["font"] = ft
        GLineEdit_622["fg"] = "#333333"
        GLineEdit_622["justify"] = "center"
        GLineEdit_622["text"] = ""
        GLineEdit_622.place(x=170,y=210,width=251,height=53)
        GLineEdit_622["show"] = "Username"
        GLineEdit_622["invalidcommand"] = "Username"

        GLineEdit_782=tk.Entry(root)
        GLineEdit_782["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_782["font"] = ft
        GLineEdit_782["fg"] = "#333333"
        GLineEdit_782["justify"] = "center"
        GLineEdit_782["text"] = "Entry"
        GLineEdit_782.place(x=170,y=310,width=251,height=67)
        GLineEdit_782["show"] = "Password"
        GLineEdit_782["invalidcommand"] = "Password"

    def Username(self):
        print("command")

    def Password(self):
        print("command")
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
"""

