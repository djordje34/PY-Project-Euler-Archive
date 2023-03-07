import time


"""
The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

def fibonacci():
     
    fib = [0, 1]
    i = 2
    while 1:
        fib.append(fib[i-1] + fib[i-2])
        i+=1
        if len(str(fib[len(fib)-1]))==1000:
            break;
        
    return len(fib)-1


def main():
    start_time = time.time()
    print(f"{fibonacci()}\nVreme: {time.time()-start_time} sekundi")
    
if __name__ == "__main__":
    main()