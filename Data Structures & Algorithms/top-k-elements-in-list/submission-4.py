class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}

        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] = d[n] + 1

        res = []
        
        max = 'x'
        d[max] = 0

        for i in range(k):
            max = 'x'
            for key in d:
                if d[max] < d[key]:
                    max = key
            res.append(max)
            del d[max]
        
        return res

                
                    