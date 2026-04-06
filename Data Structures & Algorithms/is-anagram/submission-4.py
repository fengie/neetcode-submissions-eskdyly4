class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        freq = {}
        
        for x in s:
            freq[x] = freq.get(x,0) + 1

        for x in t:
            if x not in freq:
                return False

            freq[x] -= 1

            if freq[x] < 0:
                return False

        return True

        