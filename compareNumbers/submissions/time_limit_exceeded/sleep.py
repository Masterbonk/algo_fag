import time

a = int(input())
b = int(input())
c = int(input())
for _ in range(10**10):
    a = a + b - b
print(*sorted((a,b,c)))
