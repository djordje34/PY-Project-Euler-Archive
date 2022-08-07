

def getVal(val):
    return sum([x for x in range(val) if (x%5==0 or x%3==0)])


def main():
    print(getVal(1000))
    
if __name__=="__main__":
    main()