import sys # 빠른 입력 함수 사용
input = sys.stdin.readline
from collections import deque

# 트럭의 수, 다리의 길이, 최대 하중
n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))
trucks.reverse() # 트럭 배열
# 덱(deque)을 큐 목적으로 사용
q = deque()
total = 0 # 총 무게
t = 0 # 총 소요 시간

while True:
    # 모든 트럭을 처리한 경우 종료
    if len(trucks) == 0 and total == 0:
        break
    if len(q) == w: # 큐가 가득 찬 경우 꺼내기
        x = q.popleft()
        total -= x
    # 트럭이 들어갈 수 있는 경우
    if len(trucks) > 0 and total + trucks[-1] <= l:
        q.append(trucks[-1]) # 큐(다리)에 추가
        total += trucks[-1] # 무게 반영
        trucks.pop()
    else: # 트럭이 들어가지 못 한다면 0을 삽입
        q.append(0)
    t += 1

print(t)  # 총 소요시간 출력