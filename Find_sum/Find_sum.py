def find_sum(num, num_array):  # 목표 구간 합을 찾기 위한 메소드
    max_sum = num[1]  # 목표값
    for i in range(0, len(num_array)):  # 리스트 원소 순회
        sum = 0  # 합산값 초기화
        for j in range(i, len(num_array)):  # 앞에서 선택한 원소를 제외한 리스트 원소 순회
            if max_sum == sum + num_array[j]:  # 목표값이 있는 경우
                return True
            elif max_sum < sum + num_array[j]:  # 합산값이 목표값을 넘어가는 경우
                break
            else:  # 합산값이 목표값보가 작은 경우
                sum = sum + num_array[j]
                continue
    return False  # 목표 구간 합을 찾을 수 없음


num = [int(n) for n in input().split()]  # n, k의 값
num_array = [int(n) for n in input().split()]  # A의 n개의 값

print(find_sum(num, num_array))

# 목표 구간 합 찾기에서 사용한 자료구조는 리스트이며, 위 코드는 리스트 A를 순회하면서 연속된 값의 합이 k가 되는 값이 있는지 판별한다.
# 첫번째 for문에서는 리스트 원소를 하나씩 순회한다. 즉 n개의 원소를 순회한다.
# 안에 있는 for문은 앞에서 선택한 원소를 포함한 연속된 값의 합이 k를 넘는지 판별한다.
# 즉 연속된 구간의 합산값이 목표값 k를 넘어가는지 확인하기 위해서 두번째 for문에서 리스트 원소를 순회한다.
# 최악의 경우 모든 원소를 순회를 해야하기 때문에 위와 값이 n번 순회할 수 있지만 k의 최대값이 100,000이므로 모든 원소를 순회하지 않는 경우가 발생한다. 즉 상수의 시간이 걸릴수 있다.
# 따라서 w.c인 경우 O(n^2)의 시간이 걸리지만 평균적으로는 O(n)의 수행시간이 걸린다.
