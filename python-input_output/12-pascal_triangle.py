#!/usr/bin/python3
'''doc'''


def pascal_triangle(n):
    '''doc'''
    lis = []
    row = 0

    for i in range(1, n+1):
        cur = []
        for j in range(i):
            if j == 0 or j == i-1:
                row = 1
            else:
                a = lis[i-2][j]
                b = lis[i-2][j-1]
                row = a + b
            cur.append(row)
        lis.append(cur)
    return lis
