def parse_input(day: int, is_live: bool = True) -> list[str]:
    lines = []
    input_folder = "My_Inputs" if is_live else "Sample_Inputs"
    file_path = f"C://Users//Jim//Coding//AoC_2023//Inputs//{input_folder}//day_{day}.txt"
    with open(file_path, "r") as f:
        l = f.readlines()
        for line in l:
            lines.append(line.strip())
        return lines