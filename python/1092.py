s1, s2 = input(), input()

from collections import Counter
c1 = Counter(s1)
c2 = Counter(s2)

flag = True
for item in c2:
    if c2[item] > c1[item]:
        flag = False
        break

if flag:
    print("Yes", len(s1) - len(s2))
else:
    cnt = 0
    for item in c2:
        if c2[item] > c1[item]:
            cnt += c2[item] - c1[item]
    print("No", cnt)