with open('StrategyGuide.txt') as f:
    Count1 = 0
    Check1 = 0
    for line in f:
        if line[2] == 'X':
            Count1 = Count1 + 0
            Check1 = Check1 + 1
        elif line[2] == 'Y':
            Count1 = Count1 + 3
            Check1 = Check1 + 1
        elif line[2] == 'Z':
            Count1 = Count1 + 6
            Check1 = Check1 + 1
        else:
            print('bye')

with open('StrategyGuide.txt') as d:
    Check2 = 0
    for line in d:
        if line[0] == 'A' and line[2] == 'X':
            Count1 = Count1 + 3
            Check1 = Check1 + 1
        elif line[0] == 'A' and line[2] == 'Y':
            Count1 = Count1 + 1
            Check1 = Check1 + 1
        elif line[0] == 'A' and line[2] == 'Z':
            Count1 = Count1 + 2
            Check1 = Check1 + 1
        elif line[0] == 'B' and line[2] == 'X':
            Count1 = Count1 + 1
            Check1 = Check1 + 1
        elif line[0] == 'B' and line[2] == 'Y':
            Count1 = Count1 + 2
            Check1 = Check1 + 1
        elif line[0] == 'B' and line[2] == 'Z':
            Count1 = Count1 + 3
            Check1 = Check1 + 1
        elif line[0] == 'C' and line[2] == 'X':
            Count1 = Count1 + 2
            Check1 = Check1 + 1
        elif line[0] == 'C' and line[2] == 'Y':
            Count1 = Count1 + 3
            Check1 = Check1 + 1
        elif line[0] == 'C' and line[2] == 'Z':
            Count1 = Count1 + 1
            Check1 = Check1 + 1
        else:
            print('hi')

print(Count1)
print(Check1)
     
# For some reason this code works if you run each individual 'for' loop, but once you put them one after the other, the second loop doesn't go through. In the end I just did these 2 loops separately and added them up.
