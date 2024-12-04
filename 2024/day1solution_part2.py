import math
first = []
sec = {}
total = 0
with open("/Users/wyattfreemanmacpro/AdventOfCode/2024/day1.txt") as f:
    for line in f:
        s = line.split("   ")
        first.append(int(s[0]))
        if int(s[1]) not in sec:
            sec[int(s[1])] = 1
        elif int(s[1]) in sec:
            sec[int(s[1])] += 1

for i in first:
    if i in sec:
        total += (i * sec[i])

print(total)