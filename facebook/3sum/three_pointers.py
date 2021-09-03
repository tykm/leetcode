# Source: https://www.youtube.com/watch?v=erEHQO0xljc

def threesum(nums: list[int]) -> list[list[int]]:
    ans = []
    nums.sort()
    #print(nums)
    for i in range(len(nums) - 2):
        # If there are at least 2 nums left and anchor is duplicate with anchor + 1, skip anchor
        if i > 0 and nums[i] == nums[i - 1]:
            print(i)
            continue
        l = i + 1
        r = len(nums) - 1
        while l < r:
            sm = nums[i] + nums[l] + nums[r]
            if sm < 0:
                l += 1
            elif sm > 0:
                r -= 1
            else:   # sm = 0
                ans.append([nums[i], nums[l], nums[r]])
                # why l<r here?
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                # why l<r?
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
    
    
    return ans


nums = [-1,0,1,2,-1,-4]
nums = [0,0,0]

print(threesum(nums))
