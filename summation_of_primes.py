
import math
import time

def getPrimes(n):

    """Sieve of Eratosthenes algorithm for generation of prime numbers
    
    Input: 
        int: ceiling number
    Returns:
        list: list of primes 
    """
    
    is_prime = [False, False] + [True] * (n - 1)
    primes = [2]

    for j in range(4, n + 1, 2):
        is_prime[j] = False

    for i in range(3, n + 1, 2):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return primes


def main():
    start_time = time.time()
    print(sum(getPrimes(2000000)))

    print(f"Vreme: {time.time()-start_time} sekundi")

if __name__=="__main__":
    main()