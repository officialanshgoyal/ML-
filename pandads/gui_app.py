# GUI - Graphical User Interface

# Libraries
############################
# 1. Tkinter
# 2. PyQt
# 3. Turtle

from lzma import FILTER_LZMA2
from symbol import term
import tkinter as ttk
from unittest import result
app = ttk.Tk()
app.title('My App')
app.geometry('1000x800')

msg = ttk.Variable(app)
print(msg.get())
msg.set('Empty')
print(msg.get())

ttk.Label(app,text= 'Asimple Text Lable').place(x=10,y=20)
ttk.Label(app,textvariable=msg, font=('Arial',25)).place(x=30,y=150)
ttk.Label(app,text='Ansh Goyal').place(x=50,y=60)
def abc():
    print('Wow')
    msg.set('jo tera mann kare')

ttk.Button(app, text='Isko Click Kar do', command=abc, font=('Arial',25)).place(x=70,y=40)
ttk.Button(app,text='ye wala bhi hai', font=('Arial',15) ,command=lambda:msg.set('pata nahi ')).place(x=90,y=100)



f1 = ttk.Variable(app)
f1.set('0')
f2 = ttk.Variable(app)
f2.set('0')
result= ttk.Variable(app)

ttk.Entry(app,textvariable=f1, font=('Arail',22)).place(x=110,y=200)
ttk.Entry(app,textvariable=f2,font=('Arial',22)).place(x=170,y=200)
ttk.Label(app,text='Result').place(x=100,y=300)
ttk.Label(app,textvariable=result,font=('Arial',22)).place(x=100,y=330)
def calci(op):
    print('I will Calculate')
    result.set(eval(f1.get()+op+f2.get()))

ttk.Button(app,text='+',command=lambda:calci('+'),font=('Arial',22)).place(x=50,y=240)
ttk.Button(app,text='-',command=lambda:calci('-'),font=('Arial',22)).place(x=100,y=240)  
ttk.Button(app,text='*',command=lambda:calci('*'),font=('Arial',22)).place(x=150,y=240)
ttk.Button(app,text='/',command=lambda:calci('/'),font=('Arial',22)).place(x=200,y=240)


box = ttk.Listbox(app, height=5,fg='Red',activestyle='dotbox')
box.insert(1,'sample 1')
box.insert(2,'sample 2')
box.insert(3,'sample 3')
box.place(x=450,y=40)


def show():
    print(box.get(box.curselection()))

ttk.Button(app,text='show',command=show).place(x=450,y=250)




app.mainloop()