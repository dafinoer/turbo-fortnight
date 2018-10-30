n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
a = ar.count(1)
b = ar.count(2)
c = ar.count(3)
d = ar.count(4)
e = ar.count(5)
li=[a,b,c,d,e]
print(1+li.index(max(li)))
