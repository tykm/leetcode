class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            local = '';
            left = right = 0
            
            # Find location of @ to split string into domain and local
            # right = index of @
            for letter in email:
                if letter == "@":
                    break
                right += 1
                
            # Calculate the local string
            while left < right:
                if email[left] == '+':
                    break
                if email[left] == '.':
                    left += 1
                    continue
                local += email[left]
                left += 1
            
            # Calculate domain string
            domain = email[right:]
            unique.add(local + domain)
        return len(unique)