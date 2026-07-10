# Problem: Reverse a Linked List
# URL: https://www.datapathsala.com/dsa/reverse-linked-list-basic?difficulty=basic
# Date: 2026-07-10 20:14:17

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        # Approach 1, Using Stack, Not Optimal Solution O(N), S(N)
        # temp = head
        # stack = []

        # while temp:
        #     stack.append(temp.val)
        #     # print(temp.data)
        #     temp = temp.next
        # # print(stack)

        # temp = head
        # while temp:
        #     temp.val = stack.pop()
        #     temp = temp.next
        # return head


    # Approach 2, Optimal Approach, T -> O(N), S -> O(1)
        prev = None
        curr = head
        
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        head = prev
        return head