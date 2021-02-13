from typing import List, Dict

T = int(input())
case: List[int] = [list(map(int, input().split())) for _ in range(T)]

for i in range(T):
    R: List[int] = case[i][1]
    L: List[int] = case[i][0]
    for j in range(R):
        print(j)