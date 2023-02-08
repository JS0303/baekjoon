# n = int(input())

# count = 1
# stack = []
# result = []

# for i in range(1, n+1):
#     data = int(input())
#     while count <= data:
#         stack.append(count)
#         result.append('+')
#         count += 1
#     if stack[-1] == data:
#         stack.pop()
#         result.append('-')
#     else:
#         print('NO')
#         exit(0)
    
# print('\n'.join(result))

import sys
# 빠른 입력 함수 사용
input = sys.stdin.readline

n = int(input()) # 수의 개수
stack = [] # 스택(stack) 초기화
answer = [] # 최종 정답
current = 1 # 현재 삽입할 수

for _ in range(n):
    x = int(input()) # 하나씩 수 입력
    # top()보다 x가 더 크다면, 스택에 삽입
    while len(stack) == 0 or stack[-1] < x:
        stack.append(current)
        current += 1
        answer.append('+')
    # top()과 x가 같다면, 스택에서 제거
    if stack[-1] == x:
        stack.pop()
        answer.append('-')
    # top()보다 x가 더 작다면 불가능
    else:
        answer = ["NO"]
        break

for x in answer: # 정답 출력
    print(x)
