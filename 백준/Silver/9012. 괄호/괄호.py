import sys
input = sys.stdin.readline
from collections import deque

def sol(arr):
    q = deque()
    for a in arr:
        if a == "(":
            q.append(a)
        elif a == ")":
            if len(q) != 0:
                q.pop()
            else:
                print("NO")
                return
    if len(q) == 0:
        print("YES")
    else:
        print("NO")

T = int(input())

for _ in range(T):
    arr = list(input())
    sol(arr)

