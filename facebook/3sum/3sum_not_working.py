def threesum(nums: list[int]) -> list[list[int]]:
    ones = {}
    twos = {}
    ans = []
    for i in range(len(nums)):
        num = nums[i]
        # store curr num in ones 
        ones[num] = i
        # store pairs in twos
        for j in range(i):
            prev = nums[j]
            sm = num + prev
            if sm not in twos:
                twos[sm] = [[i, j]]
                continue
            twos[sm].append([i, j])   
        # Check if negative of curr num in twos
        if -num in twos:
            print(num)
            print(twos[-num])
            for pair in twos[-num]:
                if i != pair[0] and i != pair[1] and pair[0] != pair[1]:
                    ans.append([i, pair[0], pair[1]])
    return ans


nums = [-1,0,1,2,-1,-4]
#nums = [-1,0,1,2]

print(threesum(nums))
