"""
Name : 83. Remove-Duplicates-from-Sorted-List.py
Author : xyChen
Time : 2021/3/26 13:59
Desc: 83. 删除排序链表中的重复元素
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 思路和之前的一道删除有序数组中的重复元素一样，同样是双指针遍历所有元素。只不过这次换成了指针，当相等的时候，不是i不动、j加1
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        i = head
        j = i.next
        while j is not None:
            if i.val == j.val:
                j = j.next
                i.next = j
                continue
            i = i.next
            j = j.next
        return head


if __name__ == '__main__':
    node5 = ListNode(3, None)
    node4 = ListNode(3, node5)
    node3 = ListNode(2, node4)
    node2 = ListNode(1, node3)
    head = ListNode(1, node2)
    solution = Solution()
    res = solution.deleteDuplicates(head)
    while res is not None:
        print(res.val)
        res = res.next
