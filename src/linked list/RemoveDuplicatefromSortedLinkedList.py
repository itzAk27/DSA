# Problem: Remove Duplicate from Sorted Linked List
# URL: https://www.datapathsala.com/dsa/remove-duplicates-sorted-list?difficulty=basic
# Date: 2026-07-11 21:27:07

def deleteDuplicates(self):
        if self.head is None:
            return self.head

        if self.head.next is None:
            return self.head 

        # Approach 1
        # prev = self.head
        # curr = self.head.next

        # while curr:
        #     if curr.data == prev.data:
        #         prev.next = curr.next
        #         curr = curr.next
        #     else:
        #         prev = curr
        #         curr = curr.next
        # self.display()


        # Approach 2, O(N), S(1)
        curr = self.head
        while curr and curr.next:
            if curr.data == curr.next.data:
                curr.next = curr.next.next
            else:
                curr = curr.next
        self.display()