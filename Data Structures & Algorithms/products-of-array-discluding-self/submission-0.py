class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product = 1
        res = [0] * len(nums)
        count = 0
        for num in nums:
            if num:
                product *= num
            else:
                count += 1
        if count > 1:
            return [0] * len(nums)

        for i, num in enumerate(nums):
            if count:
                if num == 0:
                    res[i] = product
                else:
                    res[i] = 0
            else:
                res[i] = int(product/ num)
        return res

            

        