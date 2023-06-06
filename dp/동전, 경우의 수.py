'''
https://www.acmicpc.net/problem/2293

- dp 중에서 경우의 수를 구하는 문제
    - 경우의 수에서 순서만 다른 경우 같은 경우로 계산하는 조건때문에 동전의 순서를 고정하는 로직에 주목
- 이게 왜 dp일까?
    - 문제를 분할해서 계산하고 저장할 수 있다.
'''

import sys


input = lambda: sys.stdin.readline().rstrip()
n, k = map(int, input().split())
coins = [coin for coin in [int(input()) for _ in range(n)] if coin <= k]
# dp table
dp = [0] * (k+1)

# 동전의 순서가 다른 경우를 배제하기 위해 동전의 순서를 고정
for coin in coins:
    dp[coin] += 1

    for won in range(1, k+1):
        if dp[won]:
            if won+coin <= k:
                dp[won+coin] += dp[won]
            else:
                break
print(dp[k])
