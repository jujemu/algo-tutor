'''
https://www.acmicpc.net/problem/2294

- 동전의 개수가 최소가 되게 만드는 문제
- 흔한 dp 문제이지만, 또 다른 풀이인 bfs를 활용하는 것도 참고
'''
import sys


input = lambda: sys.stdin.readline().rstrip()
n, k = map(int, input().split())
coins = set([coin for coin in [int(input()) for _ in range(n)] if coin <= k])

# dp 테이블
INF = 10_001
dp = [INF] * (k+1)

# 점화식: a(n+coin) = min(a(n)+1, a(n+coin))
for coin in coins:
    dp[coin] = 1
    for won in range(1, k+1):
        if dp[won] != INF:
            if won+coin > k:
                break
            dp[won+coin] = min(dp[won]+1, dp[won+coin])

print(dp[k] if dp[k] != INF else -1)

# bfs를 이용한 풀이
'''
import sys
from collections import deque

input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())
    dp = [0]*(k+1)
    coin = set()
    queue = deque()
    for _ in range(n):
        c = int(input())
        if c <= k:
            coin.add(c)
            queue.append((c, 2))
            dp[c] = 1
    while queue:
        i, cnt = queue.popleft()
        if i == k:
            break
        for c in coin:
            if i+c <= k and dp[i+c] == 0:
                dp[i+c] = cnt
                queue.append((i+c, cnt+1))
    print(dp[k] if dp[k] else -1)

solution()
'''