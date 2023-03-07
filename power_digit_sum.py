import time

def main():
    start_time = time.time()
    print(f"{sum([int(x) for x in str(2**1000)])}\nVreme: {time.time()-start_time} sekundi")
    
if __name__ == "__main__":
    
    main()