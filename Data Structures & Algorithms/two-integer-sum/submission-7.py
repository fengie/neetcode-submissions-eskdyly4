class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        freq = {}

        for i, x in enumerate(nums):
            difference = target - nums[i]

            if difference in freq:
                return [freq[difference], i]

            freq[x] = i