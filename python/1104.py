n = int(input())
nums = list(map(float, input().split()))

res = 0.0
for idx, v in enumerate(nums):
    res += v * (idx + 1) * (n - idx)
print("%.2f" % res)