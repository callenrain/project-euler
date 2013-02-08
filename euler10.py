def isprime(startnumber):
    startnumber*=1.0
    for divisor in range(2,int(startnumber**0.5)+1):
        if startnumber/divisor==int(startnumber/divisor):
            return False
    return True

def main():
    total = 0
    max = input("What number do you want to go to?")
    for a in range(2,max):
        if isprime(a):
            total = total+a
            if a%10000 == 0:
                print a
    print "current total is", total2
main()
