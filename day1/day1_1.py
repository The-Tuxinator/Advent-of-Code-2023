import re

settings = []
with open("input1_1.txt", "r") as input_text:
    for setting in input_text.readlines():
        first_digit = str(re.search(r"\D*.", setting).group(0)[-1])
        last_digit = str(re.search(r".\D*$", setting).group(0)[0])
        settings.append(int(first_digit + last_digit))

print(settings)
print(sum(settings))
