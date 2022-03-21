def select_vote(num, A):
    max = -1
    B = [0 for i in range(num+1)]
    C = []
    for i in range(0,num):
        B[A[i]+1] += 1
        if max == B[A[i]+1] and len(C) != 0:
            C.pop()
        elif max < B[A[i]+1]:
            if len(C) != 0:
                C.pop()
            max = B[A[i]+1]
            C.append(A[i])
    if len(C) == 0:
        return -1
    else:
        k = C.pop()
        if B[k+1] > (num / 2):
            return k
        else:
            return -1

n = int(input())
A = [int(k) for k in input().split()]

print(select_vote(n,A))