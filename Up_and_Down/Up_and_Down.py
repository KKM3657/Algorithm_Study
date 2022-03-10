def solve(A):
    B = [A[0]]  # 조건을 만족하는 리스트
    top = A[0]  # 리스트의 끝부분 초기화

    for i in range(1, len(A)):  # 리스트 A만큼 반복
        if i % 2 == 0:  # 인덱스가 짝수일때
            if top >= A[i]:  # A[i] <= A[i+1]이 만족
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

# 주어진 리스트 A를 순회하면서 만약 A[짝수] <=[짝수+1]이 만족할 경우 그대로 리스트 B에 들어간다.
# A[짝수] <= [짝수+1]가 만족하지 않는 경우 리스트 B에서 값을 pop한 뒤 순서를 바꿔서 다시 저장한다.
# A[홀수] >= [홀수+1]가 만족한 경우 마찬가지로 리스트 B에 들어가며, 만족하지 않는 경우 순서를 바꿔서 저장한다.
# 여기서 top은 리스트 B의 끝부분을 말하며, 주어진 조건을 만족하는지 확인하기 위한 변수로 사용된다.
# 다음의 코드는 리스트 A 원소를 한번씩 방문하면서 조건을 확인한다. 또한 인덱스가 짝수, 홀수인 경우 조건을 만족하는지, 만족하지 않으면
# pop한 뒤 순서를 바꿔서 append하는 연산이 일어나므로 W.S O(n)의 시간이 걸린다.

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
