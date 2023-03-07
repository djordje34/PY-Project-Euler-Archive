import time
import math


"""

The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

"""




def main():
    start_time = time.time()
    
    print(f"{(temp:=str(sum([x**x for x in range(1,1000)])))[len(temp)-10:]}\nVreme: {time.time()-start_time} sekundi")
    
if __name__=='__main__':
    main()