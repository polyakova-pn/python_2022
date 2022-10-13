a = list(input().split())
x = int(a[0])
y = int(a[1])
r = int(a[2])
if ((x ** 2 + y ** 2) ** 0.5) > r:
    print('NO')
else:
    print('YES')