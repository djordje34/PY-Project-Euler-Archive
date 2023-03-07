import time

from numpy import argmax

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