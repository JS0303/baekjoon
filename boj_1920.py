# N, A = int(input()), {i: 1 for i in map(int, input().split())}
# M = input()

# for i in list(map(int, input().split())):
# 	print(1 if i in A else 0)

n = int(input())
arr = set(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))
for i in x:
    if i in arr:
        print(1)
    else:
        print(0)
