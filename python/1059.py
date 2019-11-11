N = int(input())
n = N
sqrt = int(pow(N, 0.5)) + 5
res = {}
for i in range(2, sqrt):
    while N % i == 0:
        res[i] = res.get(i, 0) + 1
        N //= i
if N > 1:
    res[N] = 1

print(n, end='')
# keng die de bian jie qing kuang
if n == 1:
    print('=1',end='')
for idx, k in enumerate(sorted(res.keys())):
    if idx == 0:
        print('=', end='')
    else:
        print('*', end='')
    if res[k] > 1:
        print('{}^{}'.format(k, res[k]), end='')
    else:
        print(k, end='')
