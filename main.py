import dcf
import os

map = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]

legend = [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9']

complete = False

while not complete:
    os.system('cls')
    print(f'{legend[map[0][0]]} {legend[map[0][1]]} {legend[map[0][2]]} | {legend[map[0][3]]} {legend[map[0][4]]} {legend[map[0][5]]} | {legend[map[0][6]]} {legend[map[0][7]]} {legend[map[0][8]]}\n{legend[map[1][0]]} {legend[map[1][1]]} {legend[map[1][2]]} | {legend[map[1][3]]} {legend[map[1][4]]} {legend[map[1][5]]} | {legend[map[1][6]]} {legend[map[1][7]]} {legend[map[1][8]]}\n{legend[map[2][0]]} {legend[map[2][1]]} {legend[map[2][2]]} | {legend[map[2][3]]} {legend[map[2][4]]} {legend[map[2][5]]} | {legend[map[2][6]]} {legend[map[2][7]]} {legend[map[2][8]]}\n---------------------\n{legend[map[3][0]]} {legend[map[3][1]]} {legend[map[3][2]]} | {legend[map[3][3]]} {legend[map[3][4]]} {legend[map[3][5]]} | {legend[map[3][6]]} {legend[map[3][7]]} {legend[map[3][8]]}\n{legend[map[4][0]]} {legend[map[4][1]]} {legend[map[4][2]]} | {legend[map[4][3]]} {legend[map[4][4]]} {legend[map[4][5]]} | {legend[map[4][6]]} {legend[map[4][7]]} {legend[map[4][8]]}\n{legend[map[5][0]]} {legend[map[5][1]]} {legend[map[5][2]]} | {legend[map[5][3]]} {legend[map[5][4]]} {legend[map[5][5]]} | {legend[map[5][6]]} {legend[map[5][7]]} {legend[map[5][8]]}\n---------------------\n{legend[map[6][0]]} {legend[map[6][1]]} {legend[map[6][2]]} | {legend[map[6][3]]} {legend[map[6][4]]} {legend[map[6][5]]} | {legend[map[6][6]]} {legend[map[6][7]]} {legend[map[6][8]]}\n{legend[map[7][0]]} {legend[map[7][1]]} {legend[map[7][2]]} | {legend[map[7][3]]} {legend[map[7][4]]} {legend[map[7][5]]} | {legend[map[7][6]]} {legend[map[7][7]]} {legend[map[7][8]]}\n{legend[map[8][0]]} {legend[map[8][1]]} {legend[map[8][2]]} | {legend[map[8][3]]} {legend[map[8][4]]} {legend[map[8][5]]} | {legend[map[8][6]]} {legend[map[8][7]]} {legend[map[8][8]]}')
    x = dcf.number_input(int, "X: ", 1, 9)-1
    y = dcf.number_input(int, "y: ", 1, 9)-1
    map[y][x] = dcf.number_input(int, "Number: ", 0, 9)

    