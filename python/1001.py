a, b = map(int, input().split())

s = list(reversed(str(abs(a + b))))

res = []
for idx in range(len(s)):
    if idx > 0 and idx % 3 == 0:
        res.append(',')
    res.append(s[idx])
res = ''.join(reversed(res))
if a + b > 0:
    print(res)
elif a + b < 0:
    print('-', res, sep='')
else:
    print(0)