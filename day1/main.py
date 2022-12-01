# read input from input.txt

import sys

sys.stdin = open('input.txt', 'r')
calCount = 0
c = []
# read lines until break
while True:
    try:
        line = input()
        if (line == ''):
            c.append(calCount)
            calCount = 0
        else:
            calCount += int(line)
    except EOFError:

        c.append(calCount)
        print(sum(sorted(c)[-3:]))
        break