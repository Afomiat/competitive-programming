import bisect

n = int(input())
a = list(map(int, input().split()))
a.sort()
t = int(input())
for _ in range(t):
    x = int(input())
    print(bisect.bisect_right(a, x))