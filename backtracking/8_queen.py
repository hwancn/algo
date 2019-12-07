# -*- coding: utf-8 -*-
# 八皇后问题
result = [None] * 8


def isOk(row, col):
    """
    判断row行col列是否合适，在代码中其实我们只需要看row行的上面的行就行了，row行下面没有棋子，我们是从上往下放的
    :param row:
    :param col:
    :return:
    """
    leftup, rightup = col-1, col+1 # col列的左右两列
    for i in range(row-1, -1, -1):
        if result[i] == col:
            # 第i行的第col列已经填了棋子
            return False
        # 考察左对角线
        if leftup >= 0:
            if result[i] == leftup:
                # 第i行的第leftup列上面有棋子
                return False
        # 判断有对角线
        if rightup <= 7:
            if result[i] == rightup:
                # 第i行的rightup列有棋子
                return False
        # 分别向左向右移动对角线元素，判断上一行
        leftup -= 1
        rightup += 1
    return True


def cal8queens(row):
    """
    调用的时候cal8queens(0)
    :param row: 开始的行数，
    :return:
    """
    if row == 8:
        # 已经放了8行了
        print(result)
        return
    for col in range(0, 8):
        # 我们使用0--7分别表示8列
        if isOk(row, col):
            result[row] = col
            cal8queens(row+1)


if __name__ == '__main__':
    cal8queens(0)
