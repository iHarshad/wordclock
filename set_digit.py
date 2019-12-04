def set_digit(digit, firstlastsingle): #first = 0, last = 1, single = 2
    offset = 0
    if firstlastsingle == 1:
            offset = 5
    elif firstlastsingle == 2:
            offset = 3

    if (digit == 1):
        if firstlastsingle != 0:
            offset = 2
        for r in range(9):
            Matrix[r][4 + offset] = 1
    elif (digit == 2):
        Matrix[2][1+offset] = 1
        Matrix[2][2+offset] = 1
        Matrix[2][3+offset] = 1
        Matrix[2][4+offset] = 1
        Matrix[3][4+offset] = 1
        Matrix[4][4+offset] = 1
        Matrix[5][4+offset] = 1
        Matrix[5][1+offset] = 1
        Matrix[5][2+offset] = 1
        Matrix[5][3+offset] = 1
        Matrix[6][1+offset] = 1
        Matrix[7][1+offset] = 1
        Matrix[8][1+offset] = 1
        Matrix[8][2+offset] = 1
        Matrix[8][3+offset] = 1
        Matrix[8][4+offset] = 1
    elif (digit == 3):
        Matrix[2][1+offset] = 1
        Matrix[2][2+offset] = 1
        Matrix[2][3+offset] = 1
        Matrix[2][4+offset] = 1
        Matrix[3][4+offset] = 1
        Matrix[4][4+offset] = 1
        Matrix[5][4+offset] = 1
        Matrix[5][1+offset] = 1
        Matrix[5][2+offset] = 1
        Matrix[5][3+offset] = 1
        Matrix[6][4+offset] = 1
        Matrix[7][4+offset] = 1
        Matrix[8][1+offset] = 1
        Matrix[8][2+offset] = 1
        Matrix[8][3+offset] = 1
        Matrix[8][4+offset] = 1
    elif (digit == 4):
        Matrix[2][4+offset] = 1
        Matrix[3][4+offset] = 1
        Matrix[4][4+offset] = 1
        Matrix[5][4+offset] = 1
        Matrix[6][4+offset] = 1
        Matrix[7][4+offset] = 1
        Matrix[2][1+offset] = 1
        Matrix[3][1+offset] = 1
        Matrix[4][1+offset] = 1
        Matrix[5][1+offset] = 1
        Matrix[5][2+offset] = 1
        Matrix[5][3+offset] = 1
    elif (digit == 5):
        Matrix[2][1+offset] = 1
        Matrix[2][2+offset] = 1
        Matrix[2][3+offset] = 1
        Matrix[2][4+offset] = 1
        Matrix[3][1+offset] = 1
        Matrix[4][1+offset] = 1
        Matrix[5][1+offset] = 1
        Matrix[5][2+offset] = 1
        Matrix[5][3+offset] = 1
        Matrix[8][1+offset] = 1
        Matrix[8][2+offset] = 1
        Matrix[8][3+offset] = 1
        Matrix[8][4+offset] = 1
    elif (digit == 6):
        Matrix[2][1+offset] = 1
        Matrix[2][2+offset] = 1
        Matrix[2][3+offset] = 1
        Matrix[2][4+offset] = 1
        Matrix[3][1+offset] = 1
        Matrix[4][1+offset] = 1
        Matrix[5][1+offset] = 1
        Matrix[5][2+offset] = 1
        Matrix[5][3+offset] = 1
        Matrix[6][1+offset] = 1
        Matrix[7][1+offset] = 1
        Matrix[8][1+offset] = 1
        Matrix[8][2+offset] = 1
        Matrix[8][3+offset] = 1
        Matrix[8][4+offset] = 1
        Matrix[6][1+offset] = 1
    elif (digit == 7):
        Matrix[2][1+offset] = 1
        Matrix[2][2+offset] = 1
        Matrix[2][3+offset] = 1
        Matrix[2][4+offset] = 1
        Matrix[3][4+offset] = 1
        Matrix[4][4+offset] = 1
        Matrix[5][4+offset] = 1
        Matrix[6][4+offset] = 1
        Matrix[7][4+offset] = 1
        Matrix[8][4+offset] = 1
    elif (digit == 8):
        Matrix[2][1+offset] = 1
        Matrix[2][2+offset] = 1
        Matrix[2][3+offset] = 1
        Matrix[2][4+offset] = 1
        Matrix[3][1+offset] = 1
        Matrix[4][1+offset] = 1
        Matrix[5][1+offset] = 1
        Matrix[5][2+offset] = 1
        Matrix[5][3+offset] = 1
        Matrix[6][1+offset] = 1
        Matrix[7][1+offset] = 1
        Matrix[8][1+offset] = 1
        Matrix[8][2+offset] = 1
        Matrix[8][3+offset] = 1
        Matrix[8][4+offset] = 1
        Matrix[6][1+offset] = 1
        Matrix[3][4+offset] = 1
        Matrix[4][4+offset] = 1
    elif (digit == 9):
        Matrix[2][1+offset] = 1
        Matrix[2][2+offset] = 1
        Matrix[2][3+offset] = 1
        Matrix[2][4+offset] = 1
        Matrix[3][4+offset] = 1
        Matrix[4][4+offset] = 1
        Matrix[5][4+offset] = 1
        Matrix[6][4+offset] = 1
        Matrix[7][4+offset] = 1
        Matrix[8][4+offset] = 1
        Matrix[3][1+offset] = 1
        Matrix[4][1+offset] = 1
        Matrix[5][1+offset] = 1
        Matrix[5][2+offset] = 1
        Matrix[5][3+offset] = 1
