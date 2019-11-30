n = int(input())
ns = [input() for _ in range(n)]
res = []

for i in ns:
    a, b = i.split()
    if '1' in b or 'l' in b or 'O' in b or '0' in b:
        b = b.replace('1', '@').replace('l', 'L').replace('O', 'o').replace('0', '%')
        res.append(' '.join([a, b]))

if len(res) == 0:
    if n == 1:
        print(f'There is 1 account and no account is modified')
    else:
        print(f'There are {n} accounts and no account is modified')

else:
    print(len(res))
    for r in res:
        print(r)
