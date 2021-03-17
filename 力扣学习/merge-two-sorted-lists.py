"""
Name : merge-two-sorted-lists.py
Author : xyChen
Time : 2021/3/15 10:14
Desc: 合并两个升序链表，将新链表的头结点返回。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 麻烦的是python中没有指针这一概念。思路还是有的，1开辟新的链表，其中的元素是l1, l2中的较小者
# 2将l1, l2合并为一个有序链表。具体实现起来还是下不了手，主要是不明白ListNode的结构，不懂它的next是怎么回事
# 实现的代码是用户@风不语的答案，比较简单，明白。涉及指针问题可能用C/C++比较容易理解
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 这里的None是res.next为空，本身是存在的，相当于头指针
        res = ListNode(None)
        node = res
        while l1 and l2:
            if l1.val < l2.val:
                # node.next, l1 = l1, l1.next
                node.next = l1
                l1 = l1.next
            else:
                # node.next, l2 = l2, l2.next
                node.next = l2
                l2 = l2.next
            node = node.next
        if l1:
            node.next = l1
        else:
            node.next = l2
        return res.next


if __name__ == "__main__":
    node5 = ListNode(7, None)
    node3 = ListNode(3, node5)
    node1 = ListNode(1, node3)
    node4 = ListNode(4, None)
    node2 = ListNode(2, node4)
    solution = Solution()
    res = solution.mergeTwoLists(node1, node2)
    while res != None:
        print(res.val)
        res = res.next

