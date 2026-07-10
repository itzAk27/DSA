# Problem: Sum of All Nodes Values
# URL: https://www.datapathsala.com/dsa/linked-list-sum?difficulty=basic
# Date: 2026-07-10 20:54:32

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def listSum(self, head: Optional[ListNode]) -> int:
        # T -> O(N), S -> O(1)
        res = 0
        if head is None:
            return res
        
        if head.next is None:
            return head.val

        temp = head
        while temp:
            res += temp.val
            temp = temp.next
        return res