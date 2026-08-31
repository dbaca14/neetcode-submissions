class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sSeen = [0] * 26
        tSeen = [0] * 26

        for char in s:
            sSeen[ord(char) - ord('a')] +=1

        for char in t:
            tSeen[ord(char) - ord('a')] +=1
            
        return sSeen == tSeen

