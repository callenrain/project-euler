def main():
    bignum = 2**1000
    bigstr = str(bignum)
    length = len(bigstr)
    total = 0
    for i in range(length):
      total = total + int(bigstr[i])
    print total
main()
