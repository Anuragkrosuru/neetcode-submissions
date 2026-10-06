import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)   # same as unordered_map<int,int>
        maxheap = []
        
        # Push (-freq, num) so largest freq comes out first
        for num, freq in frequency.items():
            heapq.heappush(maxheap, (-freq, num))
        
        ans = []
        for _ in range(k):
            freq, num = heapq.heappop(maxheap)
            ans.append(num)
        
        return ans