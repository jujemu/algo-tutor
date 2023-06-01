'''
https://www.acmicpc.net/problem/1202

- 배열이 정렬된 채로 추가나 추출해야할 때 사용한다.
- 시행이 반복될 때마다 추출하는 것이 아니라 조건을 만족하는 모든 원소를 한번에 추출하고 추가해서 최적화할 수 있다.
'''
import heapq
import sys


input = lambda: sys.stdin.readline().rstrip()
N, K = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(N)]
backs = sorted([int(input()) for _ in range(K)])

heapq.heapify(jewels)

result = 0
tmp = []
for back in backs:
    while jewels and back >= jewels[0][0]:
        heapq.heappush(tmp, -heapq.heappop(jewels)[1])
    if tmp:
        result -= heapq.heappop(tmp)
print(result)
