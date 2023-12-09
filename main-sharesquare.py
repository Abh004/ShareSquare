import psycopg2
import tkinter
from tkinter import messagebox
from tkinter.ttk import *
from PIL import ImageTk, Image

#DB Conn for login page
def loginpage():
    conn = psycopg2.connect(
        host="localhost",
        database="sharesquare1",
        user="postgres",
        password="welcome1234")
    cur = conn.cursor()

    check_login = (f"SELECT username FROM public.loginpage WHERE username = '{email_Entry.get()}'")
    check_password = (f"SELECT password FROM public.loginpage WHERE username = '{email_Entry.get()}'")

    if len(email_Entry.get())!=0 and len(pwd_Entry.get())!=0:
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
    else:
        messagebox.showinfo(title="Invalid Input",message="Please fill in all the fields!")

#DB Conn for register page
def regpage():
    conn = psycopg2.connect(
        host="localhost",
        database="sharesquare1",
        user="postgres",
        password="welcome1234")
    cur = conn.cursor()

    insert_name = (f"INSERT into public.loginpage (name,username,email,password) VALUES ('{cusn_Entry.get()}','{cemail_Entry.get()}','{cpw_Entry.get()}','{cpwd_Entry.get()}');")
    username_check = (f"SELECT username from public.loginpage where username = '{cemail_Entry.get()}';")

    cur.execute(username_check)
    username_result = cur.fetchone()

    if len(cusn_Entry.get())!=0 and len(cemail_Entry.get())!=0 and len(cpw_Entry.get())!=0 and len(cpwd_Entry.get())!=0:
        if username_result==None:
            cur.execute(insert_name)
            conn.commit()
            messagebox.showinfo(title="SignUp",message="User account has been created! Please proceed to login page!")
            swin.destroy()

        else:
            messagebox.showinfo(title='Username Invalid',message="Username already exists! Please pick a unique one!")
            swin.focus()

    else:
        messagebox.showinfo(title="Invalid Input",message="Please fill in all the fields!")   
        swin.focus()         

#Calling signup DB Command
def register():
    regpage()

#Calling login DB Command
def login():
    loginpage()

#colors
bg1='#1b1b1b'
c1='#212121'
c2='#71758F'
root = tkinter.Tk()
frame=tkinter.Frame(bg=bg1)
width = 450
height = 450
screen_width = root.winfo_screenwidth()  
screen_height = root.winfo_screenheight() 
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)

#login window
root.title("Login - Sharesquare")
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root['background']=bg1
root.resizable(0,0)

#login widgets
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

#main window
def mainwindow():
    window = tkinter.Toplevel(root)
    window.title("ShareSquare - Home")
    window['background']=bg1
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))
    window.resizable(0,0)

    #header
    cv=tkinter.Canvas(window,width=1200,height=90,bg=bg1,highlightthickness=0)
    cv.pack()    
    cv.create_rectangle(0,0,1200,90,fill=c1)
    img = ImageTk.PhotoImage(Image.open(r"resources\Image.png"))
    cv.create_image(15, 22.5,anchor=tkinter.NW, image=img)
    cv.create_text(130,40,text="ShareSquare",fill="White",font="Arial 16 bold")    
    cv.create_text(209,65,text="Friendly way to split bills with your friends!",fill="White",font="Arial 12")
    

    #buttons
    frame3=tkinter.Frame(window,bg=bg1)
    frame3.pack()
    split_bill=tkinter.Button(frame3,text="Split Bill",bg=c2,fg="White")
    split_bill.grid(row=37,column=0,columnspan=2)
    window.mainloop()
    

#signup window
def signup():
    global cusn_Entry, cemail_Entry, cpw_Entry, cpwd_Entry, swin

    swin=tkinter.Toplevel()
    swin.title("Sign Up - Sharesquare")
    swin['background']=bg1
    swin.geometry('%dx%d+%d+%d' % (width, height, x, y))
    swin.resizable(0,0)

    frame2=tkinter.Frame(swin,bg=bg1)
    frame2.pack()

    login_label2=tkinter.Label(frame2,text="Sign Up",bg=bg1,fg="White",font=("Arial",16))
    login_label2.grid(row=0,column=0,columnspan=2,pady=40)

    cusn_label=tkinter.Label(frame2,text="Name",bg=bg1,fg="White")
    cusn_Entry=tkinter.Entry(frame2)
    cusn_label.grid(row=1,column=0)
    cusn_Entry.grid(row=1,column=1)

    cemail_label=tkinter.Label(frame2,text="Username",bg=bg1,fg="White")
    cemail_Entry=tkinter.Entry(frame2)
    cemail_label.grid(row=2,column=0)
    cemail_Entry.grid(row=2,column=1)

    cpw_label=tkinter.Label(frame2,text="E-mail",bg=bg1,fg="White")
    cpw_Entry=tkinter.Entry(frame2)
    cpw_label.grid(row=3,column=0)
    cpw_Entry.grid(row=3,column=1)

    cpwd_label=tkinter.Label(frame2,text="Password",bg=bg1,fg="White")
    cpwd_Entry=tkinter.Entry(frame2,show="*")
    cpwd_label.grid(row=4,column=0)
    cpwd_Entry.grid(row=4,column=1)

    cacc=tkinter.Button(frame2,text="Sign Up",bg=c2,fg="White", command=register)
    cacc.grid(row=5,column=0,columnspan=2,pady=20)

signup_button=tkinter.Button(frame,text="Sign Up",bg=c2,fg="White",command=signup)
signup_button.grid(row=4,column=0,columnspan=2, padx=7)
frame.pack()
root.mainloop()

