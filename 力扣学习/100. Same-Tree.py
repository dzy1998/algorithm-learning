"""
Name : 100. Same-Tree.py
Author : xyChen
Time : 2021/4/1 9:54
Desc: 100. 相同的树
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if (p is None) and (q is None):
            return True
        if (p is None) or (q is None):
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # 思路是有的，递归的思路，但是python的链表实现实在不容易，自己调试不了
        # 下面的是我自己的，上面是来自@Tohsaka，直接改成python然后提交的，并没有调试
        # if (p is None and q is not None) or (p is not None and q is None):
        #     return False
        # else:
        #     if p is None:
        #         return True
        #     else:
        #         if p.val != q.val:
        #             return False
        #         else:
        #             if p.left:
        #                 self.isSameTree(p.left, q.left)
        #             if p.right:
        #                 self.isSameTree(p.right, q.right)
        #             return True


if __name__ == '__main__':
    solution = Solution()

    res = solution.isSameTree(p=[1, 2], q=[1, None, 2])
    print(res)
