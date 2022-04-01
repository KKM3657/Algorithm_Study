def search_solution(input1, input2):  # 최소 점프거리를 찾기 위한 메소드
    distance = input1[0]  # 최대 거리
    input2.append(distance)  # 이진탐색을 위한 마지막 거리추가
    k = input1[2]  # 최대 빼는 돌의 갯수
    answer = 0  # 최소 점프거리
    left = 1  # 시작점
    right = distance  # 끝점

    while left <= right:  # 시작점이 끝점을 넘어가지 않을때까지 반복
        rock_count = 0  # 최소 점프거리를 확인하기 위해 뺄 돌의 갯수
        next_rock = 0  # 최소거리를 설정했을때 다음 돌의 위치
        mid = (left + right) // 2  # 이진탐색을 위한 중간값 설정

        for value in input2:  # 돌의 위치를 순회하면서 뺄 돌의 갯수 확인
            if value - next_rock < mid:  # 다음 돌의 위치에서 최소 거리안에 돌이 있다면 그 돌을 뺌
                rock_count += 1
            else:  # 최소 거리를 넘어가는 돌을 발견하면 다음 돌로 넘어감
                next_rock = value

        if rock_count > k:  # 뺄 돌의 갯수가 설정한 최대 빼는 돌의 갯수를 넘어간다면 끝점을 mid-1로 옮김
            right = mid - 1
        else:  # 뺄 돌의 갯수가 설정한 최대 빼는 돌의 갯수보다 적으면 시작점을 mid+1로 옮김 (만약 설정한 돌의 갯수와 같다면 answer이 됨)
            left = mid + 1
            answer = mid

    return answer


input1 = [int(k) for k in input().split()]
input2 = [int(k) for k in input().split()]
print(search_solution(input1, input2))

# 이 문제는 이진탐색을 이용한 문제이다. 탐색할 것은 징검다리를 건너기 위해 필요한 점프의 최소값이며, 구간을 나누는 기준은 거리가 된다.
# 점프의 최소거리를 찾기 위해 mid라는 중간값을 두어 구간을 나누었다.
# 만약 구간의 mid값(최소거리)에 들어가는 돌이 있다면 뺄 돌로 설정하여 rock_count로 설정하고 최대 뺄수 있는 돌인 k개를 기준으로 rock_count가 적은지 많은지 판단할 수 있다.
# 적은 경우 최소 점프거리가 될 수 없는 경우가 있으므로 시작점을 mid+1로 옮겨 최소 점프거리를 제한 할 수 있다.
# 마찬가지로 많은 경우 최소 점프거리를 넘어가는 경우가 있으므로 끝점을 mid-1로 옮겨 최소 점프거리를 제한한다.
# 시간 복잡도는 이진탐색을 하는 경우이므로 O(log(n))의 시간이 걸리며, 여기서 n은 입력받은 돌의 갯수에 대한 것이 아니다.
# 즉 구간을 나누는 기준과 탐색의 주체인 거리 이므로 O(log(거리))가 시간복잡도가 된다.

