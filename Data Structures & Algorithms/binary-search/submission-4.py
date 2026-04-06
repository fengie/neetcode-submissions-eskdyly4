class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums)-1
        left = 0

        while right >= left:
            middle = (right+left)//2

            if nums[middle]>target:
                right = middle-1
            
            elif nums[middle] < target:
                left = middle+1

            else:
                return middle

        return -1

