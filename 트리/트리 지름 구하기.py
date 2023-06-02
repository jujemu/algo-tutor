'''
https://www.acmicpc.net/problem/1967

트리의 지름을 구하기 위해서는
    - 한 노드에서 가장 먼 노드를 구하고
    - 구한 노드로부터 가장 먼 노드를 양 끝점에 놓아 연결한 선이 트리의 지름이 된다.
'''
import sys
sys.setrecursionlimit(10_001)


def dfs(cur, acc):
    for adj, d in graph[cur]:
        if distance[adj] == -1:
            distance[adj] = acc + d
            dfs(adj, acc+d)


input = lambda: sys.stdin.readline().rstrip()
n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    n_1, n_2, d = map(int, input().split())
    graph[n_1].append([n_2, d])
    graph[n_2].append([n_1, d])

distance = [-1] * (n + 1)
distance[1] = 0
dfs(1, 0)

start = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[start] = 0
dfs(start, 0)

print(max(distance))