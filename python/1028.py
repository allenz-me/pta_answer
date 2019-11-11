N, C = map(int, input().split())

data = []
for i in range(N):
    ins = input().split()
    # ins[2] = int(ins[2])
    data.append(ins)

if C == 1:
    data.sort(key=lambda x: int(x[0]))
elif C == 2:
    data.sort(key=lambda x: (x[1], int(x[0])))
else:
    data.sort(key=lambda x: (x[2], int(x[0])))

for d in data:
    print(' '.join(d))