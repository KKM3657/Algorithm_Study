# def is_possible(value_list, visit, n):
#     global stack_l, chance
#     a,b = value_list[0],value_list[1]
#     for i in range(n):
#         for j in range(n):
#             if i == a or j == b or abs(i - a) == abs(j - b) or i + j == a + b:
#                 continue
#             else:
#                 if visit[i][j] == 1:
#                     continue
#                 else:
#                     stack_l.append([i, j])
#                     #visit[i][j] = 1
#     return
#
# def n_queen(stack_l, visit, n):
#     global count
#     if len(stack_l) == 0:
#         return
#     value_list = stack_l.pop()
#     count += 1
#     visit[value_list[0]][value_list[1]] = 1
#     is_possible(value_list, visit, n)
#     n_queen(stack_l, visit, n)
#
# n = int(input())
# count = -1
# stack_l = [[0,0]]
# visit = [[0 for i in range(n)] for j in range(n)]
# n_queen(stack_l,visit,n)
# print(count)


def solution(n):
    cnt = 1  # while 반복문을 위한 count 변수

    while cnt < n:  # O(n)
        tmp = cnt + 1
        next = (2 * tmp - 1) * (tmp ** 2 - 3 * tmp + 2) - (tmp - 1) * (tmp - 2)  # sol(n-1)에 더해질 값
        DP.append(DP[-1] + next)  # DP 테이블에 저장

        cnt += 1


# main
n = int(input())
DP = [0]  # DP memoization
solution(n)
print(DP[-1])