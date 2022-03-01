def f(num):
    return (num << 1) % 256


n = 91
n = f(n)
n = f(n)
n = n - 1
n = f(n)
n = f(n)
n = n - 1

print(n)