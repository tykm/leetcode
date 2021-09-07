def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums2[j] >= nums1[i] and nums2[j] < nums1[i+1]:
                nums1[i+1:] = [nums2[j]] + nums1[i+2:m+n-i]

                



nums1 = [1,2,3,0,0,0]
m = 3 
nums2 = [2,5,6]
n = 3


merge(nums1, m, nums2, n)