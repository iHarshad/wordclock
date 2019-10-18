import numpy as np

Matrix = np.zeros((12,12)) # initialize mapping matrix

# Generates and returns mapping matrix
def getMatrix():
    even_row_ctr = 0;
    odd_row_ctr = 23;
    for i in range(12):
        for j in range(12):
            if (i % 2 == 0):
                Matrix[j][i] = even_row_ctr
                even_row_ctr = even_row_ctr + 1
            else:
                Matrix[j][i] = odd_row_ctr
                odd_row_ctr = odd_row_ctr - 1
        if (i % 2 == 0):
            even_row_ctr = even_row_ctr + 12
        else:
            odd_row_ctr = odd_row_ctr + 36
    return Matrix
