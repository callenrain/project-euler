def rev(number):
    numstring = str(number)
    reversestring = numstring[::-1]
    reverseint = int(reversestring)
    return reverseint

def main():
    max = 0
    for i in range(999,100,-1):
        for j in range (999, 100, -1):
            reverse = rev(i*j)
            if reverse == i*j:
                if i*j > max:
                    max = i*j
                    print "Max found:", max
        print i,"is done"            
    print "Final max:", max
main()


