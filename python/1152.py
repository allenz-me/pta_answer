def isprime(p:int) -> bool:
    if p == 2:
        return True
    elif p % 2 == 0 or p == 1:
        return False
    for i in range(3, int(pow(p, 1/2)) + 3, 2):
        if p % i == 0:
            return False
    return True


L, K = map(int, input().split())

s = input()
for i in range(len(s)-K+1):
    p = s[i:i+K]
    if isprime(int(p)):
        print(p)
        break
else:
    print('404')