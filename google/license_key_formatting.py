# Took about 30 minutes with distractions

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "")
        length = len(s)
        foo = 0
        remainder = length % k
        k_ct = k
        key = ''
        
        
        # Loop thru existing s
        for letter in s:
            foo += 1
            letter = letter.upper()
            # Account for beginning odd number
            if remainder == 1:
                remainder -= 1
                key += letter
                if foo != length:
                    key += '-'
                continue
            elif remainder > 1:
                key += letter
                remainder -= 1
                continue
            
            # Now that beginning odds are over, time to do the rest regularly
            if k_ct == 1 and foo != length:
                k_ct = k
                key += letter + '-'
            else:
                key += letter
                k_ct -= 1
            
        return key
        