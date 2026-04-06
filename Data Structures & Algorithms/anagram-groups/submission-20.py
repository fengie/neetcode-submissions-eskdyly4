class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = {}
        res = []

        for s in strs:
            sortedS = "".join(sorted(s.replace(" ", "")))

            if sortedS not in d:
                d[sortedS] = [s]
            else:
                d[sortedS].append(s)

        for key in d:
            res.append(d[key])

        return res