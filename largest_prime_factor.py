from math import ceil, sqrt
import time

def checkFactor(n):
    maxPrime = -1

    while n % 2 == 0:
        maxPrime = 2
        n /= 2

    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            maxPrime = i
            n = n / i
    if n > 2:
        maxPrime = n
    return int(maxPrime)


def main():
    start_time = time.time()
    #print(checkFactor(600851475143))
    br=600851475143 
    print("za broj ",br)
    
    print(checkFactor(br))
    time1=time.time() - start_time
    print("--- %s seconds ---" % time1)
    
    
if __name__=="__main__":
    main()