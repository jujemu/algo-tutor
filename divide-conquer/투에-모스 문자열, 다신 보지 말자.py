'''
https://www.acmicpc.net/problem/18222

쉽다.
'''
k = int(input())

cur = k-1
i = 0
while True:
    if cur == 0:
        break
    p = int(len(bin(cur)[2:]))-1
    cur = cur-2**p
    i += 1
print(1 if i%2 else 0)
