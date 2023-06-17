'''
https://www.acmicpc.net/problem/11055

- 수열의 원소는 여러 증가 부분 수열에 포함될 수 있다.
- 한 증가 부분 수열의 끝은 끝까지 가봐야안다.
- N이 너무 작아서 그냥 N^2로 들어갈까?

LIS -> 한번에 이해하기 힘든 유형
추가로 https://www.acmicpc.net/problem/2631 문제 풀어보기

참고
https://m.blog.naver.com/occidere/220793914361
'''
N = int(input())
sequence = [*map(int, input().split())]

d = [ele for ele in sequence]
for i in range(N):
    for j in range(i+1):
        if sequence[j] < sequence[i] and d[i] < d[j]+sequence[i]:
            d[i] = d[j]+sequence[i]
print(max(d))

# 더 직관적인 풀이
"""
input()
dp = [0] * 1001
for i in map(int, input().split()):
    dp[i] = max(dp[:i]) + i

print(max(dp))
"""