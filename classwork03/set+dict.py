print()
print('ex0')
A = set('bqlpzlkwehrlulsdhfliuywemrlkjhsdlfjhlzxcovt')
B = set('zmxcvnboaiyerjhbziuxdytvasenbriutsdvinjhgik')
print(A-B)

print()
print('ex1')
a = input().split()
print(set(a[0]) & set(a[1]) & set(a[2]))

print()
print('ex2')
a = input().split()
b = set(a[0])
for i in range(len(a)):
    b = b & set(a[i])
print(b)

print()
print('ex4')
e = {i: chr(i) for i in range(97, 123)}
print(e)

print()
print('ex5')
d = {i: chr(i + 97) for i in range(97, 123)}
print(d)

print()
print('ex6')
d = {i: chr(i + 97) for i in range(26)}
a = input()
b = 0
for i in range(26):
    if set(d[i]) & set(a) == set(d[i]):
        b = b + i + 1
print(b)

print()
print('ex7')
n = int(input())
d = dict()
for i in range(n):
    s = input().split()
    d[s[0]] = s[1]
s = input()
if s in set(d.keys()):
    print(d[s])
else:
    for i in range(n):
        if d[list(d.keys())[i]] == s:
            print(list(d.keys())[i])

print()
print('ex8')
a = input().translate({ord(i): None for i in '1234567890 '})
n = len(a)
while len(a) > 0:
    print(a[0], "-", a.count(a[0]) / n)
    a = a.translate({ord(a[0]): None})