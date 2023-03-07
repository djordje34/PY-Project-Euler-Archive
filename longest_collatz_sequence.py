import time

from numpy import argmax


"""


The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), 
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""

def getSimplerCollatzTerms(n):
    ctr = 1
    while(n-1):
        ctr+=1
        n= n/2 if not n%2 else 3*n+1
        
    return ctr

def getCollatzTerms(n):
    terms = [n]
    while (n-1):
        
        n= n/2 if not n%2 else 3*n+1
        n=int(n)
        terms.append(n)
    return len(terms),terms

def main():
    start_time = time.time()
    #print(getCollatzTerms(13),((c_exec:=time.time())-start_time))
    #print(getSimplerCollatzTerms(13),time.time()-c_exec)
    l = (range(100001,1000001,2)[::-1])
    nl = list(map(getSimplerCollatzTerms,l))
    print(f"{l[int(argmax(nl))]}\nVreme: {time.time()-start_time} sekundi")

        
if __name__ == "__main__":
    main()