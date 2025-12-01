def get_offset(s: str) -> int:
    direction_map = {'L': -1, 'R': 1}

    try:
        direction = direction_map[s[0].upper()]
    except KeyError:
        raise ValueError(f"Invalid direction {s[0]}. Must be 'L' or 'R'.")
    
    try:
        magnitude = int(s[1:])
    except ValueError:
        raise ValueError("Invalid number format in '{s}'.")
    
    return direction * magnitude

def process_offsets():
    curr_position = 50
    zero_count = 0

    while(True):
        try:
            inp = input()
        except EOFError:
            break

        if inp.lower() == "x":
            break

        try:
            offset = get_offset(inp)
            curr_position += offset
            curr_position %= 100

            if curr_position == 0:
                zero_count += 1
            # print(f"curr:{curr_position}, offset:")
        except (ValueError, IndexError) as e:
            print(f"Skipping invalid input: {e}")
            continue
    
    print(zero_count)

if __name__ == "__main__":
    process_offsets()

"""
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
        curr+=offset
        curr%=100
        if curr == 0:
            sol+=1
    print(sol)

if __name__ == "__main__":
    main()
"""