n, k, m = map(int, input().split())

if k <= m:
    stops = min(m - k, k + n - (m + 1))
else:
    stops = min(k - m, m + n - (k + 1))

print(stops)