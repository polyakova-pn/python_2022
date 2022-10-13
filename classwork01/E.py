s = input()
sl = 'qwertyuiopasdfghjklzxcvbnm'
sb = 'QWERTYUIOPASDFGHJKLZXCVBNM'
l = 0
b = 0
for i in s:
    if i in sl:
        l += 1
    elif i in sb:
        b += 1
print(b, l)