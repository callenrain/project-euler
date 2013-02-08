def isprime(startnumber):
    startnumber*=1.0
    for divisor in range(2,int(startnumber**0.5)+1):
        if startnumber/divisor==int(startnumber/divisor):
            return False
    return True

def main():
    primenumber = 0
    max = input("What number do you want to go to?")
    for a in range(2,max):
        if isprime(a):
            primenumber = primenumber+1
            print "Prime #",primenumber,":", a
main()
