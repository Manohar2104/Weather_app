from tkinter import*
from weather_ui import*
from three_day_ui import*
w2=Tk()
w2.title("weather app")
w2.geometry('706x435')
def close():
	w2.quit()
b1=Button(w2,text="CURRENT WEATHER",command=rev)
b2=Button(w2,text="3 DAYS WEATHER",command=t_day)
b1.pack()
b2.pack()
w2.mainloop()
