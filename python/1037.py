n1 = int(input())
nums1 = list(map(int, input().split()))

n2 = int(input())
nums2 = list(map(int, input().split()))

nag1 = sorted(filter(lambda x: x < 0, nums1))
nag2 = sorted(filter(lambda x: x < 0, nums2))

pos1 = sorted(filter(lambda x: x > 0, nums1))
pos2 = sorted(filter(lambda x: x > 0, nums2))

res = 0

for i in range(1, min(len(pos1), len(pos2))+1):
    res += pos1[-i] * pos2[-i]

for i in range(min(len(nag1), len(nag2))):
    res += nag1[i] * nag2[i]

print(res)