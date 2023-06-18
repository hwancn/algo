# -*- coding: utf-8 -*-

# matrix是个二维数组，用于表示杨辉三角
# 本题中可以为 [[5], [7,8], [2,3,4], [4,9,6,1], [2,7,9,4,5]]
def yanghui_triangle(matrix):
    n = len(matrix)
    w = len(matrix[-1])
    # 初始化state 数组
    # 假设路径不存在负数
    # 对于第n行，那一行的元素个数为n+1
    state = []
    for i in range(n):
        inner = [-1] * (i + 1)
        state.append(inner)
    print(state)
    state[0][0] = matrix[0][0]
    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                # 那一行的第一个元素
                state[i][j] = state[i-1][j] + matrix[i][j]
            elif j == i:
                # 那一行的最后一个元素
                state[i][j] = state[i-1][j-1] + matrix[i][j]
            else:
                parent_left = state[i-1][j-1]
                parent_right = state[i-1][j]
                state[i][j] = min(parent_left, parent_right)  + matrix[i][j]
    # 找出最小的路径
    min_distance = 2 ** 32 - 1   # 最大int
    for j in range(n):  # 最下面那一排有n个元素
        if state[n-1][j] < min_distance:
            min_distance = state[n-1][j]
    return min_distance


if __name__ == '__main__':
    matrix = [[5], [7, 8], [2, 3, 4], [4, 9, 6, 1], [2, 7, 9, 4, 5]]
    print(yanghui_triangle(matrix))
    assert yanghui_triangle(matrix) == 20
