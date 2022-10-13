s = list(input().split())
sl = []
for i in s:
    if len(i) > 3:
        sl.append(i)
    else:
        w = ''
        sl.append(w)
slong = ' '.join(sl)
print(slong)