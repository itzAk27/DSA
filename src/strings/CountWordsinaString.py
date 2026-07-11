# Problem: Count Words in a String
# URL: https://www.datapathsala.com/dsa/count-words
# Date: 2026-07-11 18:36:29

class Solution:
    def __init__(self):
        pass

    def countWords(self, s: str) -> int:
        # Approach 1, T -> O(len(S) or N), S -> O(1)
        # spaces = 0
        # in_word = False

        # for ch in s:
        #     if ch != ' ':
        #         # condition used to count words after spaces
        #         # new word starts it will count
        #         if not in_word:
        #             spaces += 1
        #             in_word = True
        #     else:
        #         in_word = False
        # return spaces

        
        # Approach 2
        spaces = 0
        for i in range(len(s)):
            if s[i] != ' ':
                if i == 0 or s[i-1] == ' ':
                    spaces += 1
        return spaces


obj = Solution()
s = "   hello  world Akhtar   "
ret = obj.countWords(s=s)
print(ret)