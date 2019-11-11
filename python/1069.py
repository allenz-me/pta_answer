n = '{:0>4d}'.format(int(input()))

if all(i == n[0] for i in n):
    print('{} - {} = 0000'.format(n, n))
elif n == '6174':
    print('7641 - 1467 = 6174')
else:
    while n != '6174':
        n1 = int(''.join(sorted(str(n), reverse=True)))
        n2 = int(''.join(sorted(str(n))))
        n = '{:0>4d}'.format(n1 - n2)
        print('{} - {:0>4d} = {}'.format(n1, n2, n))
