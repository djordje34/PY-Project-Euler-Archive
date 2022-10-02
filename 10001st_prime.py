def getNth(n):
    """This function returns Nth prime number.
    If a number is divisible by every prime number previously added to the primes list, then it is a prime.
    \nSieve of Eratosthenes is the preferred algorithm when working with prime numbers (or at least personally), but the problem requires specifically 10001st prime, so this method was used.

    Args:
        n (int): Integer representing index of desired prime number in primes list

    Returns:
        int: Integer at the n-th position in the primes list
    """
    p = [2]
    chck = 3
    while len(p)<n:
        if(len(p)%1000==0):
            print(f"CURRENT PRIME GEN(x1000)->{len(p)//1000}")
        if all(chck % el != 0 for el in p):
            p.append(chck)
        chck += 2
    return p[-1]

def main():

    print(getNth(10001))
    
    
if __name__=='__main__':
    main()