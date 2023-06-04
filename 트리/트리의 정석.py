'''
https://www.acmicpc.net/problem/15681

- dfs를 통해 자식 노드로 구현하는 트리 구현
- dfs를 진행하면서 leaf에서 root로 향하는 경로를 찾을 수 있다.
'''
import sys


def solution():
    input = sys.stdin.readline

    N, R, Q = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    dp = [1]*(N+1)
    for _ in range(N-1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    stack = [R]
    path = []
    while stack:
        idx = stack.pop()
        for i in graph[idx]:
            graph[i].remove(idx)
            stack.append(i)
            path.append((idx, i))
    for u, v in path[::-1]:
        dp[u] += dp[v]
    for _ in range(Q):
        u = int(input())
        print(dp[u])

solution()
