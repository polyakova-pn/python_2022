def invert_array(a, n):
    b = []
    for el in reversed(a[:n]):
        b.append(el)
    return b