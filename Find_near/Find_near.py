def find_near(num, num_array):  # 작으면서 가까운 값을 찾기 위한 메소드
    B = [0, ]   # A[i]보다 작은 값 중에서 A[i]와 가장 가까운 위치의 수를 찾은 후 B에 저장
    for i in range(1, num): # A의 모든 원소 순회
        near = -1   # 조건을 만족하는 가장 가까운 A[i] 값
        for j in reversed(range(i)):    # A[i]에서 왼쪽으로 원소 순회
            if num_array[i] > num_array[j]: # 조건을 만족하는 가장 가까운 위치의 수인지 판별
                near = num_array[j]
                break
        if near == -1:  # A[i]에서 왼쪽으로 원소 순회하였지만 조건을 만족하지 않으면 0 저장
            B.append(0)
        else:           # 조건을 만족하는 값을 B에 저장
            B.append(near)
    return B


num = int(input())  # n 값
num_array = [int(n) for n in input().split()]   # n개의 값
B = find_near(num, num_array)

for value in B: # 출력
    print(value, end=' ')

# 작으면서 가까운 값 찾기에서 사용한 자료구조는 리스트이며, 위 코드는 리스트 A를 순회하면서 A[i]보다 작은 값 중에서 A[i]와 가장 가까운 위치의 수를 찾는다.
# B의 첫번째 원소는 항상 0이므로 0으로 초기화를 하였다.
# 첫번째 for문에서는 리스트 원소를 하나씩 순회한다. 즉 n개의 원소를 순회한다.
# 안에 있는 for문은 앞에서 선택한 원소를 기점으로 왼쪽으로 순회한다. 즉 인덱스가 1씩 줄어들며, 조건에 만족하지 않으면 0까지 순회한다.
# 또한 조건을 만족하는 가장 가까운 위치의 수인지 판별하기 위해서 기준이 되는 A[i]와 왼쪽 원소 값을 차례대로 비교한다.
# 최악의 경우 왼쪽 원소를 하나씩 순회를 해야하기 때문에 위와 값이 0부터 n-1까지 순회할 수 있다.
# 하지만 A[i] 바로 앞에 작은 수가 있는 경우 상수 번의 순회가 가능하다.
# 따라서 w.c인 경우 O(n^2)의 시간이 걸리지만 평균적으로는 O(n)의 수행시간이 걸린다.
