"""
Name : 36. Valid-Sudoku.py
Author : xyChen
Time : 2021/3/23 14:48
Desc:
"""
from typing import List


class Solution:
    # 思路就是很正常的,根据三条规则,通过visit来记录每一行 列 块中数字出现的次数
    # 第一次提交判断条件是2 in visit,最后有一个测试用例没通过,原因是该测试用例中有个块中有3个一样的数字
    # 所以改成max(visit) > 1
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            visited1 = [0] * 9
            visited2 = [0] * 9
            for j in range(9):
                if board[i][j] != '.':
                    pos = int(board[i][j]) - 1
                    visited1[pos] += 1
                if board[j][i] != '.':
                    pos = int(board[j][i]) - 1
                    visited2[pos] += 1
            if max(max(visited1), max(visited2)) > 1:
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                visited = [0] * 9
                for m in range(i, i + 3):
                    for n in range(j, j + 3):
                        if board[m][n] != '.':
                            pos = int(board[m][n]) - 1
                            visited[pos] += 1
                if max(visited) > 1:
                    return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValidSudoku([
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))