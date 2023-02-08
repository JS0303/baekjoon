import sys
input = sys.stdin.readline # 빠른 입력 함수 사용

k = int(input()) # 수의 개수
stack = [] # 스택(stack) 초기화

for _ in range(k):
    x = int(input()) # 하나씩 수 입력
    if x == 0: # 값이 0인 경우 가장 최근 수 제거
        stack.pop()
    else: # 스택에 해당 수 삽입
        stack.append(x)

print(sum(stack))