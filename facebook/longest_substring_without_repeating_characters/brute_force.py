# n^2

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        # For letter in s
        for i in range(len(s)):
            # Make string and found array
            str = s[i]
            found = [s[i]]
            # For every letter after curr letter, check if it's already in str
            # If so, set max to len(str) and break
            # Else, add letter to str and found
            for j in range(i+1, len(s)):
                if s[j] in found:
                    #print(found)
                    #print(s[j])
                    break
                found += s[j]
                str += s[j]
            if len(str) > max:
                max = len(str)
        return max