from typing import List, Dict

C: str = list(input())
es = all([e == C[0] for e in C[1:]]) if C else False

if es == True:
    print("Won")
else:
    print("Lost")