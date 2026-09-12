class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sChars = [0] * 26
        tChars = [0] * 26

        for c in s:
            sChars[ord(c) - ord('a')] += 1

        for c in t:
            tChars[ord(c) - ord('a')] += 1

        return sChars == tChars

        

        