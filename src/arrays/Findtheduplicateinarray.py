# Problem: Find the duplicate in array
# URL: https://www.datapathsala.com/dsa/find-duplicate-basic
# Date: 2026-07-13 11:17:18

class Solution:
    def __init__(self):
        pass


    def findDuplicate(self, nums: list[int]) -> int:
        # 1. Brute Force, 
        # TC -> O(N log N), where N is the size of the array. This is because we are sorting the array, which takes O(N log N) time.
        # Space Complexity: O(1), as we are sorting the array in-place and not using any additional data structures that grow with input size.

        # nums = sorted(nums)
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return nums[i]
        # return -1


        # 2. Better Approach
        # freq = {}

        # for i in nums:
        #     freq[i] = freq.get(i, 0) + 1
        
        # for i in freq:
        #     if freq.get(i) > 1:
        #         return i
        # return -1

        # Time Complexity: O(N), where N is the size of the array. This is because we are traversing the array once to build the frequency array.
        # Space Complexity: O(N), as we are using an additional frequency array of size N+1 to keep track of the occurrences of each element.
        freq = [0]*len(nums)
        for i in nums:
            if freq[i] == 0:
                freq[i] += 1
            else:
                return i
        return -1
        
        
        # visited = set()
        # for i in nums:
        #     if i in visited:
        #         # print(f"It's Dup: {i}")
        #         return i
        #         break
        #     visited.add(i)
        # return -1


obj = Solution()
nums = [1,3,4, 4, 2]
ret = obj.findDuplicate(nums=nums)
print(ret)