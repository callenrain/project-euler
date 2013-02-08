def main():
    count = 1
    for i in range(100,1,-1):
        count = count * i
    count = str(count)
    num = 0
    for i in range(len(count)):
        num = num + int(count[i])
    print num
main()
