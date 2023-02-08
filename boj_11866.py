import sys # 빠른 입력 함수 사용
input = sys.stdin.readline
from collections import deque

# 원소의 개수 N과 제거할 간격 K 입력
n, k = map(int, input().split())
# 1부터 N까지의 원소를 삽입
d = deque([i for i in range(1, n+1)])
result = [] # 결과 배열

# N개의 원소를 모두 꺼내기
for i in range(n):
	# K - 1번 "왼쪽으로 돌리기" 수행
	for i in range(k-1):
		x = d.popleft()
		d.append(x)
	x = d.popleft() # 원소 꺼내기
	result.append(x)

# 정답 출력
print('<', end='')
for i in range(len(result)):
	if i < len(result) -1:
		print(result[i], end=', ')
	else: # 마지막 원소
		print(result[i], end='')
print('>')