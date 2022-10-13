s = [int(i) for i in input().split()]
n = s[0]
m = s[1] % n
a = [int(i) for i in input().split()]
a1 = a[m:]
a2 = a[:m]
for i in a2:
    a1.append(i)
print(*a1)