n = int(input())
l = list(map(int,input().split()))
m = max(l)
count=0
for i in range(len(l)):
    if l[i] is m:
        count+=1
print (count)
