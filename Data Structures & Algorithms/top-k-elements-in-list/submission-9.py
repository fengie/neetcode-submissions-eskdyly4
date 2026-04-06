class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            d[n] = 1 + d.get(n,0)

        bucket = [[]for _ in range(len(nums) + 1)]

        for n in d:
            bucket[d[n]].append(n)

        res = []

        for i in range(len(bucket)-1,0,-1):
            for n in bucket[i]:
                res.append(n)

                if len(res) == k:
                    return res