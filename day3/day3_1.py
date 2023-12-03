import re
from pprint import pp


def parse_numbers(line):
    return list(re.finditer(r"\d+", line))


def parse_symbols(line):
    return list(re.finditer(r"[^\d|.|\n]", line))


def has_adjacent_symbol(number, symbols):
    for symbol in symbols:
        if number.start()-1 <= symbol.start() <= number.end():
            return int(number.group(0))
    return 0


rows = []
part_numbers = []
with open("input3", "r") as input_file:
    for each in input_file.readlines():
        rows.append([parse_numbers(each), parse_symbols(each)])

# pp(rows)

for i, row in enumerate(rows):
    symbols = row[1]
    if i > 0:
        symbols = symbols + rows[i-1][1]
    if i < len(rows)-1:
        symbols = symbols + rows[i+1][1]
    for number in row[0]:
        part_numbers.append(has_adjacent_symbol(number, symbols))
print(part_numbers)
print(f"The sum is {sum(part_numbers)}")
