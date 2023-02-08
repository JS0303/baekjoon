import sys
input = sys.stdin.readline # 빠른 입력 함수 사용

n = int(input()) # 명령의 수를 입력
stack = [] # 스택(stack) 초기화

for _ in range(n):
    command = input().strip().split(' ') # 공백 기준 구분
    if command[0] == 'push': # 원소 삽입
        stack.append(int(command[1]))
    elif command[0] == 'pop': # 원소 삭제
        if len(stack) == 0: print(-1) # 원소가 없는 경우
        else: print(stack.pop())
    elif command[0] == 'size': # 원소의 개수 출력
        print(len(stack))
    elif command[0] == 'empty': # 스택이 비어있는지 출력
        if len(stack) == 0: print(1) # 원소가 없는 경우
        else: print(0)
    elif command[0] == 'top': # 최상단 원소 출력
        if len(stack) == 0: print(-1) # 원소가 없는 경우
        else: print(stack[-1])