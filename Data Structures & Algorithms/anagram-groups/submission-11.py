class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = defaultdict(list)

        for s in strs:
            sortedS = ''.join(sorted(s))
            d[sortedS].append(s)

        res = []

        for key in d:
            res.append(d[key])

        return res



        