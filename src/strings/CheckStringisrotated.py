# Problem: Check String is rotated
# URL: https://www.datapathsala.com/dsa/is-rotation-string
# Date: 2026-07-14 14:08:34

class Solution:
    def __init__(self):
        pass


    def isRotation(self, s: str, goal: str) -> bool:
        # 1
        # Time Complexity: O(N^2) since generating N rotations and each comparison takes O(N) time.
        # Space Complexity: O(N) for the space needed to store each rotated string.
        # if len(s) != len(goal):
        #     return False
        
        # for i in range(len(s)):
        #     con = s[i:] + s[:i]
        #     if con == goal:
        #         return True
        # return False

        
        # 2
        # Time Complexity: O(N), because checking for a substring in s + s is linear in time.
        # Space Complexity: O(N) for the space needed to store the concatenated string s + s.
        if len(s) != len(goal):
            return False
        
        if goal in (s+s):
            return True
        return False


obj = Solution()
s = 'abcde'
goal = 'cedab'
ret = obj.isRotation(s=s, goal=goal)
print(ret)