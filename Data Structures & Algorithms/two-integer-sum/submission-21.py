class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}


        for i in range(len(nums)):
            d[nums[i]] = i

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in d and d[difference] != i:
                if d[difference] > i:
                    return[i,d[difference]]

                return [d[difference],i]
                
                