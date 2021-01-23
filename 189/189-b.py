from typing import List, Dict

N, X = map(int, input().split())

alcohol = 0
count = 0

for i in range(N):
    v, p = map(int, input().split())
    alcohol += v * p
    if alcohol > X * 100:
        print(i+1)
        exit()

print(-1)