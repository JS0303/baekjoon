import sys # 빠른 입력 함수 사용
input = sys.stdin.readline
from collections import deque

n = int(input()) # 원소의 개수 N
# 전체 원소 리스트
arr = list(map(int, input().split()))
d = deque() # 덱(deque) 초기화
for i in range(n):
	# (수, 번호) 형태로 원소를 삽입
	d.append((arr[i], i+1))
result = [] # 결과 배열
current, index = d.popleft() # 원소 추출
result.append(index)
for i in range(n-1): # 원소를 모두 꺼내기
	if current > 0: # 양수라면
		# current - 1번 "왼쪽으로 돌리기" 수행
		for j in range(current -1):
			x = d. popleft()
			d.append(x)
	else: # 음수라면 (0은 없음)
		# |current|번 "오른쪽으로 돌리기" 수행
		for j in range(-current):
			x = d.pop()
			d.appendleft(x)
	# 원소 추출
	current, index = d.popleft()
	result.append(index)

for x in result: # 결과 출력
	print(x, end=' ')