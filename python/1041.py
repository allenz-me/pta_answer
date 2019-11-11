from collections import Counter
N, *nums = map(int, input().split())
c = Counter(nums)
for i in nums:
    if c[i] == 1:
        print(i)
        break
else:
    print("None")