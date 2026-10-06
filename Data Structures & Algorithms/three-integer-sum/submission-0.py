class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        output = []

        for i in range(len(nums)-1):
            target = -(nums[i])
            left = i+1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    temp = [nums[left], nums[right], -target]
                    if temp not in output:
                        output.append(temp)
                    left += 1
                elif nums[left] + nums[right] <= target:
                    left+= 1
                else:
                    right-=1
        return output
                

        