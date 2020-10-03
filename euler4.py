palindromelist = []
for i in range(143, 1000):
    for j in range(707, 1000):
        a = i * j
        if str(a) == str(a)[::-1] and a not in palindromelist:
            palindromelist.append(a)
palindromelist.sort()

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    palindromelist.append(n)
    palindromelist.sort()
    ind = palindromelist.index(n)
    ans = palindromelist[ind-1]
    palindromelist.remove(n)
    print(ans)