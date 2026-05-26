
import pandas as pd
from tabulate import tabulate

def tabular(name,dict1):

    """df1 = pd.DataFrame(dict1.values(),
                       index=["Name", "Temperature", "Pressure", "Humidity", "Windspeed", "Description",
                              "Max Temperature", "Min_Temperature", "Sunrise", "Sunset"])

    return tabulate(df1, headers='keys', tablefmt='psql')"""
    statement=(str(name).upper()+"\n"+"\n"+"\n"+"Temperature   "+str(dict1["Temperature"])
               +"\n"+"Pressure   "+str(dict1["Pressure"])+
               "\n"+"Humidity   "+str(dict1["Humidity"])+
               "\n"+"Wspeed   "+str(dict1["Wspeed"])+
               "\n"+"Description   "+str(dict1["Description"])
                +"\n"+"Max Temperature   "+str(dict1["Max_temperature"])
               +"\n"+"Min Temperature   "+str(dict1["Min_temperature"])
               +"\n"+"Sunrise   "+str(dict1["Sunrise"])
               +"\n"+"Sunset   "+str(dict1["Sunset"]))
    return statement




#dict1 = {"Name": "Pranav", "Temp": 300, "Pressure": 1000}



