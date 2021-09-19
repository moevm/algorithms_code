def f_iter(n):
    res = 1
    while n > 1:
        res *= n
        n -= 1
    return res

def f_rec(n):
    if n == 1:
        return 1
    res = n * f_rec(n-1)
    return res

#f_rec(1000)
print(f_iter(2), f_iter(4))
print(f_rec(2), f_rec(4))
