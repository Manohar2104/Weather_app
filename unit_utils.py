def get_unit(param):
    if param=="Temperature":
        return "°C"
    if param=="Pressure":
        return "hPa"
    if param=="Humidity":
        return "%"
    if param=="Wspeed":
        return "metre per seconds"
    if param=="Sunrise" or param=="Sunset":
        return "hours"
