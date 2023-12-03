def parse_input(day):
    lines = []
    with open(f"C://Users//Jim//Coding//AoC_2023//day_{day}.txt", "r") as f:
        l = f.readlines()
        for line in l:
            lines.append(line.strip())
        return lines