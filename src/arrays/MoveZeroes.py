# Problem: Move Zeroes
# URL: https://datapathsala.com/dsa/move-zeroes
# Date: 2026-07-21 00:18:35

class Solution:
    def moveZeroes(self, nums: list[int]) -> list[int]:
        # Time Complexity: O(N), we can move all zeroes to end in linear time.
        # Space Complexity: O(N), additional space used for temporary array.
        # temp = [0]*len(nums)
        # print(temp)
        # index = 0
        # for i in nums:
        #     if i != 0:
        #         # temp.append(i)
        #         temp[index] = i
        #         index += 1

        # # print(temp)
        # return temp
        # # print(nums)

        # for i in range(len(temp)):
        #     nums[i] = temp[i]
        # return nums


        # 2. IMP**
        # T(N), S(1)
        # pos = 0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         print(nums)
        #         nums[pos], nums[i] = nums[i], nums[pos]
        #         pos += 1
        # return nums


        # 3.
        # optimal sol
        # Time Complexity: O(N), we can move all zeroes to end in linear time.
        # Space Complexity: O(1), constant additional space is used.
        j = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i
                break

        # print(j)
        
        if j == -1:
            return j
        
        for i in range(j+1, len(nums)):
            # print(nums[i])
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums
        

obj = Solution()
nums = [0,2,3, 0, 4,3,2,1]
ret = obj.moveZeroes(nums=nums)
print(ret)