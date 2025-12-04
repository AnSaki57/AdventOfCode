def isRepeatingNum(int: int) -> bool:
    s = str(int)
    checknum = (s + s)[1:-1]
    if checknum.find(s) == -1:
        return False
    return True

def getCount():
    inp = input().split(',')
    count = 0

    for numrange in inp:
        try:
            lb = int(numrange.split('-')[0])
            ub = int(numrange.split('-')[1])
            
            for i in range(lb, ub+1):
                if isRepeatingNum(i):
                    count+=i

        except ValueError:
            print(f"getDoubleCounts: {range}")
            continue
    
    print(count)

if __name__ == "__main__":
    getCount()