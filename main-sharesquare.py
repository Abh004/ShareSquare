import psycopg2
import tkinter
from tkinter import messagebox
from tkinter.ttk import *
from tkinter.scrolledtext import ScrolledText
from PIL import ImageTk, Image

#DB Conn for login page
def loginpage():
    global active_user
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
            active_user = email_Entry.get()
            mainwindow()        
        else:
            messagebox.showinfo(title="Login",message="Incorrect Email or password")
    else:
        messagebox.showinfo(title="Invalid Input",message="Please fill in all the fields!")
    conn.close()

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
    conn.close() 

#DB conn for groups page
def submit():
    conn = psycopg2.connect(
        host="localhost",
        database="sharesquare1",
        user="postgres",
        password="welcome1234")
    cur = conn.cursor()

    insert_users = (f"INSERT into public.groups1 (groupname, leader, members) VALUES ('{Entry_groupname.get()}','{active_user}','{Entry_members.get()}');")

    if len(Entry_groupname.get())!=0 and len(Entry_members.get())!=0:
        cur.execute(insert_users)
        conn.commit()
        messagebox.showinfo(title='Success!',message="Group has been created!")
        window1.focus()
    else:
        messagebox.showinfo(title="Inavlid Input",message="Please fill in all the fields!")
        window1.focus()
    conn.close()

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
login_button=tkinter.Button(frame,text="Login",bg=c2,fg="White",command=loginpage)
login_label.grid(row=0,column=0,columnspan=2,pady=40)
email_label.grid(row=1,column=0)
email_Entry.grid(row=1,column=1)
pwd_label.grid(row=2,column=0)
pwd_Entry.grid(row=2,column=1)
login_button.grid(row=3,column=0,columnspan=2,pady=20)

#split bill page
#next
def next():
    #DB conn for profile page
    conn = psycopg2.connect(
        host="localhost",
        database="sharesquare1",
        user="postgres",
        password="welcome1234")
    cur = conn.cursor()

    check_groups = (f"Select groupname, members from public.groups1 where leader = ('{active_user}');")
    cur.execute(check_groups)
    result2=cur.fetchall()
    options=[]
    for i in range(len(result2)):
        options.append(result2[i][0])
    print(options)         

    def input():
        conn = psycopg2.connect(
        host="localhost",
        database="sharesquare1",
        user="postgres",
        password="welcome1234")
        cur = conn.cursor()

        check_members= (f"select members from public.groups1 where groupname = ('{menu.get()}'); ")
        cur.execute(check_members)
        result3=cur.fetchall()
        x=result3[0][0].split(",")
        d=""
        for i in range(len(x)):
            d+=str(i+1)+") "+x[i]
            d+="\n"+"\n" 

        def enter():
            conn = psycopg2.connect(
            host="localhost",
            database="sharesquare1",
            user="postgres",
            password="welcome1234")
            cur = conn.cursor()

            check_members= (f"select members from public.groups1 where groupname = ('{menu.get()}'); ")
            cur.execute(check_members)
            result3=cur.fetchall()
            x=result3[0][0].split(",")

            amount=Entry_members1.get()
            split=float(amount)/len(x)
            f=""   
            for j in range(len(x)):
                f+=str(j+1)+")"+x[j]+" - "+"₹"+str(split)
                f+="\n"+"\n" 

            if menu1.get()=="Equal Split":
                frame6.destroy()
                frame7=tkinter.Frame(window4,bg=bg1)
                frame7.pack()       
                label_profile7=tkinter.Text(frame7,bg=bg1,fg="White",height=5, width=30, font="Arial 16")
                v=Scrollbar(frame7, orient='vertical')
                v.grid(column=7, pady=(0,0),padx=(10,0))
                v.config(command=label_profile7.yview)    
                label_profile7.insert(tkinter.END, f)
                label_profile7.configure(state='disabled', yscrollcommand=v.set)
                label_profile7.grid(row=1,column=1,columnspan=6,pady=(10,0),padx=(40,90))
        
        frame5.destroy()
        frame6=tkinter.Frame(window4,bg=bg1)
        frame6.pack()
        label6=tkinter.Label(frame6,text="Members",bg=bg1,fg="White",font=("Arial 16 bold",16))
        label6.grid(row=0, column=0, columnspan=2, padx=(170,160), pady=(40,0))
        label_profile6=tkinter.Text(frame6,bg=bg1,fg="White",height=5, width=30, font="Arial 16")
        v=Scrollbar(frame6, orient='vertical')
        v.grid(column=7, pady=(0,0),padx=(10,0))
        v.config(command=label_profile6.yview)    
        label_profile6.insert(tkinter.END, d)
        label_profile6.configure(state='disabled', yscrollcommand=v.set)
        label_profile6.grid(row=1,column=1,columnspan=6,pady=(10,0),padx=(40,90))
        label7=tkinter.Label(frame6,text="Bill Amount",bg=bg1,fg="White",font=("Arial 16 bold",16))
        label7.grid(row=3, column=0, columnspan=2, padx=(170,160), pady=(40,0))
        Entry_members1=tkinter.Entry(frame6)
        Entry_members1.grid(row=3,column=0,columnspan=2, padx=(170,160), pady=(90,0))
        label8=tkinter.Label(frame6,text="₹",bg=bg1,fg="White",font=("Arial 16 bold",16))
        label8.grid(row=3, column=0, columnspan=2, padx=(20,160), pady=(90,0))
        amount_button = tkinter.Button(frame6,text = "Enter",bg=c2,fg="White", command=enter)
        amount_button.grid(row=3,column=0,columnspan=2,padx=(170,160), pady=(160,0)) 

        menu1= tkinter.StringVar()
        drop1= OptionMenu(frame6, menu1, "Equal Split","Unequal Split (by %)")
        drop1.grid(row=2,column=0,columnspan=2, padx=(170,160), pady=(10,0))   
        conn.close()
        
    window4 = tkinter.Toplevel(root)
    window4.title("ShareSquare - Split Bill")
    window4['background']=bg1
    window4.geometry('%dx%d+%d+%d' % (width, height, x, y))
    window4.resizable(0,0)

    frame5=tkinter.Frame(window4,bg=bg1)
    frame5.pack()

    menu= tkinter.StringVar()  
    #menu.set( "Equal Split" )  
    #Create a dropdown Menu
    drop= OptionMenu(frame5, menu, *options)
    drop.grid(row=0,column=0,columnspan=2, padx=(0,0), pady=(80,0))    
    button1 = tkinter.Button(frame5,text = "Enter",bg=c2,fg="White", command=input)
    button1.grid(row=1,column=0,padx=(20,0), pady=(20,0)) 
    label5=tkinter.Label(frame5,text="Choose Group",bg=bg1,fg="White",font=("Arial",16))
    label5.grid(row=0, column=0, columnspan=2, pady=(0,0))
    conn.close()
    window1.destroy()   


def splitbill():
    global Entry_groupname, Entry_members, window1

    window1 = tkinter.Toplevel(root)
    window1.title("ShareSquare - Split Bill")
    window1['background']=bg1
    window1.geometry('%dx%d+%d+%d' % (width, height, x, y))
    window1.resizable(0,0)
    
    frame4=tkinter.Frame(window1,bg=bg1)
    frame4.pack()
    label2=tkinter.Label(frame4,text="Create Group",bg=bg1,fg="White",font=("Arial",16))    
    label=tkinter.Label(frame4,text="Group Name",bg=bg1,fg="White")
    label1=tkinter.Label(frame4,text="Members",bg=bg1,fg="White")
    Entry_members=tkinter.Entry(frame4)
    Entry_groupname=tkinter.Entry(frame4)
    label2.grid(row=0,column=0,columnspan=2,pady=40)
    label.grid(row=1,column=0)
    Entry_groupname.grid(row=1,column=1)
    label1.grid(row=2,column=0)
    Entry_members.grid(row=2,column=1)
    submit_button=tkinter.Button(frame4,text="Submit",bg=c2,fg="White",command=submit)
    submit_button.grid(row=3,column=0,columnspan=2,pady=20)
    next_button=tkinter.Button(frame4,text="Next",bg=c2,fg="White",command=next)
    next_button.grid(row=5,column=0,columnspan=2,pady=20)

#your debts page
def your_debts():
    window2 = tkinter.Toplevel(root)
    window2.title("ShareSquare - Debts")
    window2['background']=bg1
    window2.geometry('%dx%d+%d+%d' % (width, height, x, y))
    window2.resizable(0,0)

#user profile page 
def profile():
    #DB conn for profile page
    conn = psycopg2.connect(
        host="localhost",
        database="sharesquare1",
        user="postgres",
        password="welcome1234")
    cur = conn.cursor()

    check_users = (f"SELECT username, name, email from public.loginpage where username = ('{active_user}');")
    check_groups = (f"Select groupname, members from public.groups1 where leader = ('{active_user}');")
    cur.execute(check_users)
    result=cur.fetchone()
    profile_uname=(result[0])
    profile_name=(result[1])
    profile_email=(result[2])  
    cur.execute(check_groups)

    result1=cur.fetchall()
    d=""
    for i in range(len(result1)):
        d+=str(i+1)+") "+result1[i][0]+" - "+result1[i][1]
        d+="\n"+"\n"
    print(d)  

    window3 = tkinter.Toplevel(root)
    window3.title("ShareSquare - Your Profile")
    window3['background']=bg1
    window3.geometry('%dx%d+%d+%d' % (width, height, x, y))
    window3.resizable(0,0)

    label_profile=tkinter.Label(window3,text="Username:",bg=bg1,fg="White", font="Arial 16 bold")
    label_profile.grid(row=0,column=0,columnspan=2,pady=(40,0),padx=(40,0))
    label_profile1=tkinter.Label(window3,text="Name:",bg=bg1,fg="White", font="Arial 16 bold")
    label_profile1.grid(row=2,column=0,columnspan=2)
    label_profile2=tkinter.Label(window3,text="E-mail:",bg=bg1,fg="White", font="Arial 16 bold")
    label_profile2.grid(row=4,column=0,columnspan=2)
    label_profile3=tkinter.Label(window3,text=profile_uname,bg=bg1,fg="White", font="Arial 16")
    label_profile3.grid(row=0,column=3,columnspan=2,pady=(40,0),padx=(40,0))
    label_profile4=tkinter.Label(window3,text=profile_name,bg=bg1,fg="White", font="Arial 16")
    label_profile4.grid(row=2,column=3,columnspan=2)
    label_profile4=tkinter.Label(window3,text=profile_email,bg=bg1,fg="White", font="Arial 16")
    label_profile4.grid(row=4,column=3,columnspan=2)
    label_profile5=tkinter.Label(window3,text="Groups:",bg=bg1,fg="White", font="Arial 16 bold")
    label_profile5.grid(row=8,column=0,columnspan=2,padx=(15,0))
        
    label_profile6=tkinter.Text(window3,bg=bg1,fg="White",height=8, width=30, font="Arial 16 bold")
    v=Scrollbar(window3, orient='vertical')
    v.grid(sticky='e',column=7, pady=(10,0))
    v.config(command=label_profile6.yview)    
    label_profile6.insert(tkinter.END, d)
    label_profile6.configure(state='disabled', yscrollcommand=v.set)
    label_profile6.grid(row=9,column=1,columnspan=6,pady=(40,0),padx=(40,90)) 
    conn.close()

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
    split_bill=tkinter.Button(frame3,text="Split your Bill",bg=c2,fg="White",command=splitbill)
    split_bill.grid(row=0,column=0, pady=70)#, padx=(240,0))
    debt_check=tkinter.Button(frame3,text="Your Debts",bg=c2,fg="White",command=your_debts)
    debt_check.grid(row=1,column=0)#, padx=(240,0))
    user_profile=tkinter.Button(frame3,text="Your Profile",bg=c2,fg="White",command=profile)
    user_profile.grid(row=2,column=0,pady=70)#, padx=(240,0))
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

    cacc=tkinter.Button(frame2,text="Sign Up",bg=c2,fg="White", command=regpage)
    cacc.grid(row=5,column=0,columnspan=2,pady=20)

signup_button=tkinter.Button(frame,text="Sign Up",bg=c2,fg="White",command=signup)
signup_button.grid(row=4,column=0,columnspan=2, padx=7)
frame.pack()
root.mainloop()

