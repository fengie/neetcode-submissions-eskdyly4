class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        freq = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference not in freq:
                freq[difference] = i
            
        for i in range(len(nums)):
            if nums[i] in freq and freq[nums[i]] != i:
                if i < freq[nums[i]]:
                    return [i,freq[nums[i]]]
                else:
                    return [freq[nums[i]], i]