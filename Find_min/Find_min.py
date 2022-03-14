def find_min(num, num_array):
    B = []
    min = 100001
    for i in range(0, num[1]):
        if min > num_array[i]:
            min = num_array[i]
    B.append(min)
    print(min, end=' ')
    for i in range(1, num[0] - num[1] + 1):
        min = 100001
        if i == num[0] - num[1] or num_array[i - 1] == B[i - 1]:
            for j in range(i, i + num[1]):
                if min > num_array[j]:
                    min = num_array[j]
            B.append(min)
            print(min, end=' ')
        elif B[i - 1] > num_array[i + num[1] - 1]:
            min = num_array[i + num[1] - 1]
            B.append(min)
            print(min, end=' ')
        else:
            min = B[i - 1]
            B.append(min)
            print(min, end=' ')


num = [int(n) for n in input().split()]
num_array = [int(n) for n in input().split()]
find_min(num, num_array)

# def find_min(num,num_array):
#     B = []
#     for i in range(0,num[0]-num[1]+1):
#         min = 100000
#         for j in range(i,i+num[1]):
#             if min > num_array[j]:
#                 min = num_array[j]
#         B.append(min)
#         print(min, end=' ')
#
#
# num = [int(n) for n in input().split()]
# num_array = [int(n) for n in input().split()]
# B = find_min(num, num_array)
