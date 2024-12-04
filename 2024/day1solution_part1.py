import math
first = []
sec = []
total = 0
with open("/Users/wyattfreemanmacpro/AdventOfCode/2024/day1.txt") as f:
    for line in f:
        s = line.split("   ")
        first.append(s[0])
        sec.append(s[1])
    first.sort()
    sec.sort()

for i in range(0, len(first)):
    total += abs(int(first[i]) - int(sec[i]))

print(total)