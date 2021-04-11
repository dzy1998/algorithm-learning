"""
Name : 237. Delete-Node-in-a-Linked-List.py
Author : xyChen
Time : 2021/4/10 15:26
Desc:
"""


# Definition for singly-linked list.

head = []
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 并没有给head，思路是把node的下一结点复制到node，删除Node的下一节点
    # 思路来自@nkul
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        p = node.next
        node.val = p.val
        node.next = p.next
        # p = head
        # while p.next is not None:
        #     if p.next is node:
        #         p.next = node.next


if __name__ == '__main__':

