def multiply(num1: str, num2: str) -> str:
    sol = [0] * (len(num1) + len(num2))


    ans = ''
    for num in sol:
        if num == 0:
            continue
        ans += str(num)
    return ans


print(multiply('2','3'))