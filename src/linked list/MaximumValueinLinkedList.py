# Problem: Maximum Value in Linked List
# URL: https://www.datapathsala.com/dsa/linked-list-max?difficulty=basic
# Date: 2026-07-10 21:45:10

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def maxValue(self, head: Optional[ListNode]) -> int:
        # Complexity T -> O(N), S -> O(1)
        if head.next is None:
            return head.val
        
        res = -10**5
        temp = head
        while temp:
            if res < temp.val:
                res = temp.val
            temp = temp.next
        # print(f"Max Value in List: {res}")
        return res