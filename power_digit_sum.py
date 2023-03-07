import time

"""

215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?

"""

def main():
    start_time = time.time()
    print(f"{sum([int(x) for x in str(2**1000)])}\nVreme: {time.time()-start_time} sekundi")
    
if __name__ == "__main__":
    
    main()