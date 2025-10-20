import math

p = int(input("Enter lower limit"))
q = int(input("Enter the upper limit"))
for i in range(p, q + 1):
    a = b = l = i
    c = 0
    while l > 0:
        d = l % 10
        c = c + 1
        l = l // 10
    x = a % (math.pow(10, (c // 2)))
    y = a // (math.pow(10, (c // 2)))
    s = x + y
    if (s * s) == b:
        print(i)