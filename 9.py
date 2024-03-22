f, s, t = map(int, input().split())
highest= max(f,s,t)
lowest=min(f,s,t)
avarage = f+s+t-highest-lowest
print(highest, avarage, lowest)