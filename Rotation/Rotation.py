# O(log(n))
def rotation(A, first, last):  # rotation_list의 k를 찾기 위한 메소드
    if A[first] <= A[last]:  # 이진탐색에서 구간을 넘어가는 경우 리턴
        return first
    mid = (first + last) // 2  # 중간값 설정
    next_value = (mid + 1) % len(A)  # mid의 다음값(mid가 끝점이면 시작점이 됨)
    prev = (mid - 1 + len(A)) % len(A)  # mid의 전값(mid가 시작점이면 끝점이 됨)

    if A[mid] <= A[next_value] and A[mid] <= A[prev]:  # 처음 시작점을 찾기 위한 이진탐색(재귀 이용)
        return mid  # 시작점 탐색 완료
    elif A[mid] <= A[last]:  # 중간값보다 끝값이 큰 경우 시작점이 first부터 mid-1사이 구간에 있음
        return rotation(A, first, mid - 1)
    elif A[mid] >= A[first]:  # 중간값보다 시작값이 작은 경우 시작점이 mid+1부터 last사이 구간에 있음
        return rotation(A, mid + 1, last)


# O(n)
# def rotation(A):
# 	i, min = 1, A[0]
# 	while i != len(A) and min < A[i]:
# 		min = A[i]
# 		i += 1
# 	return i

A = [int(n) for n in input().split()]
first, last = 0, len(A) - 1
print((len(A) - (rotation(A, first, last))) % len(A))

# 이 문제는 이진탐색 문제이다. 탐색할 것은 시작점의 위치이며, 구간을 나누는 기준은 중간값과 양 끝점을 비교하여 구간 안에서의 시작점 위치를 찾는 기준이 된다.
# 구간 안에서 first값이 mid보다 작은 경우 first부터 mid까지 증가하는 구간이므로 시작점이 될 수 없다. 따라서 mid+1부터 last의 구간에서 시작점이 있다.
# 마찬가지로 mid값보다 last값이 큰 경우 mid값부터 last까지 증가하는 구간이므로 시작점이 될 수 없다. 따라서 first부터 mid-1의 구간에서 시작점이 있다.
# 이진 탐색을 통해 시작점의 위치를 알 수 있다.
# 시간 복잡도는 서로 다른 n개의 값에서 시작점의 위치를 찾는 것이므로 O(log(n))의 시간이 걸리고 여기서 n은 입력받은 서로 다른 오름차순으로 정렬된 숫자이다.
# 즉 O(log(n))의 시간 복잡도가 걸린다.


