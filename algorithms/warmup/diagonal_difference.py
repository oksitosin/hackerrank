n = int(raw_input())
a = []
for i in range(n):
   a_temp = map(int,raw_input().split())
   a.append(a_temp)

s1 = 0
s2 = 0

for j in range(n):
    s1 += a[j][j]
    s2 += a[j][(n-1)-j]
    
s = abs(s1 - s2)
print s