import math

total = 0

def checkAll(s: list) -> bool:
    if not all(s[i] < s[i + 1] and abs(s[i] - s[i + 1]) < 4 for i in range(len(s) - 1)):
        pass  # The sequence is strictly increasing with the required condition

    for i in range(0, len(s) - 1):
        
        

    # Check if the sequence is strictly decreasing with a difference of less than 4
    elif safe and all(s[i] > s[i + 1] and abs(s[i] - s[i + 1]) < 4 for i in range(len(s) - 1)):
        pass  # The sequence is strictly decreasing with the required condition

    else:
        return False
    return True

with open("/Users/wyattfreemanmacpro/AdventOfCode/2024/day1.txt") as f:
    for line in f:
        safe = True
        allowed = 0
        line = line.strip()
        s = list(map(int, line.split()))
        #NO LONGER NEED TO CHECK SIMILAR NUMS FOR SECOND PART
        # Check for equal numbers (early exit if any two numbers are equal)
        #if any(s[i] == s[i + 1] for i in range(len(s) - 1)):
            #safe = False

        # Check if the sequence is strictly increasing with a difference of less than 4
        checkAll(s)
