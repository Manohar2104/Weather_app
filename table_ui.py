import tkinter as tk
from tkinter import *
def table(d1,d2):
    param = ["Name","Temperature", "Pressure", "Humidity","Wspeed","Description","Max_temperature","Min_temperature","Sunrise","Sunset"]
    l1 = []
    for i in param:
        l = []
        l = [i, d1[i], d2[i]]
        l1.append(l)
    totalrow=len(l1)
    totalcolumns=len(l1[0])
    root = Tk()
    #t = Table(root)


    for i in range(totalrow):
        for j in range(totalcolumns):
            e = Entry(root, width=20, fg='blue',
                           font=('Arial', 16, 'bold'))

            e.grid(row=i, column=j)
            e.insert(END, l1[i][j])
    #root.mainloop()



#table({"Temperature":200,"Pressure":1000,"Humidity":40},{"Temperature":100,"Pressure":2000,"Humidity":60})