with open('Calories.txt') as f:
    Elves = f.read().split('\n\n')
    count = 1
    Book = dict()
    for Elf in Elves:
        Book[count] = Elf.split('\n')
        count = count + 1
    Book2 = list()
    for k, v in Book.items():
        x = 0
        for i in range(0, len(v)):
            x = x + int(v[i])
        Book2.append(x)
    Book2.sort(reverse=True)
    print(Book2[0] + Book2[1] + Book2[2])