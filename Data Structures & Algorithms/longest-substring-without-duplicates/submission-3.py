class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        l = 0
        res= 0

        for i in range(len(s)):
            if s[i] in freq:
                l = max(freq[s[i]] + 1, l)

            freq[s[i]] = i
            res = max(res, i-l+ 1)

        return res