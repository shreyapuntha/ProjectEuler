import math

t = int(input().strip())
for a0 in range(t):
    ans = False
    n = int(input().strip())
    a = n
    while n % 2 == 0:
        n = n / 2
        if n == 1:
            print(2)
            ans = True
    if ans == False:
        for i in range(2, int(math.sqrt(n) + 1), 3):
            if n % i == 0:
                n = n / i

