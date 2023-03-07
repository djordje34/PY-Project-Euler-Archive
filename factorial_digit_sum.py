import time
def fact(n):
    
    if n == 1:
        return n
    return n * fact(n-1)


def main():
    start_time = time.time()
    print(f"{sum([int(x) for x in str(fact(100))])}\nVreme: {time.time()-start_time} sekundi")
    
    
if __name__ == "__main__":
    main()