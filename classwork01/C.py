a = list(input().split())
ls = 1000
lb = 0
for i in a:
    if len(i) > lb:
        lb = len(i)
    if len(i) < ls:
        ls = len(i)
print(ls, lb)