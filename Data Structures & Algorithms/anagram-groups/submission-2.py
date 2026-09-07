class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # creates a dict with default values as lists
        # prevents KeyError exception when trying to modify missing keys

        anagrams = defaultdict(list)

        for i, s in enumerate(strs):
            # List keeps track of characters
            charCount = [0] * 26

            # Populate list
            for c in s:
                charCount[ord(c) - ord('a')] += 1
            
            # Append char tracker list to dict as key and string as value
            # turn charCount into immutable to prevent exception
            anagrams[tuple(charCount)].append(s)

        # Turn dicitonary into list as per expected return type 
        return list(anagrams.values())



            

            
