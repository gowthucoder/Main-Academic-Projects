from tkinter import *
import tkinter.font as f
from tkinter import messagebox as m
import mysql.connector


mydb = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password='',
    database='college'
) 

mycursor = mydb.cursor()
a=Tk()
a.title('STUDENTS RECORD')
a.config(bg="#0373fc")
a.geometry("900x600")
t=Text(a,width = 50,height=50,border=3,bg='yellow')
t.pack(side="right")
f_1 = f.Font(family= 'ARIAL' ,size=26,weight='bold')
f_2 = f.Font(family= "Arial" ,size=16,weight='bold')
lbl_head = Label(a,text='STUDENTS RECORD' ,fg='white',bg='#0373fc')
lbl_head.pack()
lbl_head['font'] = f_1
lbl_1 = Label(a,text='Roll No',fg='yellow',bg='#0373fc',font=('Arial',20)).place(x=50,y=100)
lbl_2 = Label(a,text='Name',fg='yellow',bg='#0373fc',font=('Arial',20)).place(x=50,y=150)
lbl_3 = Label(a,text='Age',fg='yellow',bg='#0373fc',font=("Arial",20)).place(x=50,y=200)
lbl_4 = Label(a,text='City',fg='yellow',bg='#0373fc',font=("Arial",20)).place(x=50,y=250)
en_1 = Entry(a,border=2,font=("Arial",18),width=15)
en_2 = Entry(a,border=2,font=("Arial",18),width=15)
en_3 = Entry(a,border=2,font=("Arial",18),width=15)
en_4 = Entry(a,border=2,font=("Arial",18),width=15)
en_1.place(x=150,y=105)
en_2.place(x=150,y=155)
en_3.place(x=150,y=205)
en_4.place(x=150,y=255)
global stu
stu=[]

def find():
    global stu
    le = len(stu)
    idno = Entry.get(en_1)
    mycursor.execute('select * from where idno = {}'.format(idno))
    for i in mycursor:
        t.insert(INSERT,i) 
        clear() 

def delete():
    global stu
    idno = Entry.get(en_1)
    mycursor.execute("delete from student where idno = {}".format(idno) )
    mydb.commit()
    li = len(stu)
    for i in range(li):
     if stu[i][0] == idno:
        stu.pop(i)
        m.showinfo('Deleted',f'{"rollno"} Deleted')
        break
    clear()


def show():
    mycursor.execute('select * from student')
    res=mycursor.fetchall()
    for i in res:
        print(i)
        t.insert(INSERT,i)
        t.insert(INSERT,"\n")
    clear()

def clear():
   en_1.delete(0,END)
   en_2.delete(0,END)
   en_3.delete(0,END)
   en_4.delete(0,END)
def process():
   idno = Entry.get(en_1)
   name = Entry.get(en_2)
   age = Entry.get(en_3)
   city = Entry.get(en_4)
   rec=[idno,name,age,city]
   stu.append(rec)
   print(stu)
   print("\n")
   t.insert(INSERT,stu)
   sql='INSERT INTO student(no,name,age,city) values(%s,%s,%s)'
   val=(idno,name,age,city)
   mycursor.execute(sql,val)
   mydb.commit()
   clear()


btn_sub = Button(a,text='Submit',activeforeground='#34c6eb',activebackground='white',bg='#eb9e34',command=process)
btn_sub.place(x=50,y=330)
btn_sub['font'] = f_2
btn_sub = Button(a,text='Find',activeforeground='#34c6eb',activebackground='white',bg='#eb9e34',command=find,width=6)
btn_sub.place(x=140,y=330)
btn_sub['font'] = f_2
btn_sub = Button(a,text='Delete',activeforeground='#34c6eb',activebackground='red',bg='#eb9e34',command=delete,width=6)
btn_sub.place(x=228,y=330)
btn_sub['font'] = f_2
btn_sub = Button(a,text='Show',activeforeground='#34c6eb',activebackground='white',bg='#eb9e34',command=show,width=6)
btn_sub.place(x=315,y=330)
btn_sub['font'] = f_2
def clr():
   t.delete("1.0","end")
btn_sub = Button(a,text='Clear',activeforeground='#34c6eb',activebackground='yellow',bg='#eb9e34',command=clear,width=6)
btn_sub.place(x=403,y=330)
btn_sub['font'] = f_2
a.mainloop()








