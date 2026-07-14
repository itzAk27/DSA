# Problem: Max Consecutive Ones
# URL: https://www.datapathsala.com/dsa/max-consecutive-ones
# Date: 2026-07-14 13:13:31

class Solution:
    def __init__(self):
        pass


    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        if len(nums) == 1 and nums[0] == 1:
            return 1

        # 1.
        # old_cnt = 0
        # max_ones = 0
        # for i in nums:
        #     if i == 1:
        #         old_cnt += 1
        #     elif old_cnt > max_ones:
        #         max_ones = old_cnt
        #         old_cnt = i
        # if old_cnt > max_ones:
        #     return old_cnt
        # return max_ones
    
        # T -> O(N), S -> O(1)
        max_count = 0
        cnt = 0
        for i in nums:
            if i == 1:
                cnt += 1
                if cnt > max_count:
                    max_count = cnt
            else:
                cnt = 0
        return max_count
                

obj = Solution()
nums = [1,1,1,1, 0,0, 1,1,1,1,1,1]
ret = obj.findMaxConsecutiveOnes(nums=nums)
print(ret)