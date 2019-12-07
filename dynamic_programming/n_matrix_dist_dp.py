# -*- coding: utf-8 -*-
# n * n 矩阵定点距离问题

n_matrix = [
    [1, 3, 5, 9],
    [2, 1, 3, 4],
    [5, 2, 6, 7],
    [6, 8, 4, 3],
]


def min_dist_dp(matrix, n):
    # 初始化一个n*n的二维数组
    states = []
    for i in range(n):
        states_item = [0] * n
        states.append(states_item)
    sum = 0
    for i in range(n):
        # 初始化第一行数据
        sum += matrix[0][i]
        states[0][i] = sum
    print(states)
    sum = 0
    for i in range(n):
        # 初始化第一列数据
        sum += matrix[i][0]
        states[i][0] = sum
    print(states)
    for i in range(1, n):
        for j in range(1, n):
            states[i][j] = matrix[i][j] + min(states[i][j-1], states[i-1][j])
    print(states)
    return states[n-1][n-1]


if __name__ == '__main__':
    print(min_dist_dp(n_matrix, 4))
