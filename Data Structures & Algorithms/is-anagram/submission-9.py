class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Use lists to keep track of each str's chars
        sCount = [0] * 26
        tCount = [0] * 26

        # populate lists
        for c in s:
            sCount[ord(c) - ord('a')] += 1

        for c in t:
            tCount[ord(c) - ord('a')] += 1

        # compare lists
        return sCount == tCount



