"""
https://www.acmicpc.net/problem/1717

"""
import sys
sys.setrecursionlimit(int(1e6)+1)

def find_parent(child):
    if parent[child] != child:
        parent[child] = find_parent(parent[child])
    return parent[child]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    parent[a] = b


input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())

parent = [i for i in range(n+1)]
for _ in range(m):
    cmd, a, b = map(int, input().split())

    if cmd == 0:
        union(a, b)
    else:
        a, b = find_parent(a), find_parent(b)
        print("YES" if a == b else "NO")
