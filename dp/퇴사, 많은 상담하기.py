'''
https://www.acmicpc.net/problem/14501

문제 풀이 과정
 - N이 작으니깐 브루트 포스로 풀 수 있겠네 -> 다른 방법 모색
 - 만약 상담 리스트가 있고 내가 고르는 거였으면 우선순위 큐로 풀었을 수 있겠네
 - 가장 높은 금액의 상담부터 진행하면 기간때문에 합이 최대가 아닐 수 있으니깐 그리디는 아니겠네
 - 일 별로 나눠서 dp로 풀자
'''
N = int(input())
tasks = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0]*(N+1)
for cur_day, (t, p) in enumerate(tasks):
    n_day = cur_day+t
    if n_day <= N:
        for i in range(n_day, N+1):
            dp[i] = max(dp[i], dp[cur_day]+p)
print(dp[-1])
