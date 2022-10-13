def dot_product(n, v1, v2):
    skp = 0
    for i in range(n):
        skp += v1[i] * v2[i]
    return skp