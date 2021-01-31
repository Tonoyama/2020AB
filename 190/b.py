from typing import List, Dict

N, S, D = map(int, input().split())
magic: List[int] = [list(map(int, input().split())) for _ in range(N)]

count: int = 0

for i in range(N):
    if magic[i][0] >= S or magic[i][1] <= D:
        pass
    else:
        count += 1

if count >= 1:
    print("Yes")
else:
    print("No")