class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sd = {}
        td = {}

        for c in s:
            if c not in sd:
                sd[c] = 1
            else:
                sd[c] = sd[c] +1

        for c in t:
            if c not in td:
                td[c] = 1
            else:
                td[c] = td[c] +1

        return sd == td