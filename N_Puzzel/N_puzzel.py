import math

puzzle = [[6, 1, 10, 2], [7, 11, 4, 14], [5, 10000, 9, 15], [8, 12, 13, 3]]

list = []


def returninver(puzzle):
    count = 0

    for row in puzzle:
        x = len(row)
        for col in row:
            list.append(col)
            d = len(list)

    blank = list.index(10000)
    for i in range(len(list)):
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                count = count + 1
    for k in range(len(list)):
        indexnum = list.index(10000)
    inv = count - (indexnum - blank)
    row = math.ceil((d - blank) / x)

    print(" Number of Puzzle : ", puzzle)
    print("Number of Inversion:", inv)
    print("Number of Dimenstion :", d)
    print("Blank  Row Postion From Bottom:", row)

    return inv, row, d


def isEven(number):
    if (number % 2 == 0):
        return True
    else:
        return False









def solvablity(inv, blank, d):
    if (isEven(d) == False and isEven(inv) == True):
        print("it is Solvable")

    elif (isEven(d) == True and isEven(row) == False and isEven(inv) == True):
        print("it is Solvable")
    elif (isEven(d) == True and isEven(row) == True and isEven(inv) == False):

        print("Comment: Yes it is Solvable")
    else:
        print("Comment: No! It is not  Solvable")
    return solvablity


inv, row, d = returninver(puzzle)
solvablity(inv, row, d)