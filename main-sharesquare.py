import tkinter as tk
import tkinter.font as tkFont
import psycopg2

def login():
    conn = psycopg2.connect(
        host="localhost",
        database="sharesquare",
        user="postgres",
        password="welcome1234")
    cur = conn.cursor()

    login_username = input("Please enter your username or email: ")
    login_password = input("Please enter your password: ")

    check_login = (f"SELECT name FROM public.login WHERE name = '{login_username}'")
    check_password = (f"SELECT password FROM public.login WHERE name = '{login_username}'")

    cur.execute(check_login)
    username_result = cur.fetchone()[0]
    cur.execute(check_password)
    password_result = cur.fetchone()[0]

    passwordr = password_result
    usernamer = username_result

    if login_password == passwordr and login_username == usernamer:
        print("Logged in successfully")
    else: 
        print("Login failed, wrong username or password")

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

