from string import digits


info_is_ready = False
with open("statistics.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    count_lines = len(lines)

if count_lines > 1:
    info_is_ready = True
    start_file = count_lines - 14
    end_file = count_lines - 9

    lines_list = []
    for stroka in lines[start_file:end_file]:
        line = stroka.split()
        for el in line:
            if el[0] in digits and ":" not in el and el.count(".") <= 1:
                lines_list.append(line)

    old_valutes_of_data = [
        float(lines_list[i][0]) for i in range(len(lines_list))
        ]
else:
    info_is_ready = False
    old_valutes_of_data = []


if __name__ == "__main__":
    print(lines_list)
