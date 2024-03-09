import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    stack = []
    string = input().strip()
    string += str(" ")
    for s in string:
        if s != " ": 
            stack.append(s)
        else:
            while stack:
                print(stack.pop(), end="")
            print(" ", end="")
    print()
            