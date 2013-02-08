def getdigit(i):
    if i < 10:
        digit = 1
    elif i < 100:
        digit = 2
    elif i < 1000:
        digit = 3
    else:
        digit = 4
    return digit

def calcone(i):
    if i == 1:
        return 3
    elif i == 2:
        return 3
    elif i == 6:
        return 3
    elif i == 3:
        return 5
    elif i == 7:
        return 5
    elif i == 8:
        return 5
    elif i == 4:
        return 4
    elif i == 5:
        return 4
    elif i == 9:
        return 4
    else:
        return 0
    
def calctwo(i):
    if i < 10:
        return calcone(i)
    elif i < 20:
        if i == 10:
            return 3
        elif i == 11:
            return 6
        elif i == 12:
            return 6
        elif i == 13:
            return 8
        elif i == 14:
            return 8
        elif i == 19:
            return 8
        elif i == 15:
            return 7
        elif i == 17:
            return 9
        elif i == 16:
            return 7
        elif i == 18:
            return 8
    else:
        s = str(i)
        onesplace = calcone(int(s[1]))
        tensplace = int(s[0])
        if tensplace == 2:
            tens = 6
        if tensplace == 3:
            tens = 6
        if tensplace == 4:
            tens = 5
        if tensplace == 8:
            tens = 6
        if tensplace == 9:
            tens = 6
        elif tensplace == 5:
            tens = 5
        elif tensplace == 6:
            tens = 5
        elif tensplace == 7:
            tens = 7
        return tens + onesplace

def calcthree(i):
    if i == 100:
        return 10
    else:
        s = str(i)
        hundreds = calcone(int(s[0])) + 7
        if s[1:] == '00':
            return hundreds
        else:
            tens = calctwo(int(s[1:]))
            return hundreds + tens + 3
  
def main():
    from time import clock
    start = clock()
    total = 0
    for i in range(1,1001):
        digit = getdigit(i)
        if digit == 1:
            num = calcone(i)
            total = total + num
        elif digit == 2:
            num = calctwo(i)
            total = total + num
        elif digit == 3:
            num = calcthree(i)
            total = total + num
        else:
            num = 11
            total = total + num
    print total
    """while True:
        i = input("Enter: ")
        digit = getdigit(i)
        if digit == 1:
            num = calcone(i)
        elif digit == 2:
            num = calctwo(i)
        elif digit == 3:
            num = calcthree(i)
        else:
            num = 11
        print num"""
    print (clock() - start)
main()
    
