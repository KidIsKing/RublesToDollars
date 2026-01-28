from string import digits


info_is_ready = False
with open("statistics.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    count_lines = len(lines)

if count_lines > 7:
    info_is_ready = True
    start_file = count_lines - 14
    end_file = count_lines - 9

    lines_list = []
    for stroka in lines[start_file:end_file]:
        line = stroka.split()
        lines_list.append(line)

    correct_lines = []
    for strochka in lines_list:
        for el in strochka:
            if el[0] in digits and ":" not in el and el.count(".") <= 1:
                correct_lines.append(strochka)

    usd_old_data = float(correct_lines[0][0])
    eur_old_data = float(correct_lines[1][0])
    gbp_old_data = float(correct_lines[2][0])
    aed_old_data = float(correct_lines[3][0])
    cny_old_data = float(correct_lines[4][0])

    price_old_data = [
        usd_old_data,
        eur_old_data,
        gbp_old_data,
        aed_old_data,
        cny_old_data
    ]
else:
    info_is_ready = False
    price_old_data = []


if __name__ == "__main__":
    print(correct_lines)
