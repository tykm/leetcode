def roman_to_int(s: str) -> int:
    v = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    neg = False
    ans = 0
    n = len(s)
    for i in range(n):
        if neg:
            neg = False
            continue
        curr = s[i]
        if curr in ['I', 'X', 'C'] and i < n - 1:
            nxt = s[i + 1]
            if (curr == 'I' and nxt in ['V', 'X']) or \
                (curr == 'X' and nxt in ['L', 'C']) or \
                    (curr == 'C' and nxt in ['D', 'M']):
                neg = True
                ans += v[nxt] - v[curr]
                continue
        ans += v[curr]
        
        
    return ans



s = "III"
ss = 'IV'
sss = 'IX'
ssss = 'LVIII'
sssss = 'MCMXCIV'

print(roman_to_int(sssss))