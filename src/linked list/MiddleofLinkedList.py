# Problem: Middle of Linked List
# URL: https://www.datapathsala.com/dsa/middle-of-linked-list-basic?difficulty=basic
# Date: 2026-07-09 16:37:50

class Solution:
    def middleValue(self, head: Optional[ListNode]) -> int:

        # 1. Brute Force T - O(N) and S - O(1)
        # temp = head

        # length_of_list = 0
        # while temp:
        #     temp = temp.next
        #     length_of_list += 1

        # temp = head

        # for _ in range(length_of_list//2):
        #     temp = temp.next
        # return temp.val

        # 2. Optimal Approach, T -> O(N), S -> O(1)
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.val