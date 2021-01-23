from typing import List, Dict

H, W = (int(x) for x in input().split())
block: List[str] = [input() for i in range(H)]

block: str = ' '.join(block)
block: List[str] = block.split()
block: List[int] = list(map(int, block))
delete_block: List[int] = list(map(lambda x: x-min(block), block))
delete_block: int = sum(delete_block)

print(delete_block)