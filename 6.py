f, s, t = map(int, input().split())
count=0
if f==s:
    count+=1
if f==t:
    count+=1
if s==t:
    count+=1
print(count)