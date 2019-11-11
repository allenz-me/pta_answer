from statistics import median_low

n1, *nums1 = map(int, input().split())
n2, *nums2 = map(int, input().split())

nums = nums1 + nums2
print(median_low(nums))