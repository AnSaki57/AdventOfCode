def getRangeList(ranges: list[str]) -> list[tuple[int, int]]:
    res = []
    for r in ranges:
        lb = r.split(sep='-')[0]
        ub = r.split(sep='-')[1]
        res.append((int(lb), int(ub)))

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
    ranges.sort(key=lambda item: item[1])

    while (True):
        line = input()
        if line == "":
            break
        items.append(int(line))
    
    freshCount = 0
    for item in items:
        for r in ranges:
            if r[1] < item:
                continue
            if r[0] <= item:
                freshCount+=1
                break
        print(item, freshCount)
    
    print(freshCount)

if __name__ == "__main__":
    getFreshCount()