'''
https://www.acmicpc.net/problem/23843

- 2^k로 이루어진 내림차순 배열은 a,b < c 일 때, 2^c >= 2^a + 2^b를 항상 만족한다.
- 우선순위 큐에서 추출한 값에서 더한 다음 우선순위 큐에 넣어도 위 조건에 의해 조건을 만족하며 연산할 수 있다.
'''
import heapq

N, M = map(int, input().split())
elec = list(map(int, input().split()))
elec.sort(reverse=True)
heap = []

for e in elec:
    if len(heap) < M:
        heapq.heappush(heap, e)
    else:
        outcome = heapq.heappop(heap)
        heapq.heappush(heap, outcome + e)

print(max(heap))