
from functools import reduce
def avg(L):
    sum=reduce(lambda x,y: int(x)+int(y),L)
    result=sum/len(L)
    return result
