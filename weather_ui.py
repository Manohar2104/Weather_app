from tkinter import *
from tkinter import messagebox
from current_weather_api import *
from test import *
import pandas as pd
from datetime import datetime
#from tabular_form import tabular
import table_formatter as tf
from plot_utils import compare_param
from file_export import savefile
from table_ui import table
from param_difference import diffrnc
from unit_utils import get_unit
from voice_output import to_voice
def rev():
    w = Toplevel()
    w.title("WEATHERw APP")
    w.geometry('706x435')
    cv = Canvas(w, width=706, height=435)
    #Im = PhotoImage(master=cv, file="w.gif")
    i = cv.create_image(0, 0, anchor="nw")
    cv.pack(fill="both", anchor="center", expand=True)
    l = ["select the parameter", "Temperature", "Pressure", "Humidity", "wspeed", "Description", "Max_temperature",
         "Min_temperature", "Sunrise", "Sunset"]
    e = Entry(w, width=20, borderwidth=5)
    E = Entry(w, width=20, borderwidth=5)
    E1 = cv.create_window(270, 130, anchor="nw", window=E)
    e1 = cv.create_window(270, 170, anchor="nw", window=e)
    c = StringVar()
    c.set(l[0])
    d = OptionMenu(w, c, *l)
    d1 = cv.create_window(265, 220, anchor="nw", window=d)

    def submit():
        if c.get() != "select the parameter" and str(e.get()) != "" and str(E.get()) != "":
            new_w = Toplevel(w)
            new_w.title("WEATHER APP")
            new_w.geometry('706x435')
            dict_city1 = weather_info(e.get())
            dict_city2 = weather_info(E.get())

            """subframe = Frame(new_w, background="blue")
            subframe.pack(expand=True, fill=BOTH, side=LEFT)
            message = Label(subframe, text=tf.tabular(e.get(),dict_city1))
            message.place(relx=0.5, rely=0.5, anchor=CENTER)
            subframe2 = Frame(new_w, background="red")
            subframe2.pack(expand=True, fill=BOTH, side=LEFT)
            message = Label(subframe2, text=tf.tabular(E.get(),dict_city2))
            message.place(relx=0.5, rely=0.5, anchor=CENTER)"""
            difference = diffrnc(e.get(), E.get(), c.get(), dict_city1, dict_city2)
            unit = get_unit(c.get())
            statement = "The difference in " + c.get() + " of " + e.get() + " and " + E.get() + " is " + difference + unit

            text=Text(new_w)
            text.pack(fill='both',anchor="center",expand=True)
            text.insert(END,statement)
            to_voice(statement)

            table(dict_city1,dict_city2)

            city_list = [dict_city1["Name"], dict_city2["Name"]]
            param_list = [dict_city1[c.get()], dict_city2[c.get()]]
            compare_param(city_list, param_list,c.get())

            list1 = [dict_city1, dict_city2]
            df = pd.DataFrame(list1)

            current_time = datetime.now()
            dt_string = str(current_time.strftime("%d-%m-%Y %H_%M_%S"))
            savefile(df, e.get() + "_" + E.get(), dt_string)
            #new_w.mainloop()
        else:
            t = "please fill in the details "
            messagebox.showwarning("ERROR*", t)

    b = Button(w, text="NEXT", activeforeground="Yellow", activebackground="Blue", command=submit)
    b1 = cv.create_window(345, 400, anchor="nw", window=b)
    l = Label(cv, text="Weather app", anchor="nw", font=("Times", 25))
    l.pack()
   # w.mainloop()
