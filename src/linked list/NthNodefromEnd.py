# Problem: Nth Node from End
# URL: https://www.datapathsala.com/dsa/nth-from-end?difficulty=basic
# Date: 2026-07-10 23:20:36

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nthFromEnd(self, head: Optional[ListNode], n: int) -> int:
        # Approach 1
        # prev = head
        # curr = head

        # cnt = 0
        # while curr:
        #     if cnt >= n:
        #         prev = prev.next
        #     curr = curr.next
        #     cnt += 1
        # return prev.val

        # Appraoch 2, T -> O(N), S -> O(1)
        slow = fast = head
        for _ in range(n):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        # print(slow.data)
        return slow.val