# read from the file
with open('input.txt', 'r') as f:
    data = f.read()
    # for each line
    total = 0
    for line in data.splitlines():
        # split the line into the two numbers
        opp, you = line.split()
        val = 0
        if opp == 'A':
            opp = 'R'
            val = 1
        elif opp == 'B':
            opp = 'P'
            val = 2
        elif opp == 'C':
            opp = 'S'
            val = 3

        if you == 'Y':
            # need to draw
            total += val + 3
        elif you == 'X':
            # need to lose
            if opp == 'R':
                total += 3
            elif opp == 'P':
                total += 1
            elif opp == 'S':
                total += 2
        elif you == 'Z':
            # need to win
            if opp == 'R':
                total += 2 + 6
            elif opp == 'P':
                total += 3 + 6
            elif opp == 'S':
                total += 1 + 6

        print(total)
    print(total)
