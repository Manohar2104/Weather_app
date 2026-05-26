from tkinter import *
from tkinter import filedialog

def savefile(onlyf,n1,now):


    file=filedialog.asksaveasfile(defaultextension='.csv',filetypes=[('Text file','.txt'),('CSV file','.csv'),('XLSX file','.xlsx')],initialfile=n1+"_"+now)

    file.write(onlyf.to_csv(sep=','))
    file.close()
