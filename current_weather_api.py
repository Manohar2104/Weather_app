import requests
from time_utils import unix_to_gmt
def weather_info(name):
    data = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q=" + name + "&appid=cb2a0ef956da8f73c5cd1638983366a8").json()
    temperature = round(data["main"]["temp"] - 273)
    pressure = data["main"]["pressure"]
    humidity = data["main"]["humidity"]
    wspeed = data["wind"]["speed"]
    description = data["weather"][0]["description"]
    max_temp = data["main"]["temp_max"]
    min_temp = data["main"]["temp_min"]
    sunrise = data["sys"]["sunrise"]
    new_rise = unix_to_gmt(sunrise)
    new1_rise = float(new_rise[11:16].replace(":", "."))
    sunset = data["sys"]["sunset"]
    new_set = unix_to_gmt(sunset)
    new1_set = float(new_set[11:16].replace(":", "."))
    dict_city = {"Name": name, "Temperature": temperature, "Pressure": pressure, "Humidity": humidity, "Wspeed": wspeed,
                 "Description": description, "Max_temperature": max_temp, "Min_temperature": min_temp,
                 "Sunrise": new1_rise, "Sunset": new1_set}
    return dict_city

