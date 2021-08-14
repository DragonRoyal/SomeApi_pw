import time, sys
from colorama import init
from termcolor import colored
import traceback
import tracemalloc
tracemalloc.start()
# use Colorama to make Termcolor work on Windows too
init()

def np(str):
  i=0

  for letter in str:
    i=i+1
    
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.1)
  sys.stdout.write("\n")
  
def add(num):
    
    numX=num.split("+")
    results = list(map(int, numX))
    a=sum(results)
    return a    
def cArea(RAD,pi=3.1415926535):
    try:
        
        A=pi*(RAD**2)
        return A
    except Exception as e:
        message = f"An exception of type {type(e).__name__,} occurred. Arguments:\n{e.args}"
        #return message
        return colored(("Hi! seems like you got a error heres the ERROR:",message),'blue',)
def cVOL(RAD,pi=3.1415926535):
    try:
        A=4/3*pi*(RAD**3)
        return A
    except Exception as e:
        message = f"An exception of type {type(e).__name__,} occurred. Arguments:\n{e.args}"
        return colored(("Hi! seems like you got a error heres the ERROR:",message),'blue',)
def Aseries(n):
    try:
        ans=n*(n+1)/2
        return ans
    except Exception as e:
        message = f"An exception of type {type(e).__name__,} occurred. Arguments:\n{e.args}"
        return colored(("Hi! seems like you got a error heres the ERROR:",message),'blue',)
async def factorial(n):
    try:
        a=factorial(n)
        return await a
    except Exception as e:
        message = f"An exception of type {type(e).__name__,} occurred. Arguments:\n{e.args}"
        return colored(("Hi! seems like you got a error heres the ERROR:",message),'blue',)
async def cooltesta():
    b=4
    return await b
    
a=input("what circle radius,")

print(cooltesta())
    #a=num.split()

