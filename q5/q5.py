def maxFromLine(line: str) -> int:
    """
    currmax : int = 0

    for index, digit in enumerate(line):
        c1 = currmax/10
        c2 = currmax%10
        digint = int(digit)

        if digint > c1 and index is not len(line)-1:
            currmax = digint*10
        elif digint > c2:
            currmax = int(c1*10 + digint)

    print(currmax)
    return currmax
    """
    currmax : int = 0
    currjolt : int = 0

    for index, digit in enumerate(line):
        currdig = int(digit)
        currjolt = max(currjolt, currmax * 10 + currdig)
        currmax = max(currmax, currdig)
    
    return currjolt

def parseInp():
    sum : int = 0
    while (True):
        line = input()
        if line == "x":
            break

        sum += maxFromLine(line)
    
    print(sum)

if __name__ == "__main__":
    parseInp()