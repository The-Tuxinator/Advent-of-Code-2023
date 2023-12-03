import re


def parse_numbers(line):
    return list(re.finditer(r"\d+", line))


def parse_symbols(line):
    return list(re.finditer(r"[^\d|.|\n]", line))


def find_adjacent_numbers(symbol, numbers):
    adjacent_numbers = []
    for number in numbers:
        if number.start()-1 <= symbol.start() <= number.end():
            adjacent_numbers.append(int(number.group(0)))
    return adjacent_numbers


rows = []
gear_ratios = []

with open("input3", "r") as input_file:
    for each in input_file.readlines():
        rows.append([parse_numbers(each), parse_symbols(each)])


for i, row in enumerate(rows):
    for symbol in row[1]:
        if symbol.group(0) == "*":
            numbers = row[0]
            if i > 0:
                numbers = numbers + rows[i-1][0]
            if i < len(rows)-1:
                numbers = numbers + rows[i+1][0]
            adjacent_numbers = find_adjacent_numbers(symbol=symbol, numbers=numbers)
            if len(adjacent_numbers) == 2:
                gear_ratios.append(adjacent_numbers[0] * adjacent_numbers[1])


print(gear_ratios)
print(f"The sum is {sum(gear_ratios)}")
