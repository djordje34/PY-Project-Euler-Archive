from functools import reduce

def getGCD(a,b):
    """Euclid's algorithm for GCD"""
    while b:      
        a,b =b,a%b
    return a
    
def getLCM(a,b):
    """LCM algorithm"""
    return a*b//getGCD(a, b)

def getReducedLCM(els):
    """Return lcm of a list-iterates through list and applies getLCM to all of elements,for example:\n
    [1,5,7,20]-LCM(1,5)=5,LCM(5,7)=35,LCM(35,20)=140->result=140,\n or return(LCM(LCM(LCM(1,5),7),20))"""   
    return reduce(getLCM, els)

def main():
    
    checkers=[20,19,18,17,16,15,14,13,11]

    print(getReducedLCM(checkers))


if __name__=="__main__":
    main()