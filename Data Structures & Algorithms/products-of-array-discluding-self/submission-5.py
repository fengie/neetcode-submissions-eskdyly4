class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1]* len(nums)
        left = [1]* len(nums)
        right = [1]* len(nums)
        
        product = 1

        for i in range(len(nums)):
            if i>=1:
                product *= nums[i-1]
            left[i] = product
        
        product = 1
        for i in range(len(nums)-1,-1,-1):
            if i<= len(nums)-2:
                product *= nums[i+1]
            right[i] = product

        for i in range(len(res)):
            res[i] = left[i] * right[i]

        return res
            