class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(numbers):
            if num not in num_map:
                num_map[num] = i+1

        for num in num_map:
            second = target - num
            if second in num_map:
                return [num_map[num], num_map[second]]

        