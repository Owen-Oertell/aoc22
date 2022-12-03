# input from input.txt
import sys

sys.stdin = open('input.txt', 'r')

proritySum = 0
while True:
    try:
        a = input()
        b = input()
        c = input()
        # for each char in all three
        overlap = []
        for i in range(len(a)):
            # if char is in all three
            if a[i] in b and a[i] in c:
                # add the index of the char in a to the sum
                overlap.append(a[i])

        left = [ord(i) - 96 if i.islower() else ord(i) - 38 for i in overlap]
        #print("Max is " + str(max(left)))
        proritySum += max(left)

    except EOFError:
        print(proritySum)
        break