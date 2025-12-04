# import copy

def getArrFromInp(inp: list[str]) -> list[list[int]]:
    outp = []
    for line in inp:
        outline = []
        for char in line:
            if char == '.':
                outline.append(0)
            else:
                outline.append(1)
        outp.append(outline)
    return outp

def getAccessCount(inp: list[list[int]]) -> int:
    rows = len(inp)
    cols = len(inp[0])
    # print(f"r{rows}, c{cols}")
    # print(inp[0])
    count = 0

    # inpcopy = copy.deepcopy(inp)

    for i in range(rows):
        for j in range(cols):
            if inp[i][j] == 0: continue
            currcount = 0

            if i > 0:
                currcount+=inp[i-1][j]
                if j > 0:
                    currcount+=inp[i-1][j-1]
                if j < cols-1:
                    currcount+=inp[i-1][j+1]
            if j > 0:
                currcount+=inp[i][j-1]
            if j < cols-1:
                currcount+=inp[i][j+1]
            # if i == 0:
            #     print(f"currc {j},{currcount}")
            if i < rows-1:
                currcount+=inp[i+1][j]
                if j > 0:
                    currcount+=inp[i+1][j-1]
                if j < cols-1:
                    currcount+=inp[i+1][j+1]
            
            
            if currcount < 4:
                count+=1
                # inpcopy[i][j] = 2
    # print(inp[0])
    
    """
    for i in range(rows):
        for j in range(cols):
            if inpcopy[i][j] == 0:
                print('.', end='')
            elif inpcopy[i][j] == 1:
                print('@', end='')
            else:
                print('x', end='')
        print('')
    """

    return count

def main():
    inp = []
    while True:
        line = input()
        if line == "x":
            break
        inp.append(str(line))
    
    vals = getArrFromInp(inp)
    print(getAccessCount(vals))

if __name__ == "__main__":
    main()