from datetime import datetime
def diffrnc(name1,name2,param,d1,d2):
    if param=="Sunrise" or param=="Sunset":
        start=str(d1[param]).replace(".",":")
        end=str(d2[param]).replace(".",":")
        start_time = datetime.strptime(start, "%H:%M")
        end_time = datetime.strptime(end, "%H:%M")
        difference = end_time - start_time
        seconds = difference.total_seconds()
        hours_diff=seconds/3600
        return str(round(hours_diff,2))
    else:
        return str(abs(round(d1[param]-d2[param],2)))

