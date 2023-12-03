import re
from pprint import pp


def parse_numbers(line):
    search_result = re.search(r"\d+", line)
    if search_result is None:
        return
    number_list
    last_match = 0
    while True:
        search_result = re.search(r"\d+", line[number_list[-1].start()+1])
        if
        number_list.append()
    print number_list
    return re.finditer(r"\d+", line)


def parse_symbols(line):
    return re.finditer(r"[^\d|.|\n]", line)


def has_adjacent_symbol(number, symbols):
    for symbol in symbols:
        if number.start()-1 <= symbol.start() <= number.end()+1:
            return int(number.group(1))
    return 0


rows = []
part_numbers = []
with open("input3", "r") as input_file:
    for each in input_file.readlines():
        rows.append([parse_numbers(each), parse_symbols(each)])

pp(rows)

for i, row in enumerate(rows):
    symbols = row[1]
    if i > 0:
        symbols = symbols + rows[i-1][1]
    if i < len(rows):
        symbols = symbols + rows[i+1][1]
    for number in row[0]:
        part_numbers.append(has_adjacent_symbol(number, symbols))
print(part_numbers)
