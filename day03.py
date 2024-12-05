import re

result = 0

with open("input.txt") as f:
    for prog in f:
        for match in re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)', prog):
            result += int(match.group(1)) * int(match.group(2))

print(result)

result = 0

calc = True
with open("input.txt") as f:
    for prog in f:
        for group in re.split(r"(don't\(\)|do\(\))", prog):
            if group == "don't()":
                calc = False
            elif group == "do()":
                calc = True
            elif calc:
                for match in re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)', group):
                    result += int(match.group(1)) * int(match.group(2))

print(result)
