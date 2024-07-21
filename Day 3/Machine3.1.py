with open('Rucksacks.txt') as f:
    bag = dict()
    count = 0
    for line in f:
        line = line.rstrip()
        count = count + 1
        bag[count] = line.split(f'{line[int((len(line) / 2) - 1)]}')      

