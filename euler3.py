def isprime(startnumber):
    startnumber*=1.0
    for divisor in range(2,int(startnumber**0.5)+1):
        if startnumber/divisor==int(startnumber/divisor):
            return False
    return True


def main():
    bigint = 600851475143
    for i in range(bigint-1,1,-1):
        if  bigint%i==0 and isprime(i):
            bigint = bigint/i
            break
    print bigint
main()
        

