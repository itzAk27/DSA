# Problem: Subsequence String
# URL: https://www.datapathsala.com/dsa/is-subsequence-basic
# Date: 2026-07-18 11:43:02

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # TC -> O(MIN(s,t)), SC -> O(1)
        i = j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)