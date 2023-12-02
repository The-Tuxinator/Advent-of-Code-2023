import re
import pprint

settings = []
digit_str = (None, "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")

with open("input1_2.txt", "r") as input_text:
    for setting in input_text.readlines():

        digits = re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|zero|\d))", setting)
        for i, each in enumerate(digits):
            print(f"each digit {each}")
            if each in digit_str:
                print("each")
                digits[i] = digit_str.index(each)
        number = int(f"{digits[0]}{digits[-1]}")
        settings.append(number)


pprint.pprint(settings)
print(len(settings))
print(sum(settings))
