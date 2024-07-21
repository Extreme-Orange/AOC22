with open('Rucksacks.txt') as f:
    for line in f:
        line = line.rstrip()
        print(int(len(line) / 2))