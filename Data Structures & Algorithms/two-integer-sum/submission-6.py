class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = {}

        for i, num in enumerate(nums):
            compliment = target - num

            if compliment in map1:
                return [map1[compliment], i]  
            else:
                map1[num] = i
        

        
