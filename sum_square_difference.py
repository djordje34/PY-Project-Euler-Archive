def getSumOfSquares(l):
    """Returns sum of squared nums in  list"""
    return sum([x**2 for x in range(l+1)])


def getSquareOfSum(l):
    """Returns Squared sum of nums in a list"""
    return sum([x for x in range(l+1)])**2

def main():
    print(getSquareOfSum(100)-getSumOfSquares(100))
    
if __name__=='__main__':
    main()