# Problem: Find smallest largest second smallest and largest element in array
# URL: https://www.datapathsala.com/dsa/find-second-largest
# Date: 2026-07-18 02:35:02

class Solution:
    def secondLargest(self, nums: list[int]) -> int:
        # 0. T(NlogN) because of sorting, S(1)
        # sort the array and get the second last element

        #########################

        # 1, T(N), S(1)
        # if len(nums) == 2:
        #     return min(nums)
        
        # maxi = 0
        # for i in nums:
        #     if i > maxi:
        #         maxi = i

        # second_maxi = 0
        # for i in nums:
        #     if i > second_maxi and i < maxi:
        #         second_maxi = i
        # return second_maxi

        #########################

        # 2.
        # O(N), O(1)
        first = second = float('-inf')

        for i in nums:
            if i > first:
                second = first
                first  = i
            elif i > second and i != first:
                second = i
        return second


    def secondLargest(nums: list[int]) -> int:
        # 0. T(NlogN) because of sorting, S(1)
        # sort the array and get the second  element
        
        # 1.
        # smallest = float('inf')
        # second_smallest = float('inf')
        # for i in nums:
        #     if i < smallest:
        #         smallest = i
        
        # for i in nums:
        #     if i < second_smallest and i != smallest:
        #         second_smallest = i
        # return second_smallest
    

        #2.
        first = second = float('inf')

        for i in nums:
            if i < first:
                second = first
                first = i
            elif i != first and i < second:
                second = i
        return second


    def smallest_element(self, nums: list[int]=None) -> int:
        # nums is empty
        if len(nums) < 1:
            return -1
        
        # nums is only one element
        if len(nums) == 1:
            return nums[0]
        
        # 1 sort and return 1st element of nums
        # nums.sort()
        # return nums[0]
        
        ###################

        # 2
        smallest = float('inf')

        for i in nums:
            if i < smallest:
                smallest = i
        return smallest
    

    def largest_element(self, nums: list[int]=None) -> int:
        # nums is empty
        if len(nums) < 1:
            return -1
        
        # nums is only one element
        if len(nums) == 1:
            return nums[0]
        
        # 1 sort and return 1st element of nums
        # nums.sort()
        # return nums[len(nums)-1]
        
        ###################

        # 2
        largest = float('-inf')

        for i in nums:
            if i > largest:
                largest = i
        return largest



obj = Solution()
nums = [4,5, 9,6,8]
# ret = obj.secondLargest(nums=nums)
ret = obj.largest_element(nums=nums)
print(ret)