import datetime
import time


def convtoday(variable):
    if type(variable) == str:
        variable = int(variable)
    a = time.strftime("%m-%d-%Y", time.gmtime(variable))
    m = int(a[0:2])
    d = int(a[3:5])
    y = int(a[6:10])
    b = int(datetime.datetime(y, m, d, 0, 0).timestamp())
    return (b)
