
# < Importing tkinter and sqlite3 for GUI and database respectively > 
from cgitb import text
import tkinter
from tkinter import ttk
from tkinter import *
import sqlite3
from sqlite3 import *
from tkinter import font
from turtle import width
from unicodedata import name





# Defining Functions:

#Defining Add Contact Function

def addcontact():
    firstname = entryFirstName.get()
    lastname = entryLastName.get()
    email = entryEmail.get()
    phone = entryPhone.get()
    address = entryAddress.get()

    #create database connection
    conn = sqlite3.connect('contactdatabase.db')
    cur = conn.cursor()

    # Insert data
    cur.execute("INSERT INTO Contacts ('First_Name' ,'Last_Name' ,'Email' ,'Phone' ,'Address') values (?,?,?,?,?)" ,(firstname,lastname,email,phone,address))

    # Commit Connection

    conn.commit()
    conn.close()

    # Update Table immediately
    
    conn = sqlite3.connect('contactdatabase.db')
    cur = conn.cursor()
    select = cur.execute("SELECT * FROM Contacts order by ID desc")
    select = list(select)
    treetable.insert('' , END , values = select[0])
    conn.close()


def deletecontact():
    idSelect = treetable.item(treetable.selection())['values'][0]
    conn = sqlite3.connect("contactdatabase.db")
    cur = conn.cursor()
    delete = cur.execute("delete from Contacts where ID = {}".format(idSelect))
    conn.commit()
    treetable.delete(treetable.selection())


def SEarch(event):
    for x in treetable.get_children():
        treetable.delete(x)
    fname = entrySearch.get()
    conn = sqlite3.connect('contactdatabase.db')
    cur = conn.cursor()
    select = cur.execute("select * from Contacts where First_Name = (?)", (fname,))
    conn.commit()
    for row in select:
        treetable.insert('' , END , values = row)
    conn.close()

def Reset():
    FNM.set('')
    LNM.set('')
    EML.set('')
    PHN.set('')
    ADR.set('')




# < Creating a Container >
root = tkinter.Tk()    # < main function for tkinter GUI >
root.geometry('850x500') # < total size of the container >
root.config(bg = 'darkgreen') # < color of the container >
root.resizable(0,0) # < not resizable on any directions >
root.title('Project - AddressBook') # < Title for the project >


#Assigning string variables ((for textvariables) used for Reset command )

FNM = StringVar()
LNM  = StringVar()
EML = StringVar()
PHN = StringVar()
ADR = StringVar()



# Creating Label and Entry boxes inside container(box)

lbTitle = Label(root, text = "ADDRESS BOOK", font=("Arial", 25), bg="darkblue", fg="white", bd="5").place(x=1, y=1, width=848)

lbSearch = Label(root, text = "Search", font=("Arial", 15), bg="darkblue", fg="white", bd="1",width=10).place(x=645, y=65)
entrySearch = Entry (root,font=("Arial",14))
entrySearch.bind("<Return>" , SEarch)
entrySearch.place(x=545, y=105, width=295, height=30)


lbFirstName = Label(root, text = "First Name", font=("Arial", 20), bg="darkblue", fg="white", bd="1", width=12).place(x=10,y=75)
entryFirstName = Entry (root,bd="3", font=("Arial",16), textvariable = FNM)
entryFirstName.place(x=210, y=75, width=300, height=35)

lbLastName = Label(root, text = "Last Name", font=("Arial", 20), bg="darkblue", fg="white", bd="1", width=12).place(x=10,y=115)
entryLastName = Entry (root, bd="3", font=("Arial",16), textvariable = LNM)
entryLastName.place(x=210, y=115, width=300, height=35)

lbEmail = Label(root, text = "Email", font=("Arial", 20), bg="darkblue", fg="white", bd="1", width=12).place(x=10,y=155)
entryEmail = Entry (root,bd="3", font=("Arial",16), textvariable = EML)
entryEmail.place(x=210, y=155, width=300, height=35)

lbPhone = Label(root, text = "Phone", font=("Arial", 20), bg="darkblue", fg="white", bd="1", width=12).place(x=10,y=195)
entryPhone = Entry (root,bd="3", font=("Arial",16), textvariable = PHN)
entryPhone.place(x=210, y=195, width=300, height=35)

lbAddress = Label(root, text = "Address", font=("Arial", 20), bg="darkblue", fg="white", bd="1", width=12).place(x=10,y=235)
entryAddress = Entry (root,bd="3", font=("Arial",16), textvariable = ADR)
entryAddress.place(x=210, y=235, width=300, height=35)


#Command Buttons

btAdd = Button(root, text="ADD",font=("arial",18,font.BOLD), bd="5", command = addcontact)
btAdd.place(x=555, y=160, width=130)

btModify = Button(root, text="MODIFY",font=("arial",18,font.BOLD), bd="5", command= 'modify')
btModify.place(x=555, y=230, width=130)

btReset = Button(root, text="RESET",font=("arial",18,font.BOLD), bd="5",command= Reset)
btReset.place(x=710, y=160, width=130)

btDelete = Button(root, text="DELETE",font=("arial",18,font.BOLD), bd="5",command= deletecontact)
btDelete.place(x=710, y=230, width=130)

btExit = Button(root, text="EXIT",font=("arial",25,font.BOLD), bd="10", command=quit)
btExit.place(x=710, y=300, width=130, height=190)


# Add a Side Table (Treeview)

treetable = ttk.Treeview(root, columns=(1,2,3,4,5,6), height= 5, show= "headings")
treetable.place(x=10, y=300, width= 680, height= 190)

# Adding Table headings

treetable.heading(1, text="ID")
treetable.heading(2, text="First Name")
treetable.heading(3, text="Last Name")
treetable.heading(4, text="Email")
treetable.heading(5, text="Phone")
treetable.heading(6, text="Address")


# Defining Column width

treetable.column(1, width=30)
treetable.column(2, width=80)
treetable.column(3, width=80)

treetable.column(5, width=100)
treetable.column(6, width=100)




# Displaying Datas in table

conn = sqlite3.connect('contactdatabase.db')
cur = conn.cursor()
select = cur.execute("select * from Contacts")
for row in select:
    treetable.insert('' , END , values= row)
conn.close()







root.mainloop()