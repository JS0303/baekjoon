import sys
input = sys.stdin.readline # 빠른 입력 함수 사용
from collections import deque

n, m = map(int, input().split()) # 원소의 개수, 뽑아내는 횟수
d = deque([i for i in range(1, n + 1)]) # 1부터 N까지의 원소를 삽입
targets = list(map(int, input().split())) # 뽑아낼 원소 목록
cnt = 0 # 회전 연산 수행 횟수

for target in targets: # 뽑아낼 원소를 하나씩 확인하며
    index = d.index(target) # 덱에서 해당 원소의 위치를 찾기
    if index <= len(d) // 2: # 왼쪽으로 돌리는게 더 빠른 경우
        for i in range(index): # 회전 연산 반복 수행
            x = d.popleft()
            d.append(x)
            cnt += 1
    else: # 오른쪽으로 돌리는 게 더 빠른 경우
        for i in range(len(d) - index): # 회전 연산 반복 수행
            x = d.pop()
            d.appendleft(x)
            cnt += 1
    d.popleft() # 원소 꺼내기

print(cnt) # 결과 출력