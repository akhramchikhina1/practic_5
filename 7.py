n, k, m = map(int, input().split())

if k <= m:
    stops = min(m - (k+1), k + n - (m + 1))
else:
    stops = min(k - (m+1), m + n - (k + 1))

print(stops)