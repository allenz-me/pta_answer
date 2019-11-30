s = input()

n = len(s)
if s[0] == 'P':
    p = [1]
else:
    p = [0]

for i in range(1, n):
    if s[i] == 'P':
        p.append(p[-1] + 1)
    else:
        p.append(p[-1])

a = [0]
for i in range(1, n):
    if s[i] == 'A':
        a.append(p[i-1] + a[-1])
    else:
        a.append(a[-1])

t = [0, 0]
for i in range(2, n):
    if s[i] == 'T':
        t.append((a[i-1] + t[-1]) % 1000000007)
    else:
        t.append(t[-1])

print(t[-1] % 1000000007)

