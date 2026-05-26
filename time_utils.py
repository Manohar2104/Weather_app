import datetime
def unix_to_gmt(time_in_unix):
    gmt_str=datetime.datetime.fromtimestamp(time_in_unix).strftime('%Y-%m-%d %H:%M:%S')
    return gmt_str
