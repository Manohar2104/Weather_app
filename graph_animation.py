import matplotlib.pyplot as plt
#from matplotlib.animation import FuncAnimation
x=[]
y=[]
def give(d,p):
        global data
        data=d
        global  param
        param=p


def animate(i):

        x.append(data["DateTime"][i])
        y.append(data[param][i])
        plt.style.use('fast')
        plt.plot(x,y, marker='o', markerfacecolor='green')





