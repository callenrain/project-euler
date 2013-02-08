def makechain(start):
    a = []
    current = start
    while current != 1:
        a.append(current)
        if current%2==0:
            current = current/2
        else:
            current = ((current*3)+1)
    a.append(1)
    return a
       
def main():
    max = 0
    for i in range(1,1000000):
        a = makechain(i)
        length = len(a)
        if length > max:
            max = length
            value = i
            b = a
            print value
    print max, value
    print b
main()
    
    
