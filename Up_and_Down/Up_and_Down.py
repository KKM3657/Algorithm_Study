def solve(A):
    B = [A[0]]  # 조건을 만족하는 리스트
    top = A[0]  # 리스트의 끝부분 초기화

    for i in range(1, len(A)):  # 리스트 A만큼 반복
        if i % 2 == 0:  # 인덱스가 짝수일때
            if top >= A[i]:  # B[i] <= B[i+1]이 만족
                B.append(A[i])
                top = A[i]
            else:  # 만족하지 않으면 B에서 pop한 후 value에 저장 그리고 순서를 바꿈
                value = B.pop()
                B.append(A[i])
                B.append(value)
        if i % 2 == 1:  # 인덱스가 홀수일때
            if top <= A[i]:  # B[i] >= B[i+1]이 만족
                B.append(A[i])
                top = A[i]
            else:  # 만족하지 않으면 B에서 pop한 후 value에 저장 그리고 순서를 바꿈
                value = B.pop()
                B.append(A[i])
                B.append(value)
    return B


def check(B):
    if not (B[0] <= B[1]): return False
    for i in range(1, len(B) - 1):
        if i % 2 == 1 and not (B[i] >= B[i + 1]):
            return False
        if i % 2 == 0 and not (B[i] <= B[i + 1]):
            return False
        return True


A = [int(x) for x in input().split()]
B = solve(A)
print(B)
print(check(B))
