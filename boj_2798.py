n ,m = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))

sum_list = []

for i in range(0, len(arr)):
  for j in range(i + 1, len(arr)):
    for k in range(j + 1, len(arr)):
      sum_num = arr[i]+arr[j]+arr[k]
      if sum_num <= m:
        sum_list.append(arr[i]+arr[j]+arr[k])

print(max(sum_list))