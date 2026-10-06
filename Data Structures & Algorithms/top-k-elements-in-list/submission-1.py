class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        
        arr = []

        for num, c in freq.items():
            arr.append([c, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])

        return res
        
        
            