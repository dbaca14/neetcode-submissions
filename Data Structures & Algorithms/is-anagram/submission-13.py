class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sSeen = [0] * 26
        tSeen = [0] * 26

        for c in s:
            sSeen[ord(c) - ord('a')] += 1

        for c in t:
            tSeen[ord(c) - ord('a')] += 1

        return sSeen == tSeen