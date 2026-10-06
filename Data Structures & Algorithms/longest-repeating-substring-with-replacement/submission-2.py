class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
  
        max_freq = 0
        count = {}
        l = 0
        max_length = 0

        for r in range(len(s)):
            char = s[r]
            if char not in count:
                count[char] = 0
            count[char] += 1
            max_freq = max(max_freq, count[char])
            curr = r-l+1
            replacements = curr - max_freq
            if replacements > k: 
                count[s[l]]-= 1
                l += 1
                curr -= 1
            max_length = max(max_length, curr)
        return max_length





            
