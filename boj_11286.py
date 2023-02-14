import sys
input = sys.stdin.readline # 빠른 입력 함수 사용
import heapq

heap = []
n = int(input()) # 연산의 개수 N
for i in range(n):
    x = int(input()) # 연산 정보
    if x == 0: # 삭제 연산이라면
        if len(heap) == 0: # 힙이 비어있는 경우
            print(0)
        else: # 힙이 비어있지 않은 경우
            absolute, original = heapq.heappop(heap)
            print(original)
    else: # 삽입 연산이라면
        heapq.heappush(heap, (abs(x), x))