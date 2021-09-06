def nextPermutation(nums: list[int]) -> None:
    i = len(nums) - 1       # The last index, the anchor pointer
    j = i - 1               # The moving pointer
    
    while True:
        if nums[i] > nums[j]:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            break
        j += 1
    print(nums)

nums = [1,2,3]
nextPermutation(nums)



'''
Input: nums = [1,2,3]
Output: [1,3,2]

Input: nums = [3,2,1]
Output: [1,2,3]

Input: nums = [1,1,5]
Output: [1,5,1]

Input: nums = [1]
Output: [1]

Input: nums = [1,3,2]
Output: [2,1,3]

Let's say:
[1,2,3,4,5]
[1,2,3,5,4]
'''