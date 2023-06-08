'''
https://www.acmicpc.net/problem/5557

- dp 2차원 테이블
- 숫자를 추가할 때마다 스냅샷을 찍는다는 생각으로 이해
- 2차원으로 해야하는 이유는 21크기의 배열에서 각 값이 현재 진행하고 있는 모든 숫자를 포함해야하기 때문
'''
N = int(input())
numbers = list(map(int, input().split()))
numbers, target = numbers[:-1], numbers[-1]

dp = [[0]*21 for _ in range(N-1)]
dp[0][numbers[0]] = 1
for r in range(N-2):
    for c in range(21):
        if dp[r][c]:
            n_c = c+numbers[r+1]
            if n_c <= 20:
                dp[r+1][n_c] += dp[r][c]

            n_c = c - numbers[r+1]
            if n_c >= 0:
                dp[r + 1][n_c] += dp[r][c]

print(dp[-1][target])
