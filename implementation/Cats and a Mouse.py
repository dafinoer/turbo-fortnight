t = int(input())

for _ in range(t):
    x, y, z = map(int, input().split(' '))
    print(['Cat A','Cat B', 'Mouse C'][0 if abs(x-z) < abs(y-z) else 1 if abs(x-z) > abs(y-z) else 2])

