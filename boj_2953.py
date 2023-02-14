# 내 풀이
# user1 = list(map(int, input().split()))
# user2 = list(map(int, input().split()))
# user3 = list(map(int, input().split()))
# user4 = list(map(int, input().split()))
# user5 = list(map(int, input().split()))
# winner_score = max(sum(user1),sum(user2),sum(user3),sum(user4),sum(user5))
# member = [user1, user2, user3, user4, user5]
# winner = 0
# for i in range(5):
#     if sum(member[i]) == winner_score:
#         winner = i+1
#     else:
#         continue
# print(winner, winner_score)

# 모범답안
result = 0 # 최종 우승자
max_value = 0 # 평가 점수의 최댓값

# 요리사는 총 5명
for i in range(5):
    # 각 요리사마다 하나의 행(row)을 차지
    row = list(map(int, input().split()))
    summary = sum(row) # 현재 요리사의 합
    # 현재까지의 최대 합보다 현재 행(row)의 합이 더 큰 경우
    if max_value < summary:
        max_value = summary
        result = i + 1

print(result, max_value)