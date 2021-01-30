from typing import List, Dict
import numpy as np

N: int = int(input())
moji: List[int] = [list(map(int, input().split())) for _ in range(N)]

result = 0
for row in moji:
    result += sum(row)

print(result)