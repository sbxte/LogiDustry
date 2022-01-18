import re
import random
import string
from pprint import pprint

jumps = {}
FILE_NAME = "input.txt"
JUMP_REGEX = r"jump (\d+)"
with open(FILE_NAME, "r") as file:
    for line in file:
        if re.search(JUMP_REGEX, line):
            jumps[re.search(JUMP_REGEX, line).group(1)] = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=8))
with open(FILE_NAME, "r") as f:
    text = f.read()


with open ("output.txt", "r+") as file2:
    with open(FILE_NAME, "r") as file:
        for line in file:
            if re.search(r"jump \d+", line):
                search = re.search(r"jump (\d+) (.+)\s", line)
                replace = "jump "
                replace += jumps.get(search.group(1))
                replace += " "
                replace += search.group(2)
                replace += "\n"

                file2.write(replace)
            else:
                file2.write(line)

with open('output.txt', 'r+') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if str(i + 1) in jumps:
            lines[i] = line + jumps[str(i + 1)] + ":\n"
    f.seek(0)
    for line in lines:
        f.write(line)
