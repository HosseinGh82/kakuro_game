def f(n):
    s = 0
    while n > 0:
        s = s + n % 10
        n = n // 10
    if n < 10:
        return s
    else:
        return f(s)


n = int(input())
print(f(n))

