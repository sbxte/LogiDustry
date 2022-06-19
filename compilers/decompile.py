import re
import random
import string
from pprint import pprint

lastJumpNameIndex = 0
jumps = {}
FILE_NAME = "input.txt"
JUMP_REGEX = r"jump (\d+)"
with open(FILE_NAME, "r", errors="replace") as inFile:
    for line in inFile:
        jumpSearch = re.search(JUMP_REGEX, line)
        if jumpSearch:
            jumpingIndex = jumpSearch.group(1)
            if jumpingIndex == "0":
                jumps[jumpingIndex] = "0"
            else:
                jumps[jumpingIndex] = "jump_" + str(lastJumpNameIndex) + "_"
            lastJumpNameIndex += 1


with open("output.txt", "w", errors="replace") as outFile:
    with open(FILE_NAME, "r", errors="replace") as inFile:
        for line in inFile:
            if re.search(r"^jump \d+", line):
                search = re.search(r"^jump (\d+) (.+)\s", line)
                replace = "jump "
                replace += jumps.get(search.group(1))
                replace += " "
                replace += search.group(2)
                replace += "\n"
                outFile.write(replace)
            else:
                outFile.write(line)

with open('output.txt', 'r+', errors="replace") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if str(i + 1) in jumps:
            lines[i] = line + jumps[str(i + 1)] + ":\n"
    f.seek(0)
    for line in lines:
        f.write(line)
