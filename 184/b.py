from typing import List, Dict

N, X = (int(x) for x in input().split())
S: List[str] = list(input())

for i in range(N):
    if S[i] == 'o':
        X += 1
    elif X:
        X -= 1

print(X)