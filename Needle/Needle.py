def solution(U,M,L):
    result = 0
    for value1 in U:
        for value2 in M:
            k = value1 - value2
            target = value2 - k
            if is_target(target, L):
              result += 1
    return result

def is_target(target, L):
    start = 0
    end = len(L) - 1

    while start <= end:
        mid = (start + end) // 2

        if L[mid] == target:
            return True  # 함수를 끝내버린다.
        elif L[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return False


u = int(input())
U = [int(n) for n in input().split()]
m = int(input())
M = [int(n) for n in input().split()]
l = int(input())
L = [int(n) for n in input().split()]

L.sort()

print(solution(U,M,L))