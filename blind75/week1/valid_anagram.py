class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        zeroes = 0
        for letter in s:
            if letter not in counts:
                counts[letter] = 1
                zeroes += 1
            else:
                counts[letter] += 1
        for letter in t:
            if letter not in counts:
                return False
            else:
                counts[letter] -= 1
                if counts[letter] == 0:
                    zeroes -= 1
        return zeroes == 0