# Problem: Balanced Parentheses
# URL: https://datapathsala.com/dsa/check-balanced-parens
# Date: 2026-07-19 20:45:25

class Solution:
    def isBalanced(self, s: str) -> bool:
        # 1.
        # TC -> O(N)
        # SC -> O(1)
        # It only works in backets is '()'
        # if not s:
        #     return True
        
        # cnt = 0
        # for c in s:
        #     if c == '(':
        #         cnt += 1
        #     elif c == ')':
        #         cnt -= 1
        #         if cnt < 0:
        #             return False
        # return (cnt == 0) 

        # 2.
        # Time Complexity: O(n). Single for loop used
        # Space Complexity: O(N). Stack space
        # stack = list()
        if not s:
            return True
        stack = []
        for i in s:
            # print(f"{i} - {stack}")
            if i in "([{":
                stack.append(i)
            elif not stack:
                return False
            else:
                ch = stack.pop()
                if  ( ch == '(' and i == ')' ) or \
                    ( ch == '[' and i == ']' ) or\
                    ( ch == '{' and i == '}' ):
                    continue
                else:
                    return False
        return not stack # Note to handle cases like '()['