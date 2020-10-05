"""===================================================================================="""
"""================================INSTALLING REQUIRED MODULES========================="""
"""===================================================================================="""
from tkinter.constants import END, LEFT, RIGHT, Y
import pkg_resources
import os
#from functions import add_book
#req = {'mysql-connector','mysql-connector-python','captcha'}
#ins = {pkg.key for pkg in pkg_resources.working_set}
#miss = req - ins
#if miss:
    #os.system('cmd /k "@echo off & cls & pip install mysql-connector & pip install mysql-connector-python & pip install captcha & cls & exit"')

#"""===================================================================================="""
#"""================================IMPORT MODULES========================================"""
#"""===================================================================================="""
from tkinter import Tk, Toplevel, Label, Button, Entry, StringVar, Message, Frame, mainloop
from tkinter.constants import END, LEFT, RIGHT, Y
import mysql.connector
from tkinter import ttk
import getpass as gp
import time
#"""===================================================================================="""
#"""==================================COMBINE FUNCTION=================================="""
#"""======================================================5============================="""
def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func
#"""===================================================================================="""
#"""==================================INTRODUCTION======================================"""
#"""===================================================================================="""
print ('                                                                    ')
print ('                                                                    ')
print ('            #################################################       ')
print ('            #                                               #       ')
print ('            #               BOOK MANAGEMENT SYSTEM          #       ')
print ('            #                                               #       ')
print ('            #                  Version 1.0                  #       ')
print ('            #                                               #       ')
print ('            #           Created by : Class 12 SCI           #       ')
print ('            #                                               #       ')
print ('            # The unauthorized reproduction or distribution #       ')
print ('            #      of this copyrighted work is illegal.     #       ')               
print ('            #                                               #       ')
print ('            #################################################       ')
print ('                                                                    ')
print("Please Wait For 10 seconds")
while True:
	uin = 10
	try:
	    when_to_stop = abs(int(uin))
	except KeyboardInterrupt:
		break
	while when_to_stop > 0:
		m, s = divmod(when_to_stop, 60)
		h, m = divmod(m, 60)
		time_left = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
		print(time_left + "\r", end="")
		time.sleep(1)
		when_to_stop -= 1
	break
print ('                                                                    ')
print ('                                                                    ')
print ('                                                                    ')
print ('                                                                    ')
print (' !( ｀皿 ´)o/)≡≡≡≡≡≡≡>十○!( ｀皿 ´)o/)≡≡≡≡≡≡≡>十○ ○十<≡≡≡≡≡≡≡)\o(´ 皿｀ )!○十<≡≡≡≡≡≡≡)\o(´ 皿｀ )!')
print (' !( ｀皿 ´)o/)≡≡≡≡≡≡≡>十○!( ｀皿 ´)o/)≡≡≡≡≡≡≡>十○ ○十<≡≡≡≡≡≡≡)\o(´ 皿｀ )!○十<≡≡≡≡≡≡≡)\o(´ 皿｀ )!')
print (' !( ｀皿 ´)o/)≡≡≡≡≡≡≡>十○!( ｀皿 ´)o/)≡≡≡≡≡≡≡>十○ ○十<≡≡≡≡≡≡≡)\o(´ 皿｀ )!○十<≡≡≡≡≡≡≡)\o(´ 皿｀ )!')
print ('                                                                                               ')
print ('                                                                                               ')
print ('            ︻╦╤─              |---\   |------|  |------|  |  /             ─╤╦︻                       ')
print ('            ︻╦╤─              |    \  |      |  |      |  | /              ─╤╦︻                       ')
print ('            ︻╦╤─              |-----  |      |  |      |  ||               ─╤╦︻                       ')
print ('            ︻╦╤─              |    /  |      |  |      |  | \              ─╤╦︻                       ')
print ('            ︻╦╤─              |---/   |------|  |------|  |  \             ─╤╦︻                       ')
print ('                                                                                                       ')
print ('                                                                                                       ')
print ('          |\    /|  ---  |\    |  ---    -----   |----- |\    /| |----- |\    | ------                 ')
print ('          | \  / | /   \ | \   | /    \  |       |      | \  / | |      | \   |   |                    ')
print ('          |  \/  | |---| |  \  | |--- |  |  ---| |--    |  \/  | |--    |  \  |   |                    ')
print ('          |      | |   | |   \ | |    |  |     | |      |      | |      |   \ |   |                    ')
print ('          |      | |   | |    \| |    |  |-----| |----- |      | |----- |    \|   |                    ')
print ('                                                                                               ')
print ('                                                                                               ')
print (' !( ｀皿 ´)o/)≡≡≡≡≡≡≡>十○!( ｀皿 ´)o/)≡≡≡≡≡≡≡>十○ ○十<≡≡≡≡≡≡≡)\o(´ 皿｀ )!○十<≡≡≡≡≡≡≡)\o(´ 皿｀ )!')
print (' !( ｀皿 ´)o/)≡≡≡≡≡≡≡>十○!( ｀皿 ´)o/)≡≡≡≡≡≡≡>十○ ○十<≡≡≡≡≡≡≡)\o(´ 皿｀ )!○十<≡≡≡≡≡≡≡)\o(´ 皿｀ )!')
print (' !( ｀皿 ´)o/)≡≡≡≡≡≡≡>十○!( ｀皿 ´)o/)≡≡≡≡≡≡≡>十○ ○十<≡≡≡≡≡≡≡)\o(´ 皿｀ )!○十<≡≡≡≡≡≡≡)\o(´ 皿｀ )!')
print ('                                                                    ')
print ('                                                                    ')
print ('                                                                    ')
print ('                                                                    ')
#print ('                                                                    ')
#print ('                                                                    ')
#print ('                                                                   ')
#"""===================================================================================="""
#"""=====================================SQL CONNECTION================================="""
#"""===================================================================================="""
print("MySQL Connection")
hname = input("Enter HostName: ")
uname = input("Enter UserName: ")
p = gp.getpass(prompt="Enter Your MySQL password: ",stream = None)
mydb = mysql.connector.connect(host=hname,user=uname,passwd=p,auth_plugin='caching_sha2_password')
try:
    mydb
    print("Connection Succeeded")
except:
    pass
cur=mydb.cursor()
def connect():
    cur.execute("CREATE DATABASE tetrahedron")
    cur.execute("USE tetrahedron")
    cur.execute("CREATE TABLE BOOK(ID int(255) auto_increment,PRIMARY KEY(ID),Book_Name varchar(100),Author varchar(100),ISBN varchar(100),Year varchar(100))")
try:
    connect()
except:
    cur.execute("USE tetrahedron")
    pass

#"""===================================================================================="""
#"""==================================EXIT=============================================="""
#"""===================================================================================="""
def logout():
    window.destroy()
#"""===================================================================================="""
#"""==================================RESET============================================="""
#"""===================================================================================="""
def reset():
    rest = Toplevel(window)
    rest.geometry("1100x600")
    Label(rest, text="").pack()
    text = Label(rest,text = "!!!ARE YOU SURE?? ALL DATA WILL BE PERMANANTLY DELETED!!!",fg ="red")
    text.pack()
    text.config(font = ("Arial",20))
    Label(rest,text="").pack()
    Label(rest,text="Please type CONFIRM in the box to verify!!!").pack()
    Label(rest,text="").pack()
    verify = StringVar()
    conf = Entry(rest, textvariable = verify)
    conf.pack()
    def accessg():
        rest.destroy()
        insert = "DROP DATABASE tetrahedron"
        cur.execute(insert)
        mydb.commit()
        master=Tk()
        master.geometry("150x150")
        w=Message(master,text="Database Deleted Successfully........Restart Program!!!")
        w.pack()
        mainloop()
    def ver():
        getsh = verify.get()
        if getsh == "CONFIRM":
            accessg()
        else:
            master=Tk()
            master.geometry("150x150")
            w=Label(master,text="Verification Failed!!!")
            w.pack()
    b = Button(rest,text=" DELETE  ",height = 2,command=ver)
    b.pack()
#"""===================================================================================="""
#"""===========================REMOVE RECORDS==========================================="""
#"""===================================================================================="""
def remove():
    removebook=Toplevel(window)
    removebook.title("REMOVE")
    removebook.geometry("400x200")
    Label(removebook, text="").pack()
    Label(removebook, text="Enter ID of The Book to be Deleted: ").pack()
    Label(removebook, text="").pack()
    delete=StringVar()
    e1 = Entry(removebook, textvariable=delete)
    e1.pack()
    Label(removebook, text="").pack()
    def lang():
        l = (delete.get(),)
        insert = "DELETE FROM BOOK WHERE ID = %s"
        cur.execute(insert,l)
        mydb.commit()
        removebook.destroy()
        master= Tk()
        win = Message(master,text="Records Have been deleted successfully")
        win.pack()
        mainloop()
    Button(removebook,text="DELETE",command=lang).pack()
    Label(removebook, text="").pack()
#"""===================================================================================="""
#"""=============================DISPLAY ALL RECORDS===================================="""
#"""===================================================================================="""
def view():
    editbook = Tk()
    editbook.title("VIEW")
    editbook.geometry("1100x400")
    Label(editbook, text="")
    frm = Frame(editbook)
    frm.pack(side=LEFT, padx=20)
    tv = ttk.Treeview(frm,column=(1,2,3,4,5), show="headings",height="15",selectmode='browse')
    scr = ttk.Scrollbar(frm,orient="vertical",command=tv.yview)
    scr.pack(side=RIGHT ,fill=Y)
    tv.heading(1, text="ID")
    tv.heading(2, text="BookName")
    tv.heading(3, text="Author")
    tv.heading(4, text="ISBN")
    tv.heading(5, text="Year")
    insert = "SELECT * FROM book"
    cur.execute(insert)
    rows=cur.fetchall()
    for i in rows:
        tv.insert('', 'end',values=i)
    tv.pack()
    tv.configure(yscrollcommand=scr.set)
    editbook.mainloop()
#"""===================================================================================="""
#"""=======================================UPDATE BOOK=================================="""
#"""===================================================================================="""
def update():
    updatebook = Toplevel(window)
    updatebook.title("Update Book")
    updatebook.geometry("400x100")
    Label(updatebook, text = "Edit Book Details Using ID: ").pack()
    Label(updatebook, text="").pack()
    search= StringVar()
    edit = Entry(updatebook, textvariable=search)
    edit.pack()
    Label(updatebook, text="").pack()
    def edit1():
        editbook = Toplevel(updatebook)
        editbook.title("EDIT")
        editbook.geometry("450x200")
        Label(editbook, text="EDIT RECORD").pack()
        Label(editbook, text="").pack()
        Label(editbook,text="Enter Book Name: ").pack()
        name = StringVar()
        author = StringVar()
        year = StringVar()
        e1 = Entry(editbook,textvariable = name)
        e1.pack()
        Label(editbook, text="").pack
        Label(editbook, text="Enter Author's Name: ").pack()
        e2 = Entry(editbook, textvariable=author)
        e2.pack()
        Label(editbook, text="").pack
        Label(editbook, text="Enter Year: ").pack()
        e3 = Entry(editbook, textvariable=year)
        e3.pack()
        def exe():
            l = (name.get(),author.get(),year.get(),search.get())
            insert = "UPDATE BOOK SET BOOK_NAME = %s,AUTHOR = %s,YEAR = %s WHERE ID = %s"
            cur.execute(insert,l)
            mydb.commit()
        def destroy():
            editbook.destroy()
            updatebook.destroy()
            master=Tk()
            w=Message(master,text="Records Have Been Updated!!!")
            w.pack()
            mainloop()
        Label(editbook, text="").pack()
        b4 = Button(editbook,text="UPDATE",command=combine_funcs(exe,destroy))
        b4.pack()
        editbook.mainloop()
    Button(updatebook,text="Edit",command=edit1).pack()
    Label(updatebook,text="").pack()
    updatebook.mainloop()
        
#"""===================================================================================="""
#"""===================================ADD BOOK========================================="""
#"""===================================================================================="""
def add():
    addbook = Toplevel(window)
    addbook.title("Add Book")
    addbook.geometry("300x360")
    Label(addbook,text = "Please Enter Book Details: ").pack()
    Label(addbook,text="").pack()
    name=StringVar()
    author=StringVar()
    isbn=StringVar()
    year=StringVar()
    Label(addbook,text="Name Of The Book: ").pack()
    a = Entry(addbook,textvariable=name)
    a.pack()
    Label(addbook,text="").pack()
    Label(addbook,text="Author: ").pack()
    b = Entry(addbook,textvariable=author)
    b.pack()
    Label(addbook,text="").pack()
    Label(addbook,text="ISBN:").pack()
    c = Entry(addbook,textvariable=isbn)
    c.pack()
    Label(addbook,text="").pack()
    Label(addbook,text="Year Of Publishment:").pack()
    d = Entry(addbook,textvariable=year)
    d.pack()
    Label(addbook,text="").pack()
    def submit():
        name1 = name.get()
        author1=author.get()
        year1=year.get()
        isbn1 =isbn.get()
        l = (name1,author1,isbn1,year1)
        insert="INSERT INTO BOOK (Book_Name,Author,ISBN,Year) VALUES(%s, %s, %s, %s)"
        cur.execute(insert,l)
        mydb.commit()
    def clear():
        a.delete(0,END)
        b.delete(0,END)
        c.delete(0,END)
        d.delete(0,END)
    def adddestroy():
        addbook.destroy()
    Button(addbook,text="ADD BOOK",command=combine_funcs(submit,clear)).pack()
    Label(addbook,text="").pack()
    Button(addbook,text="EXIT",command=adddestroy).pack()
    Label(addbook,text="").pack()
    addbook.mainloop()
#"""===================================================================================="""
#"""==============================MANAGEMENT BUTTONS===================================="""
#"""===================================================================================="""
def button():
    b1 = Button(window, text="Add Book",width=70,height=5,command=add).pack()
    Label(window, text="").pack()
    b2 = Button(window, text="Update Book",width=70,height = 5,command=update).pack()
    Label(window, text="").pack()
    b3 = Button(window, text="Remove Book",width=70,height = 5,command=remove).pack()
    Label(window, text="").pack()
    b4 = Button(window, text="View Book",width=70,height = 5,command=view).pack()
    Label(window, text="").pack()
    b5 = Button(window, text="Exit",width=70,height= 5,command=logout).pack()
    b = Button(window,text="Reset",command=reset)
    b.pack()
    Label(window, text="").pack()
    window.mainloop()
#"""===================================================================================="""
#"""=====================================MAIN WINDOW===================================="""
#"""===================================================================================="""
window = Tk()
window.title("Book Management")
window.geometry("650x650")
title = Label(window,text= "MANAGE BOOK")
title.pack()
title.config(font=("Arial", 50))
Label(window, text="").pack()
Label(window, text="").pack()
button()