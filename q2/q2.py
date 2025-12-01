
def getoffset(s):
    num = int(s[1:])
    if s[0] == 'L':
        num*=-1
    return num

def main():
    curr = 50
    sol = 0

    while(True):
        inp = input()
        if inp == "x":
            break
        offset = getoffset(inp)
        next = curr+offset
        if curr == 0 and next < 0:
            sol-=1
        while next < 0:
            next+=100
            sol+=1
        while next > 99:
            next-=100
            sol+=1
        if inp[0] == 'L' and next == 0:
            sol+=1
        # print(f"curr:{curr}, next:{next}, sol:{sol}")
        curr = next
    print(sol)

if __name__ == "__main__":
    main()