# Problem: Delete First Node with given Value
# URL: https://www.datapathsala.com/dsa/delete-node-by-value?difficulty=basic
# Date: 2026-07-11 19:07:11

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNode(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Time Complexity -> O(N), Space Complexity -> O(1)
        if head is None:
            return head
        
        # Only one node in list 
        if head.val == val:
            head = head.next
            return head

        prev = None
        current = head

        while current and current.val != val:
            prev = current
            current = current.next
        
        if current is None:
            return head
        
        prev.next = current.next
        return head