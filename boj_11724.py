import sys
# 빠른 입력 함수 사용
input = sys.stdin.readline

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면
    if parent[x] != x:
        # 루트 노드를 찾을 떄까지 재귀적으로 호출
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 점의 개수 N과 게임(차례)의 수 M
n, m = map(int, input().split())
parent = [0] * (n+1) # 부모 테이블 초기화하기
# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(n):
    parent[i] = i

cycle = False # 사이클 발생 여부
for i in range(m): # M은 합치기(Union) 연산의 수와 동일
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        print(i + 1) # 사이클이 처음으로 만들어진 차례의 번호
        break
    # 사이클이 발생하지 않았다면 합집합(Union) 연산 수행
    else:
        union_parent = (parent, a, b)
    
if not cycle: # 사이클이 발생하지 않은 경우
    print(0)