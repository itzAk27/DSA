# Problem: Search Value in Linked List
# URL: https://www.datapathsala.com/dsa/linked-list-search?difficulty=basic
# Date: 2026-07-10 21:34:47

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def searchList(self, head: Optional[ListNode], target: int) -> bool:
        # T -> O(N), S -> O(1)
        if head is None:
            return False
        
        temp = head
        while temp:
            if temp.val == target:
                return True
            temp = temp.next
        return False