def getDigitCount(inp: int) -> int:
    return len(str(inp))

def getFullNum(half: int) -> int:
    digCount = getDigitCount(half)
    return half * 10 ** digCount + half


def getSmallestDigNum(digCount: int) -> int:
    return 10**(digCount-1)

def getLargestDigNum(digCount: int) -> int:
    try:
        num = 9
        digCount-=1
        while digCount > 0:
            num*=10
            num+=9
            digCount-=1
        return num
    except ValueError:
        print(f"getLargestDigNum: {digCount}")
        return -1


def getSmallestLargerDoubleNumber_Half(inp: int) -> int:
    try:
        len = getDigitCount(inp)
        if len%2 == 1:
            halflen = int(len/2)+1
            return getSmallestDigNum(halflen)
        
        halfnum = int(inp/(10**(len/2)))
        if inp%(10**(len/2)) > halfnum:
            halfnum+=1
    
        return halfnum 
    except ValueError:
        print(f"getSmallestLargetDoubleNumber_Half: {inp}")
        return -1

def getLargestSmallerDoubleNumber_Half(inp: int) -> int:
    try:
        len = getDigitCount(inp)
        if len%2 == 1:
            halflen = int(len/2)
            return getLargestDigNum(halflen)
        
        halfnum = int(inp/(10**(len/2)))
        if inp%(10**(len/2)) < halfnum:
            halfnum-=1
        
        return halfnum 
    except ValueError:
        print(f"getLargestSamllerDoubleNumber_Half: {inp}")
        return -1


def getDoubleCountSums(lb: int, ub: int) -> int:
    try:
        lbnum = getSmallestLargerDoubleNumber_Half(lb)
        ubnum = getLargestSmallerDoubleNumber_Half(ub)
        print(f"{lbnum}, {ubnum}")

        sum = 0
        for i in range(lbnum, ubnum+1):
            sum += getFullNum(i)

        return sum
    except ValueError:
        print(f"getDoubleCountRange: {lb}-{ub}")
        return -1

def getDoubleCounts():
    inp = input().split(',')
    count = 0

    for range in inp:
        try:
            lb = int(range.split('-')[0])
            ub = int(range.split('-')[1])
            count+=getDoubleCountSums(lb, ub)
        except ValueError:
            print(f"getDoubleCounts: {range}")
            continue
    
    print(count)

"""
def test():
    print(getDoubleCountRange(123124, 123123))
"""

if __name__ == "__main__":
    getDoubleCounts()