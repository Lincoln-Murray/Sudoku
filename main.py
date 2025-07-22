import dcf
import os

map = [
[7,9,2,1,5,4,3,8,6],
[6,4,3,8,2,7,1,5,9],
[8,5,1,3,9,6,7,2,4],
[2,6,5,9,7,3,8,4,1],
[4,8,9,5,6,1,2,7,3],
[3,1,7,4,8,2,9,6,5],
[1,3,6,7,4,8,5,9,2],
[9,7,4,2,1,5,6,3,8],
[5,2,8,6,3,9,4,1,7]

]

legend = [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9']

complete = False

while not complete:
    os.system('cls')
    print(f'{legend[map[0][0]]} {legend[map[0][1]]} {legend[map[0][2]]} | {legend[map[0][3]]} {legend[map[0][4]]} {legend[map[0][5]]} | {legend[map[0][6]]} {legend[map[0][7]]} {legend[map[0][8]]}\n{legend[map[1][0]]} {legend[map[1][1]]} {legend[map[1][2]]} | {legend[map[1][3]]} {legend[map[1][4]]} {legend[map[1][5]]} | {legend[map[1][6]]} {legend[map[1][7]]} {legend[map[1][8]]}\n{legend[map[2][0]]} {legend[map[2][1]]} {legend[map[2][2]]} | {legend[map[2][3]]} {legend[map[2][4]]} {legend[map[2][5]]} | {legend[map[2][6]]} {legend[map[2][7]]} {legend[map[2][8]]}\n---------------------\n{legend[map[3][0]]} {legend[map[3][1]]} {legend[map[3][2]]} | {legend[map[3][3]]} {legend[map[3][4]]} {legend[map[3][5]]} | {legend[map[3][6]]} {legend[map[3][7]]} {legend[map[3][8]]}\n{legend[map[4][0]]} {legend[map[4][1]]} {legend[map[4][2]]} | {legend[map[4][3]]} {legend[map[4][4]]} {legend[map[4][5]]} | {legend[map[4][6]]} {legend[map[4][7]]} {legend[map[4][8]]}\n{legend[map[5][0]]} {legend[map[5][1]]} {legend[map[5][2]]} | {legend[map[5][3]]} {legend[map[5][4]]} {legend[map[5][5]]} | {legend[map[5][6]]} {legend[map[5][7]]} {legend[map[5][8]]}\n---------------------\n{legend[map[6][0]]} {legend[map[6][1]]} {legend[map[6][2]]} | {legend[map[6][3]]} {legend[map[6][4]]} {legend[map[6][5]]} | {legend[map[6][6]]} {legend[map[6][7]]} {legend[map[6][8]]}\n{legend[map[7][0]]} {legend[map[7][1]]} {legend[map[7][2]]} | {legend[map[7][3]]} {legend[map[7][4]]} {legend[map[7][5]]} | {legend[map[7][6]]} {legend[map[7][7]]} {legend[map[7][8]]}\n{legend[map[8][0]]} {legend[map[8][1]]} {legend[map[8][2]]} | {legend[map[8][3]]} {legend[map[8][4]]} {legend[map[8][5]]} | {legend[map[8][6]]} {legend[map[8][7]]} {legend[map[8][8]]}')
    x = dcf.number_input(int, "X: ", 1, 9)-1
    y = dcf.number_input(int, "y: ", 1, 9)-1
    map[y][x] = dcf.number_input(int, "Number: ", 0, 9)
    for line in map:
        if 1 in line and 2 in line and 3 in line and 4 in line and 5 in line and 6 in line and 7 in line and 8 in line and 9 in line and not 0 in line:
            complete = True
        else:
            complete = False
            break
    if complete:
        for i in range(0, len(map[0])):
            column = [map[0][i], map[1][i], map[2][i], map[3][i], map[4][i], map[5][i], map[6][i], map[7][i], map[8][i]]
            if 1 in column and 2 in column and 3 in column and 4 in column and 5 in column and 6 in column and 7 in column and 8 in column and 9 in column and not 0 in column:
                complete = True
            else:
                complete = False
                print("column invalid")
                break
    if complete:
        for x in range(0,8,3):
            for y in range(0,8,3):
                square = [map[y][x], map[y+1][x], map[y+2][x], map[y][x+1], map[y+1][x+1], map[y+2][x+1], map[y][x+2], map[y+1][x+2], map[y+2][x+2]]
                #print(square[0:3])
                #print(square[3:6])
                #print(square[6:9])
                if 1 in square and 2 in square and 3 in square and 4 in square and 5 in square and 6 in square and 7 in square and 8 in square and 9 in square and not 0 in square:
                    complete = True
                else:
                    complete = False
                    print("square invalid")
                    break

print("Good job")