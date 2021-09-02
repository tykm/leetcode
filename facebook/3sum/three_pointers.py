def threesum(nums: list[int]) -> list[list[int]]:
    ans = []
    nums.sort()
    for i in range(len(num) - 2):
        curr = nums[i]
        left = i + 1
        right = len(nums) - 1


    return ans


nums = [-1,0,1,2,-1,-4]
#nums = [-1,0,1,2]

print(threesum(nums))
