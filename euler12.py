from math import*

def getfactors(value):
    a = []
    max = 0
    for i in range(1,int(sqrt(value))):
        if value%i == 0:
            a.append(i)
    return a

def main():
    number = 1
    for i in range (2,10000000):
        number = number+i
        a = getfactors(number)
        length = 2*len(a)
        if length > 500:
            print number, " has length: ", length
main()
        
            
