# -*- coding: utf-8 -*-
# n阶矩阵求最短路径

min_dist_value = 500  # 默认整一个很小的值


n_matrix = [
    [1, 3, 5, 9],
    [2, 1, 3, 4],
    [5, 2, 6, 7],
    [6, 8, 4, 3],
]


def min_dist(i, j, dist, matrix, n):
    global min_dist_value
    if i == n and j == n:
        # if dist < min_dist_value:
        #     min_dist_value = dist
        #     print(dist)
        print(dist)
        return
    if i < n:
        # 往下走
        min_dist(i + 1, j, dist + matrix[i][j], matrix, n)
    if j < n:
        min_dist(i, j + 1, dist + matrix[i][j], matrix, n)


if __name__ == '__main__':
    min_dist(0, 0, 1, n_matrix, 3)