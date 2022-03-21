def ding_dang_dong(num, A):
    count = 0
    for i in range(1, num-1):
        b = A[i]
        j = 0
        while j != i:
            k = i+1
            a = A[j]
            interval = b-a
            while k != num:
                if b-a <= A[k] - b :
                    if A[k] - b <= (interval*2):
                        print(a, b, A[k])
                        count += 1
                    else:
                        break
                k += 1
            j = j+1
    return count

A = []
n = int(input())
for i in range(n):
    A.append(int(input()))
A.sort()
count = ding_dang_dong(n,A)
print(count)