class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sChr = [0] * 26
        tChr = [0] * 26

        for c in s:
            sChr[ord(c) - ord('a')] += 1
        
        for c in t:
            tChr[ord(c) - ord('a')] += 1

        return sChr == tChr