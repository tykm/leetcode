class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # { ['a','e','t']:["eat", "tea"], ...}
        anagrams = {}
        
        for word in strs:
            sort_word = tuple(sorted(word))
            if sort_word in anagrams:
                anagrams[sort_word].append(word)
            else:
                anagrams[sort_word] = [word]
        
        return anagrams.values()