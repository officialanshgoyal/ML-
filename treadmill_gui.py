from multiprocessing import Value
from optparse import Values
from tkinter.tix import COLUMN
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import tkinter as ttk




data=pd.read_csv('treadmil-users.csv')

app = ttk.Tk()
app.geometry('600x300')
app.title('Treadmil Users Analysis')

graphs = ttk.Variable(app)
Values = {
    'Pair Plot' : 'sns.pairplot(data = data)',
    'Jointplot': "sns.jointplot(data=data, x='{col1}',y= '{col2}')",
    'Bar Plot': "sns.barplot(data=data,x= ' {col1}','{col2}')"
}

graphs.set(Values['Pair Plot'])


y=10

for key ,value in Values.items():
    ttk.Radiobutton(app , text= key, variable=graphs ,value=value).place(x= 10, y= y)
    y += 20


## option Menu 1
col1 = ttk.Variable(app)
Values = ['Select','Product','Age','Gender']
col1.set(value=[0])
ttk.Label(app, text='Column 1').place(x=100,y=10)
ttk.OptionMenu(app, col1, *Values ).place(x = 100,y=40)







## Option Menu 3
col3 = ttk.Variable(app)
col3.set(values[0])
ttk.Label(app,text= 'column3').place





def show():
    #print(graphs.get())
    print(col1.get(),col2.get(),col3.get())
ttk.Button(app, text = 'Show', command=show).place(x=400,y=10)    





app.mainloop()