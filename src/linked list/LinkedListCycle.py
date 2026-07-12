# Problem: Linked List Cycle
# URL: https://leetcode.com/problems/linked-list-cycle/description/
# Date: 2026-07-12 16:59:03

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return head
        
        if head.next is None:
            return False
        
        # Approach 1, T(N), S(N) -> because of storing values in set()
        # visited = set()
        # curr = head
        # while curr:
        #     if curr in visited:
        #         return True
        #     visited.add(curr)
        #     curr = curr.next
        # return False

        # Approach 2, slow, fast method, T(N), S(1)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False