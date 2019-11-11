N = int(input())
nums = []

for i in range(N):
    n, *s = map(int, input().split())
    nums.append(set(s))

K = int(input())
for k in range(K):
    s1, s2 = map(int, input().split())
    s1 = nums[s1-1]
    s2 = nums[s2-1]
    perc = len(s1 & s2) / len(s1 | s2) * 100
    print('{:.1f}%'.format(perc))