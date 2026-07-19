# Problem: String Compression
# URL: https://datapathsala.com/dsa/basic-string-compression
# Date: 2026-07-19 22:06:12

class Solution:
    def compress(self, s: str) -> str:
        # freq = {}
        # for i in s:
        #     # print(i)
        #     freq[i] = freq.get(i, 0) + 1

        # # print(freq)

        # ret = ''
        # for i, j in freq.items():
        #     # print(f"{i} - {j}")
        #     ret = ret + i + str(j)

        # # print(ret)

        # if len(ret) < len(s):
        #     # print(ret)
        #     return ret
        # # print(s)
        # return s

        # TC -> O(N)
        # SC -> O(N)
        if not s:
            return s
        
        ret = []
        count = 1

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                ret.append(s[i-1] + str(count))
                count = 1
        ret.append(s[len(s)-1] + str(count))
        compress = ''.join(ret)
        return compress if len(compress) < len(s) else s