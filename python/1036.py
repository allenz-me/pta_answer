n = int(input())
boys = []
girls = []

for i in range(n):
    temp = input().split()
    name, gender, ids, grade = temp
    if gender == 'F':
        girls.append(temp)
    else:
        boys.append(temp)
    
girls.sort(key=lambda x: int(x[3]))
boys.sort(key=lambda x: int(x[3]))
flag = True

if len(girls) == 0:
    print('Absent')
    flag = False
else:
    print(' '.join([girls[-1][0], girls[-1][2]]))

if len(boys) == 0:
    print('Absent')
    flag = False
else:
    print(' '.join([boys[0][0], boys[0][2]]))

if not flag:
    print('NA')
else:
    print(int(girls[-1][3]) - int(boys[0][3]))