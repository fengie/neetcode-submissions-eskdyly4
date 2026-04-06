class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = {}

        for s in strs:
            sortedS = ''.join(sorted(s))

            if sortedS not in d:
                d[sortedS] = [s]

            else: 
                d[sortedS].append(s)

        res = []

        for key in d:
            res.append(d[key])

        return res



        