
from math import sqrt


def Condition(a,b,c):
    return c**2==a**2+b**2

def getTriplets():
    """ Supposed to generate Pythagorean triplets, not used"""
    l=[x for x in range(1,500)]
    
    
    for el in l:
        if el%2:
            print(el,((el**2-1)/2),((el**2+1)/2),(el+(el**2-1)/2+(el**2+1)/2))
            if el+(el**2-1)/2+(el**2+1)/2==1000:
                return(el,(el**2-1)/2,(el**2+1)/2)           
        else:

            print(el,((el/2)**2-1),((el/2)**2+1),(el+(((el/2))**2)*2))
            if el+(((el/2))**2)*2==1000:
                return(el,((el/2))**2-1,((el/2))**2+1)

def getRes():
    """Brute force way of finding given triplet,\n
    Boundaries:\n   
        x->(x<y && x<z)\n
        y->(y<z)\n
        z->(z**2==x**2+y**2)\n
        x,y,z->x+y+z==1000\n
    
    """
    ctr=0
    for x in range(334):
        
        for y in range(x,500):
            ctr+=1
            z=1000-x-y
            if not (ctr%100):
                print(f"GEN(x100) {int(ctr/100)}:({x,y,z})")
            if Condition(x,y,z):
                return (ctr,x,y,z)
    
    


def main():
        
    gen,a,b,c=getRes()
    print(f"In {int(gen*100)} iterations, the triplet:{a,b,c} has the product of:{a*b*c}")

if __name__=='__main__':
    main()