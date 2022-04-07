def solution(n, L, k, zombies):
    global zombies_fall
    result = 0
    a, b = 0, 0
    while len(zombies_fall) < k:  # 떨어진 좀비의 수가 k가 될 때 반복
        zombie_temp = []  # 한칸 떨어져 있고 마주보고 있는 좀비들 제외할 때 사용할 리스트
        # 두 좀비를 비교하여 한칸 떨어져 있고 마주보고 있을때 위치는 그대로 하고 방향만 바꾸기 위해 zombie_temp에 인덱스 저장
        for i in range(len(zombies) - 1):
            if zombies[i][1] > 0 and zombies[i + 1][1] < 0:  # 마주볼 때
                if zombies[i + 1][0] == zombies[i][0] + 1:  # 1칸 떨어져 있을 때
                    zombie_temp.append(zombies[i])
                    zombie_temp.append(zombies[i + 1])
        # 좀비 이동
        for i in range(len(zombies)):
            if zombies[i] in zombie_temp:  # zombie_tmp에 해당 하는 좀비는 방향 반대로
                zombies[i][1] = -zombies[i][1]
            else:  # 1칸 이동
                if zombies[i][1] > 0:  # 오른쪽
                    zombies[i][0] += 1
                elif zombies[i][1] < 0:  # 왼쪽
                    zombies[i][0] -= 1

        # 좀비가 떨어졌을 때 zombie_fall 리스트에 추가
        zombie_fall_temp = []
        for i in range(len(zombies)):  # 좀비가 떨어지는 경우
            if zombies[i][0] < 0 or zombies[i][0] > L:
                zombie_fall_temp.append(zombies[i])

        if len(zombie_fall_temp) == 2:  # 양끝점에서 좀비가 떨어진 경우 우선순위에 맞게 조정 (id 기준)
            for i in range(n):
                if abs(zombie_fall_temp[0][1]) == abs(init_zombie[i]):
                    a = init_zombie[i]
                if abs(zombie_fall_temp[1][1]) == abs(init_zombie[i]):
                    b = init_zombie[i]
            if a > b:  # 부호에 맞게 우선순위 조정
                zombies_fall.append(abs(zombie_fall_temp[1][1]))
                zombies_fall.append(abs(zombie_fall_temp[0][1]))
            else:
                zombies_fall.append(abs(zombie_fall_temp[0][1]))
                zombies_fall.append(abs(zombie_fall_temp[1][1]))
        elif len(zombie_fall_temp) == 1:  # 한쪽 끝점에서 좀비가 떨어진 경우
            zombies_fall.append(abs(zombie_fall_temp[0][1]))

        for i in zombie_fall_temp:  # 떨어진 좀비는 좀비 목록에서 제거
            if i in zombies:
                zombies.remove(i)

        # 위치가 같을 때 방향만 바꾸기
        for i in range(len(zombies) - 1):
            if zombies[i][0] == zombies[i + 1][0]:
                zombies[i][1], zombies[i + 1][1] = -zombies[i][1], -zombies[i + 1][1]

    # 초기 좀비의 id와 비교해서 음수 or 양수로 출력
    for i in range(n):
        if zombies_fall[k - 1] == abs(init_zombie[i]):
            result = init_zombie[i]
    return result


n, L, k = map(int, input().split())  # 좀비 수, 길의 길이, k번째로 떨어질 좀비
zombies = []  # 좀비의 초기 위치 및 id 방향
for _ in range(n):
    zombies.append(list(map(int, input().split())))
zombies_fall = []  # 떨어진 좀비들
init_zombie = []  # 최초의 좀비 입력값을 저장하기 위한 리스트

for i in zombies:  # 최초의 좀비들의 id
    init_zombie.append(i[1])

print(solution(n, L, k, zombies))

# 이 문제는 좀비들을 이동시키며 충돌했을 때 방향을 반대로 바꾸고, 좀비들이 떨어졌을때 해당하는 순서에 떨어진 좀비를 찾는 문제이다.
# 떨어진 좀비들은 zombies_fall에 하나씩 저장되며, 우선순위에 맞게 하나씩 저장된다.
# 좀비가 충돌하는 경우는 거리가 1만큼 차이나는 경우나 거리가 0인 경우이다.
# 양 끝점에서 좀비가 떨어지는 경우에는 주어진 조건인 작은 id (음수 포함)가 먼저 떨어지므로 비교를 통해 우선순위를 정했다.
# 시간 복잡도는 우선 모든 좀비를 순회하면서 충돌하는 경우를 탐색하므로 O(n)의 시간과 좀비를 이동시키는 시간 O(n),
# 떨어진 좀비를 탐색하는 시간 O(n), 우선순위에 맞게 재배열하는 시간은 최악의 경우 O(n), 떨어진 좀비를 제거하는 시간 O(n)이 걸린다.
# 최악의 경우 총 O(n)의 시간이 걸리며, k번째 떨어진 좀비를 탐색하는 문제이므로 O(n)의 시간이 k번 반복 된다.
# 즉 시간 복잡도는 최악의 경우 O(Kn)이다.
