import AoC_Lib

def part_one(lines):
    total = 0
    MAX_RED = 12
    MAX_GREEN = 13
    MAX_BLUE = 14
    for line in lines:
        line = line.split(':')
        id = int(line[0][5:])
        games = line[1].split(';')
        possible = True
        for game in games:
            draws = game.split(',')
            for draw in draws:
                if draw[-3:] == 'red':
                    if int(draw[:-4]) > MAX_RED:
                        possible = False
                        break
                elif draw[-5:] == 'green':
                    if int(draw[:-6]) > MAX_GREEN:
                        possible = False
                        break
                elif draw[-4:] == 'blue':
                    if int(draw[:-5]) > MAX_BLUE:
                        possible = False
                        break
            if not possible:
                break
        if possible:
            total += id
    return total

def part_two(lines):
    total = 0
    for line in lines:
        line = line.split(':')
        id = int(line[0][5:])
        max_red = 0
        max_green = 0
        max_blue = 0
        games = line[1].split(';')
        for game in games:
            draws = game.split(',')
            for draw in draws:
                if draw[-3:] == 'red':
                    max_red = max(max_red, int(draw[:-4]))
                elif draw[-5:] == 'green':
                    max_green = max(max_green, int(draw[:-6]))
                elif draw[-4:] == 'blue':
                    max_blue = max(max_blue, int(draw[:-5]))
        total += max_red * max_green * max_blue
    return total

def main():
    lines = AoC_Lib.parse_input(2)
    print(part_one(lines))
    print(part_two(lines))

if __name__ == "__main__":
    main()