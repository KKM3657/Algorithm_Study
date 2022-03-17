def find_min(num, num_array):  # 구간 최소 값 찾기 위한 메소드
    B = []  # 구간에 해당하는 최소값이 저장된 리스트
    min = 100001  # 최소값 초기화
    for i in range(0, num[1]):  # 구간 k를 순회
        if min > num_array[i]:  # B[0]을 탐색
            min = num_array[i]
    B.append(min)
    for i in range(1, num[0] - num[1] + 1):  # 구간 k로 만들수 있는 최대 묶음까지 순회
        min = 100001
        if i == num[0] - num[1] or num_array[i - 1] == B[i - 1]:  # 최대 인덱스에 도달하였거나 A[i-1]과 B[i-1](이전 결과값)이 같은 경우
            for j in range(i, i + num[1]):  # 구간 k에서의 최소값 탐색
                if min > num_array[j]:
                    min = num_array[j]  # 최소값이 A[j]
            B.append(min)
        elif B[i - 1] > num_array[i + num[1] - 1]:  # B[i-1](이전 결과값)이 A[i+k-1](구간 K에서의 마지막 값) 보다 클 경우 최소값 갱신
            min = num_array[i + num[1] - 1]  # 최소값이 A[i+k-1]
            B.append(min)
        else:  # A[i-1], B[i-1], A[i+k-1]을 비교하였을때 이전의 값을 활용할 수 있는 경우
            min = B[i - 1]  # 최소값이 B[i-1]
            B.append(min)
    return B


num = [int(n) for n in input().split()]  # n, k의 값
num_array = [int(n) for n in input().split()]  # A의 n개의 값
B = find_min(num, num_array)

for value in B:  # 출력
    print(value, end=' ')

# 구간 최소 값 찾기에서 사용한 자료구조는 리스트이며, 위 코드는 리스트 A를 순회하면서 구간 k에서 최소값이 되는 값을 탐색한다.
# 여기서 사용된 방법은 A[i-1], B[i-1], A[i+k-1]을 비교하여 최소값을 찾는 방식이며, 불필요한 순회를 줄이기 위해 기존의 값을 재활용했다.
# 첫번째 for문에서는 구간 k로 만들수 있는 최대 묶음까지 순회하였다. 즉 n - k개의 원소를 순회한다.
# 안에 있는 조건문은 A[i-1], B[i-1], A[i+k-1]에서 최소값이 어떤것 판별하는 조건식이다.
# 최대 인덱스에 도달하였거나 A[i-1]과 B[i-1](이전 결과값)이 같은 경우 A[i-1]가 최소값이 되기 때문에 B[i-1]를 이용할 수 없다. 즉 순회를 하면서 탐색해야된다.
# 두번째로 B[i-1](이전 결과값)이 A[i+k-1](구간 K에서의 마지막 값) 보다 클 경우 A[i+k-1]가 최소값이 되므로 B에 A[i+k-1]을 저장한다. 상수의 시간이 걸린다.
# 마지막으로 A[i-1], B[i-1], A[i+k-1]을 비교하였을때 B[i-1]이 최소인 경우 이전의 값을 활용할 수 있으므로 상수의 시간이 걸린다.
# 최악의 경우 모든 원소를 순회를 해야하기 때문에 위와 값이 n번 순회할 수 있지만 이전의 값을 활용하는 경우와 A[i+k-1](구간 K에서의 마지막 값)이 최소인 경우 상수의 시간이 걸린다.
# 따라서 w.c인 경우 O(n^2)의 시간이 걸리지만 평균적으로는 O(n)의 수행시간이 걸린다.


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
