def getRangeList(ranges: list[str]) -> list[list[int]]:
    res = []
    for r in ranges:
        lb = r.split(sep='-')[0]
        ub = r.split(sep='-')[1]
        res.append([int(lb), int(ub)])

    return res

def getFreshCount():
    rangestrs = []
    items = []

    while (True):
        line = input()
        if line == "":
            break
        rangestrs.append(line)
    
    ranges = getRangeList(rangestrs)
    ranges.sort(key=lambda item: item[0])

    changes = True
    while (changes):
        changes = False
        rlen = len(ranges)
        
        i = 1
        while i < rlen:
            while i < rlen and ranges[i][0] <= ranges[i-1][1]:
                ranges[i-1][1] = max(ranges[i-1][1], ranges[i][1])
                del ranges[i]
                rlen -= 1
            i+=1
    
    sum = 0
    for r in ranges:
        print(r)
        sum+=r[1]-r[0]+1
    print(sum)


if __name__ == "__main__":
    getFreshCount()