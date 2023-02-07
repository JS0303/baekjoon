# arr = list(map(int, input().split(' ')))

# ascending = True
# descending = True

# for i in range(1, 8):
# 	if arr[i] > arr[i-1]:
# 		descending = False
# 	elif arr[i] < arr[i-1]:
# 		ascending = False

# if ascending:
#     print("ascending")
# elif descending:
#     print("descending")
# else:
#     print("mixed")

# 스스로 푼 코드
lst = list(map(int, input().split()))

if sorted(lst) == lst:
    print("ascending")
elif sorted(lst) == lst[::-1]:
    print("descending")
else:
	print("mixed")