from numpy import prod #Helper tool to get product of a list P(l)

def checkPal(num):
    """Checks if given number is palindrome"""
    if num==num[::-1]:
        return True   
    
def getPalTuple(l):
    """Returns tuple of numbers whose product returns highest possible palindrome number in list range"""
    return max([[(x,el) for x in l if checkPal(str(x*el))] for el in l ])[0]
    
def main():
    l=[x for x in range(900,1000)]
    els=getPalTuple(l)  
    print(prod(els),els)
if __name__=="__main__":
    main()