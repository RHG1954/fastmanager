from tkinter import *
from tkinter import messagebox
from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox
import os
import tkinter.ttk as ttk
import sqlite3
import tkinter.messagebox as tkMessageBox

root=Tk()
root.title('FAST MANAGER V22.6')
root.geometry("850x500+300+200")
root.configure(bg="#fff")
root.resizable(False,False)


def signin():
    username=user.get()
    password=code.get()


    if username=='admin' and password=='rhg2022':
        
        
 
        
        RHG=Toplevel(root)
        RHG.geometry("1000x800")
        RHG.title("FASTMANAGER")
        RHG.config(bg="white")
        top = Frame(RHG)
        top.pack(padx = 5, pady = 5, anchor = 'nw')
        RHG.resizable(True,True)
        global tree
        global SEARCH
        global name,contact,email,rollno,branch
        SEARCH = StringVar()
        name = StringVar()
        contact = StringVar()
        email = StringVar()
        rollno = StringVar()
        branch = StringVar()
        #topview frame for heading

        #first left frame for registration from
        LFrom = Frame(RHG, width="230")
        LFrom.pack(side=LEFT, fill=Y)
    
        MidViewForm = Frame(RHG, width=50)
        MidViewForm.pack(side=RIGHT)





        def Database():
            global conn, cursor
            #creating student database
            conn = sqlite3.connect("student.db")
            cursor = conn.cursor()
            #creating STUD_REGISTRATION table
            cursor.execute(
                 "CREATE TABLE IF NOT EXISTS STUD_REGISTRATION (STU_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, STU_NAME TEXT, STU_CONTACT TEXT, STU_EMAIL TEXT, STU_ROLLNO TEXT, STU_BRANCH TEXT)")

            #function to insert data into database
        def register():
            Database()
            #getting form data
            name1=name.get()
            con1=contact.get()
            email1=email.get()
            rol1=rollno.get()
            branch1=branch.get()
            #applying empty validation
  
            if name1=='' or con1==''or email1=='' or rol1==''or branch1=='':
                tkMessageBox.showinfo("Warning","fill the empty field!!!")
            else:
                #execute query
                conn.execute('INSERT INTO STUD_REGISTRATION (STU_NAME,STU_CONTACT,STU_EMAIL,STU_ROLLNO,STU_BRANCH) \
                      VALUES (?,?,?,?,?)',(name1,con1,email1,rol1,branch1));
                conn.commit()
                tkMessageBox.showinfo("Message","Stored successfully")
                #refresh table data
                DisplayData()
                conn.close()

        def Reset():
            #clear current data from table
            tree.delete(*tree.get_children())
            #refresh table data
            DisplayData()
            #clear search text
            SEARCH.set("")
            name.set("")
            contact.set("")
            email.set("")
            rollno.set("")
            branch.set("")
        def Delete():
            #open database
            Database()
            if not tree.selection():
                tkMessageBox.showwarning("Warning","Select data to delete")
            else:
                result = tkMessageBox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                          icon="warning")
                if result == 'yes':
                     curItem = tree.focus()
                     contents = (tree.item(curItem))
                     selecteditem = contents['values']
                     tree.delete(curItem)
                     cursor=conn.execute("DELETE FROM STUD_REGISTRATION WHERE STU_ID = %d" % selecteditem[0])
                     conn.commit()
                     cursor.close()
                     conn.close()

            #function to search data
        def SearchRecord():
            #open database
            Database()
            #checking search text is empty or not
            if SEARCH.get() != "":
                #clearing current display data
                tree.delete(*tree.get_children())
                #select query with where clause
                cursor=conn.execute("SELECT * FROM STUD_REGISTRATION WHERE STU_NAME LIKE ?", ('%' + str(SEARCH.get()) + '%',))
                #fetch all matching records
                fetch = cursor.fetchall()
                #loop for displaying all records into GUI
                for data in fetch:
                    tree.insert('', 'end', values=(data))
                cursor.close()
                conn.close()
        #defining function to access data from SQLite database
        def DisplayData():
            #open database
            Database()
            #clear current data
            tree.delete(*tree.get_children())
            #select query
            cursor=conn.execute("SELECT * FROM STUD_REGISTRATION")
            #fetch all data from database
            fetch = cursor.fetchall()
            #loop for displaying all data in GUI
            for data in fetch:
                tree.insert('', 'end', values=(data))
            cursor.close()
            conn.close()




        Search_imager=PhotoImage(file="img/backr.png")
        myimage=Label(RHG,image=Search_imager)
        myimage.place(x=0,y=580)



        Search_image=PhotoImage(file="img/back.png")
        myimage=Label(RHG,image=Search_image)
        myimage.place(x=0,y=0)


        s= Entry(RHG, textvariable=SEARCH, font=('verdana', 15),bd=0,bg="gray", width=12)
        s.place(x=807,y=30)


        s=PhotoImage(file="img/s.png")
        pause=Button(RHG,image=s,bd=0,bg="#fff",command=SearchRecord)
        pause.place(x=735,y=20)

        image1=PhotoImage(file="img/1.png")
        pause=Button(RHG,image=image1,bd=0,bg="#fff",command=register)
        pause.place(x=30,y=4)

        btn_delete=PhotoImage(file="img/2.png")
        pause=Button(RHG,image=btn_delete,bd=0,bg="#fff",command=Delete)
        pause.place(x=220,y=0)



        btn_view=PhotoImage(file="img/3.png")
        pause=Button(RHG,image=btn_view,bd=0,bg="#fff",command=DisplayData)
        pause.place(x=400,y=0)





        btn_reset=PhotoImage(file="img/4.png")
        pause=Button(RHG,image=btn_reset,bd=0,bg="#fff",command=Reset)
        pause.place(x=600,y=0)





        Label(LFrom, text="Name", font=("Arial", 12)).place(x=5,y=145)
        Entry(LFrom,font=("Arial",10,"bold"),textvariable=name).place(x=75,y=150)
  
        Label(RHG, text="Prenome ", font=("Arial", 12)).place(x=5,y=200)
        Entry(RHG, font=("Arial", 10, "bold"),textvariable=contact).place(x=75,y=201)

        Label(RHG, text="phone", font=("Arial", 12)).place(x=5,y=250)
        Entry(RHG, font=("Arial", 10, "bold"),textvariable=email).place(x=75,y=250)

        Label(RHG, text="problem", font=("Arial", 12)).place(x=5,y=300)
        Entry(RHG, font=("Arial", 10, "bold"),textvariable=rollno).place(x=75,y=300)

        Label(RHG, text="N phone", font=("Arial", 12)).place(x=5,y=350)
        Entry(RHG, font=("Arial", 10, "bold"),textvariable=branch).place(x=75,y=350)




        #setting scrollbar
        scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
        scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
        tree = ttk.Treeview(MidViewForm,columns=("Student Id", "Name", "Prnome", "Phone","Problem","N Tele"),
                            selectmode="extended", height=20,yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        #setting headings for the columns
        tree.heading('Student Id', text="Student Id", anchor=W)
        tree.heading('Name', text="Name", anchor=W)
        tree.heading('Prnome', text="Prnome", anchor=W)
        tree.heading('Phone', text="Phone", anchor=W)
        tree.heading('Problem', text="Problem", anchor=W)
        tree.heading('N Tele', text="Number phone ", anchor=W)
        #setting width of the columns
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=100)
        tree.column('#2', stretch=NO, minwidth=0, width=150)
        tree.column('#3', stretch=NO, minwidth=0, width=80)
        tree.column('#4', stretch=NO, minwidth=0, width=120)
        tree.pack()
        DisplayData()




        RHG.mainloop()




























        

    elif username!='admin' and password!='rhg2022':
        messagebox.showerror("Invalid","invalid username and password")

    elif password!='rhg2022':
        messagebox.showerror("Invalid","invalid password")

    elif username!='admin':
        messagebox.showerror("Invalid","invalid username")





img = PhotoImage(file='img/logo1.png')
Label(root,image=img,bg='white').place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)


heading=Label(frame,text='sign in',fg='#57a1f8',bg='white',font=('Microsoft yeahi u light',23,'bold'))
heading.place(x=100,y=5)
############################

def on_enter(e):
     user.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')
        
user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)


###############################

def on_enter(e):
     code.delete(0, 'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')
        

def para():
    messagebox.showinfo("FASTMANAGER", "PERSONAL INFORMATION \n NAME:RYAN GRAICHI (RHG) \n AGE : 19 ANS \n\n\n NAME PROGRAME: FASTMANAGER \n DATE CREATED: 2022-07-12 \n ORIGINAL PROGRAME \n CONTACT ME \n\n\n WEBSITE https://hack-tools-shop.blogspot.com \n FB RHG OR RYANGRAICHI \n GMAIL rayanegraichi15@gmail.com \n\n Numiro: 0553827690 \n\n THANKS FOR DOWNLOADING THE PROGRAME")

def contact():
     messagebox.showinfo("FASTMANAGER"," send me This code 20020827\n\n EMAIL:rayanegraichi15@gmail.com")
code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204),
label=Label(frame,text="Don't have an account!",fg='black',bg='white',font=('Microsoft Yahei Ui LIght',9))
label.place(x=75,y=270)

sign_up= Button(frame,width=6,text='Sing up',border=0,bg="white",cursor='hand2',fg="#57a1f8",command=contact)
sign_up.place(x=215,y=270)

sign_up= Button(frame,width=6,text='INFO',border=0,bg="white",cursor='hand2',fg="#57a1f8",command=para)
sign_up.place(x=275,y=270)




root.mainloop()

