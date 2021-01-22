from typing import List, Dict

price: int = int(input())
A, B, C = list(map(int, input().split()))
staple_food: List[int] = list(map(int, input().split()))
main_dish: List[int] = list(map(int, input().split()))
side_dish: List[int] = list(map(int, input().split()))

count: int = 0

for i in staple_food:
    for j in main_dish:
        for k in side_dish:
            if sum([i, j, k]) == price:
                count += 1

print(count)
