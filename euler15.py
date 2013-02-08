
def paths(x,y,Dict):
    print "X: ",x,"Y: ",y
    coords = str(x)+':'+str(y)
    if coords in Dict:
        val = Dict.get(coords)
        return val
    else:
        if x == 0 and y == 0:
            return 1
        else:
            if x == 0:
                val = paths(x,y-1,Dict)
                coords = (str(x)+":"+str(y-1))
                Dict.update({coords:val})
            elif y == 0:
                val = paths(x-1,y,Dict)
                coords = (str(x-1)+":"+str(y-1))
                Dict.update({coords:val})
            else:
                right = paths(x-1,y,Dict)
                coords = (str(x-1)+":"+str(y))
                Dict.update({coords:right})
                down = paths(x,y-1,Dict)
                coords = (str(x)+":"+str(y-1))
                Dict.update({coords:down})
                return right + down

def main():
    Dict = dict()
    print paths(2,2,Dict)

main()
