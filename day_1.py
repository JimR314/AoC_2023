import AoC_Lib

def parse_input(day):
    lines = []
    with open(f"C://Users//Jim//Coding//AoC_2023//day_{day}.txt", "r") as f:
        l = f.readlines()
        for line in l:
            lines.append(line.strip())
        return lines

def add_first_and_last_digit_of_alphanumeric_string(s):
    first = False
    num = ''
    for char in s:
        if char.isnumeric():
            first = True
            num += char
            break
    for char in s[::-1]:
        if char.isnumeric():
            num += char
            break
    return int(num)

def part_one(lines):
    total = 0
    for line in lines:
        total += add_first_and_last_digit_of_alphanumeric_string(line)
    return total

def part_two(lines):
    words = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    total = 0
    for line in lines:
        i = 0
        num = ''
        while i < len(line):
            if line[i].isnumeric():
                num += line[i]
                break
            elif i + 4 < len(line) and line[i:i+5] in words:
                num += str(words[line[i:i+5]])
                break
            elif i + 3 < len(line) and line[i:i+4] in words:
                num += str(words[line[i:i+4]])
                break
            elif i + 2 < len(line) and line[i:i+3] in words:
                num += str(words[line[i:i+3]])
                break
            else:
                i += 1
        i = len(line)
        while i >= 0:
            if line[i-1].isnumeric():
                num += line[i-1]
                break
            if i - 5 >= 0 and line[i-5:i] in words:
                num += str(words[line[i-5:i]])
                break
            elif i - 4 >= 0 and line[i-4:i] in words:
                num += str(words[line[i-4:i]])
                break
            elif i - 3 >= 0 and line[i-3:i] in words:
                num += str(words[line[i-3:i]])
                break
            else:
                i -= 1
        total += int(num)
    return total
        

def main():
    lines = AoC_Lib.parse_input(1)
    # print(part_one(lines))
    print(part_two(lines))

if __name__ == "__main__":
    main()