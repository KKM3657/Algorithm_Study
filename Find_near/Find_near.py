def find_near(num, num_array):
    B = [0, ]
    print(0, end = ' ')
    for i in range(1, num):
        near = -1
        for j in reversed(range(i)):
            if num_array[i] > num_array[j]:
                near = num_array[j]
                break
        if near == -1:
            B.append(0)
            print(0, end = ' ')
        else:
            B.append(near)
            print(near, end=' ')

    return B


num = int(input())
num_array = [int(n) for n in input().split()]
B = find_near(num, num_array)

