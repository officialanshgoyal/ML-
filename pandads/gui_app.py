# GUI - Graphical User Interface

# Libraries
############################
# 1. Tkinter
# 2. PyQt
# 3. Turtle

import tkinter as ttk

app = ttk.Tk()
app.title('My App')
app.geometry('600x400')

ttk.Label(app,text= 'A simple Text Lable').place(x=80,y=100)
ttk.Label(app,text='Ansh Goyal').place(x=60,y=60)
app.mainloop()