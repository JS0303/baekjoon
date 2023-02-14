import sys
# 빠른 입력 함수 사용
input = sys.stdin.readline
import heapq

# 입력 소수의 개수 K와 구할 N번째 수
k, n = map(int, input().split())
data = list(map(int, input().split()))

heap = [] # 우선순위 큐(최소 힙)
visited = set() # 이미 처리된 수
max_value = max(data) # 최댓값

for x in data: # 초기 원소를 최소 힙에 삽입
    heapq.heappush(heap, x)

# N - 1개의 원소 꺼내기
for i in range(n - 1): # 힙에서 원소를 N번 꺼내기
    element = heapq.heappop(heap)
    for x in data:
        now = element * x # 곱한 결과 계산
        # 힙의 크기가 N 이상이고 힙의 최댓값보다 곱한 결과가 크다면
        if len(heap) >= n and max_value < now:
            continue
        if now not in visited: # 처음 방문하는 수라면
            heapq.heappush(heap, now)
            max_value = max(max_value, now)
            visited.add(now) # 방문 처리

# N번째 원소 꺼내기
print(heapq.heappop(heap))
