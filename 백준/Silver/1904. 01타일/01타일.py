import sys
input = sys.stdin.readline

N = int(input())
        
p = [0]*1000001
p[1] = 1
p[2] = 2
for i in range(3, N+1):
    p[i] = (p[i-1]+p[i-2])%15746

print(p[N])