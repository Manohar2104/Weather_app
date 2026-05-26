import requests
import json
import pandas as pd

from graph_animation import give
from graph_animation import animate
from matplotlib.animation import FuncAnimation
import file_export
import matplotlib.pyplot as plt
import numpy as np
from voice_output import to_voice
from param_summary import avg
from datetime import datetime
from unit_utils import get_unit
#from graph_5daywthr import graph_5daywthr
def threedaywthr(name,param):

        data = requests.get( "https://api.openweathermap.org/data/2.5/forecast?q="+name+"&appid=cb2a0ef956da8f73c5cd1638983366a8&cnt=24").json()
        #print(data)
        temp_list=[]
        for i in range(24):
            ele=data["list"][i]["main"]["temp"]
            temp_list.append((ele-273))
        #print(temp_list)

        press_list=[]
        for i in range(24):
            ele=data["list"][i]["main"]["pressure"]
            press_list.append(ele)
        #print(press_list)

        humid_list=[]
        for i in range(24):
            ele=data["list"][i]["main"]["humidity"]
            humid_list.append(ele)
        #print(humid_list)

        wspeed_list=[]
        for i in range(24):
            ele=data["list"][i]["wind"]["speed"]
            wspeed_list.append(ele)
        #print(wspeed_list)


        date_list=[]
        for i in range(24):
            ele=data["list"][i]["dt_txt"]
            new=ele[5:13]
            new1=str(new).replace(" ","\n")

            date_list.append(new1)
        #print(date_list)

        dict1={"Name":name, "Temperature":temp_list, "Pressure":press_list, "Humidity":humid_list, "Wspeed":wspeed_list, "DateTime":date_list}
        return dict1
        """print(dict1)
        df=pd.DataFrame(dict1)

        #print(df)
        #graph_5daywthr(dict,param,name)
        give(dict1,param)
        font1 = {'family': 'serif', 'color': 'blue', 'size': 30}
        font2 = {'family': 'serif', 'color': 'darkred', 'size': 30}
        fig=plt.figure(figsize=(30,8))
        ani=FuncAnimation(fig,animate,frames=24, interval=200,repeat=False)
        plt.grid()
        plt.ylabel(param,fontdict=font1)
        plt.title("VARIATION OF "+str(param).upper()+" IN "+str(name).upper()+" FOR THREE DAYS ",fontdict=font2)
        plt.show()


        param_list=dict1[param]
        unit=get_unit(param)
        statement="The average of "+param+" in "+name+" is "+str(round(avg(param_list),2))+unit
        print(statement)
        to_voice(statement)




        current_time = datetime.now()
        dt_string = str(current_time.strftime("%d-%m-%Y %H_%M_%S"))
        data_to_file.savefile(df,name,dt_string)"""

