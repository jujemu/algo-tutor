'''
https://www.acmicpc.net/problem/12865

- 이 문제와 퇴사2 문제를 비교하여 학습한다.
- 퇴사2에서는 순회하는 날에 정해진 스케쥴만 실행할 수 있지만
    - 평범한 배낭에서는 물건을 선택해서 넣을 수 있다.
    - 이 차이가 2차원으로 구성해야하는 이유가 된다.
'''
# 정렬할 때, 오름차순이냐, 내림차순이냐가 중요하다.
# 오름차순으로 정렬할 경우, 반복문의 w가 점점 커지기 때문에 앞에서 계산한 작은 무게의 아이템이 사라지게 된다.
# 따라서 내림차순으로 정렬해야 올바른 정답을 얻을 수 있다.
N, K = map(int, input().split())
items = [[]] + sorted([tuple(map(int, input().split())) for _ in range(N)], reverse=True)

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
for r in range(1, N+1):
    w, v = items[r]
    for c in range(w, K+1):
        dp[r][c] = max(dp[r-1][c], dp[r-1][c-w]+v)
print(dp[-1][-1])

# 위 처럼 items를 정렬하지 않으려면 인덱스 에러가 나지 않도록 조건을 달면 된다.
N, K = map(int, input().split())
items = [[]] + [tuple(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
for r in range(1, N+1):
    w, v = items[r]
    for c in range(1, K+1):
        if c-w >= 0:
            dp[r][c] = max(dp[r-1][c], dp[r-1][c-w]+v)
        else:
            dp[r][c] = dp[r-1][c]
print(dp[-1][-1])
