import time


"""
    

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

"""

def fact(n):
    
    if n == 1:
        return n
    return n * fact(n-1)


def main():
    start_time = time.time()
    print(f"{sum([int(x) for x in str(fact(100))])}\nVreme: {time.time()-start_time} sekundi")
    
    
if __name__ == "__main__":
    main()