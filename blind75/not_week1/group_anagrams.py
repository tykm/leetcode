class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # letters stores a count of each letter
        letters = [0] * 26
        # words stores the counts of anagrams
        # { (0, 1, 0, 2...): ["eat", "tea"] }
        words = {}
        
        
        for word in strs:
            letters = [0] * 26
            # Iterate through word and store letter count
            for letter in word:
                letter_value = ord(letter) - ord('a')
                letters[letter_value] += 1
            letters = tuple(letters)
            if letters not in words:
                words[letters] = [word]
            else:
                words[letters].append(word)
                
        return words.values()