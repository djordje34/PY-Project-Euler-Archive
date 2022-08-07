
from itertools import count
import numpy as np

def generateFib(n):
    current=[]
    for i in range(2):
        current.append(1)
    
    while(current[-1]<n):
        current.append(current[-1]+current[-2])
        
    return current
    
def main():
    fin=sum([el for el in generateFib(4000000) if el%2==0])
    print(fin)
    
    
    
if __name__=="__main__":
    main()
    