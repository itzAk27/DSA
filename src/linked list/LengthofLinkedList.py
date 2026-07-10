# Problem: Length of Linked List
# URL: https://www.datapathsala.com/dsa/linked-list-length?difficulty=basic
# Date: 2026-07-10 21:54:09

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getLength(self, head: Optional[ListNode]) -> int:
        # T -> O(N), S -> O(1)
        if head is None:
            return 0
        
        if head.next is None:
            return 1
        
        temp = head
        list_length = 0
        while temp:
            list_length += 1
            temp = temp.next
        # print(f"Length Of List: {list_length}")
        return list_length