# Problem: Plus One
# URL: https://datapathsala.com/dsa/plus-one
# Date: 2026-07-23 23:11:06

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # 1. 
        # carry = False
        # for i in range(len(digits)-1, -1, -1):
        #     # print(digits[i])
        #     if digits[i] < 9:
        #         digits[i] += 1
        #         return digits
        #     else:
        #         digits[i] = 0
        #         carry = True
        #         continue
        # if carry:
        #     return [1] + digits
        # return digits

        # 2.
        # Time Complexity: O(n) in the worst case (O(1) in the best case).
        # Auxiliary Space Complexity: O(1), since no extra data structure is used during processing.
        # If counting the output array, the final case where all digits are 9 allocates a new list of size n+1, making the total space O(n).
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
            

obj = Solution()
nums = [9]
ret = obj.plusOne(digits=nums)
print(ret)