from math import *

def main():
    sumsq = 0
    sqsum = 0
    for i in range(1,101):
        sumsq = sumsq + pow(i,2)
    for i in range(1,101):
        sqsum = sqsum + i
    print sqsum
    sqsum = pow(sqsum,2)
    print "Sum of the squares:", sumsq
    print "Square of the sums:", sqsum
    print "Difference:" , sqsum - sumsq
main()
