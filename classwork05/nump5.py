import numpy as np
np.random

print(np.random.seed(1))


a = np.random.rand(120)
print(*a)


suma = a.sum()
stda = a.std()
meana = a.mean()
print('sum', suma)
print('std', stda)
print('mean', meana)


amat = a.reshape(12, 10)
print(amat)


print('amat sum str', *amat.sum(axis=1))
print('amat mean str', *amat.mean(axis=1))
print('amat std str', *amat.std(axis=1))
print('amat sum col', *amat.sum(axis=0))
print('amat mean col', *amat.mean(axis=0))
print('amat std col', *amat.std(axis=0))


print('min in col', *amat.min(axis=0))
print('max in col', *amat.max(axis=0))


print('index min in str', *amat.argmin(axis=1))
print('index max in str', *amat.argmax(axis=1))