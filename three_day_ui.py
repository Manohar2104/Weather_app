from tkinter import *
from tkinter import messagebox
from three_day_data import *
from matplotlib.animation import FuncAnimation
from graph_animation import give
from graph_animation import animate
import matplotlib.pyplot as plt
from voice_output import to_voice
from param_summary import avg
from datetime import datetime
from unit_utils import get_unit
import pandas as pd
import file_export  # assuming this exists

def t_day():
    w = Toplevel()
    w.title("WEATHER APP")
    w.geometry('706x435')

    l = ["select the parameter", "Temperature", "Pressure", "Humidity", "Wspeed",
         "Description", "Max_temperature", "Min_temperature", "Sunrise", "Sunset"]

    # City Input
    Label(w, text="Enter City:", font=("Arial", 14)).place(x=260, y=120)
    e = Entry(w, width=20, borderwidth=5)
    e.place(x=260, y=150)

    # Parameter Dropdown
    c = StringVar()
    c.set(l[0])
    d = OptionMenu(w, c, *l)
    d.place(x=260, y=200)

    def submit():
        if c.get() != "select the parameter" and str(e.get()).strip() != "":
            new_w = Toplevel(w)
            new_w.title("WEATHER APP")
            new_w.geometry('706x435')

            # fetch dictionary
            dict = threedaywthr(str(e.get()), c.get())

            # prepare graph data
            give(dict, c.get())

            font1 = {'family': 'serif', 'color': 'blue', 'size': 30}
            font2 = {'family': 'serif', 'color': 'darkred', 'size': 30}

            fig = plt.figure(figsize=(30, 8))
            ani = FuncAnimation(fig, animate, frames=24, interval=200, repeat=False)
            plt.grid()
            plt.ylabel(c.get(), fontdict=font1)
            plt.title("VARIATION OF " + str(c.get()).upper() + " IN " + str(e.get()).upper() +
                      " FOR THREE DAYS", fontdict=font2)
            plt.show()

            param_list = dict[c.get()]
            unit = get_unit(c.get())
            statement = "The average of " + c.get() + " in " + e.get() + " is " + \
                        str(round(avg(param_list), 2)) + unit

            text = Text(new_w)
            text.pack(fill="both", anchor="center", expand=True)
            text.insert(END, statement)

            to_voice(statement)

            # saving file
            df = pd.DataFrame(dict)
            current_time = datetime.now()
            dt_string = str(current_time.strftime("%d-%m-%Y %H_%M_%S"))
            file_export.savefile(df, e.get(), dt_string)

            new_w.mainloop()

        else:
            messagebox.showwarning("ERROR*", "Please fill in all the details.")

    b = Button(w, text="NEXT", fg="yellow", bg="blue", command=submit)
    b.place(x=330, y=300)

    w.mainloop()
