'''
https://www.acmicpc.net/problem/9251

- 다음 포스팅을 참고
    - https://velog.io/@emplam27/알고리즘-그림으로-알아보는-LCS-알고리즘-Longest-Common-Substring와-Longest-Common-Subsequence#longest-common-subsequence-substring
'''
A, B = input(), input()
A = " " + A
B = " " + B

len_a, len_b = len(A), len(B)
dp = [[0]*len_b for _ in range(len_a)]
for r in range(len_a):
    for c in range(len_b):
        if r == 0 or c == 0:
            continue

        if A[r] == B[c]:
            dp[r][c] = dp[r-1][c-1] + 1
        else:
            dp[r][c] = max(dp[r-1][c], dp[r][c-1])

# find max
result = max([max(row) for row in dp])
print(result)
