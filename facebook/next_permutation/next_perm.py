def nextPermutation(nums: list[int]) -> None:
    # Start at the end.
    n = len(nums) - 1

    # Identify where the pivot location is:
    # Iterating backwards, the num before a forwards descent
    #[1,3,2]
    pivot = -1
    for i in range(n, 0, -1):
        if nums[i-1] < nums[i]:
            pivot = i-1
            break
    
    # Edge case: if list is fully descending
    if pivot == -1:
        nums.sort()
        #print(nums)
        return

    # Identify which num is being swapped:
    # The lowest number greater than the pivot value in the descent
    swap = None
    for i in range(pivot+1, n+1):
        if nums[i] > nums[pivot]:
            if swap == None:
                swap = i
            elif nums[i] < nums[swap]:
                swap = i

    # Swap the two 
    nums[swap], nums[pivot] = nums[pivot], nums[swap]

    # Sort the remaining
    nums[pivot+1:] = sorted(nums[pivot+1:])
    #print(nums)

nums = [1,3,2]
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
[1,2,4,3,5]
[1,2,4,5,3]
[1,2,5,3,4]
[1,2,5,4,3]
'''