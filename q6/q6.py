def maxFromLine(line: str) -> int:
    num : int  = 0
    start = 0
    
    for i in range(12):
        end = len(line) + i - 12
        maxdig = 0
        oldstart = start
        for index, digit in enumerate(line[start:end+1]):
            dig = int(digit)
            if dig > maxdig:
                maxdig = dig
                start = index+oldstart+1
        num = num*10+maxdig
    
    print(num)
    return num

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