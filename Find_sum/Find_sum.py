def find_sum(num, num_array):
    max_sum = num[1]

    for i in range(0, len(num_array)):
        sum = 0
        for j in range(i, len(num_array)):
            if max_sum == sum + num_array[j]:
                return True
            elif max_sum < sum + num_array[j]:
                break
            else:
                sum = sum + num_array[j]
                continue
    return False


num = [int(n) for n in input().split()]
num_array = [int(n) for n in input().split()]

print(find_sum(num, num_array))
