def enq(x):  # enqueue (1번 stack 활용)
    global stack1
    stack1.append(x)
    return x


def deq():  # dequeue (1,2번 stack 활용)
    global stack1, stack2
    if len(stack1) == 0 and len(stack2) == 0:  # 1,2번 stack이 전부 비어있는 경우 EMPTY
        return "EMPTY"
    elif len(stack2) != 0:  # 2번 stack에 값이 남아있는 경우 2번에서 POP
        return stack2.pop()
    else:  # 1번 stack에 값이 남아있는 경우 pop한 뒤 2번에 push
        while len(stack1) != 0:
            stack2.append(stack1.pop())
        return stack2.pop()  # First input을 pop


stack1, stack2, p, q = [], [], [], []
check = "None"
while check != "exit":  # exit가 나올때까지 입력
    check = input()
    q.append(check)

p = [k.split(" ") for k in q]  # 연산과 값을 분리 후 저장
# for i in range(len(q)):
#     p.append(q[i].split(" "))

for j in range(len(p)):  # 해당하는 연산 수행
    if p[j][0] == "exit":  # exit인 경우 종료
        break
    elif p[j][0] == "enq":  # enq인 경우
        enq(p[j][1])
    elif p[j][0] == "deq":  # deq인 경우
        print(deq())
    else:  # 값인 경우 넘어감
        continue

# enqueue의 경우 1번 stack에 값을 push하는 경우 이므로 O(1)의 시간이 걸린다.
# dequeue의 경우 2가지 조건에 의해 시간 복잡도가 정해진다.
# 우선 1. 2번 stack에 값이 남아있는 경우 2번에서 pop을 하는 경우이다.
# 2번 stack에 값이 남아있는 경우는 1번 stack에서 역방향으로 2번 stack에 저장되어 있기 때문에 queue와 같이 FIFO의 원칙을 지킨다. 이는 O(1)의 시간이 걸린다.
# 2. 1번 stack에 값이 남아있는 경우 모든 값을 pop한 뒤 2번에 push한 뒤 값을 pop을 하는 경우이다.
# 이는 1번 stack에서 LIFO의 원칙을 가지고 있기 때문에 모든 값을 pop한 뒤 2번 stack에 저장하는 경우 역방향으로 쌓인다.
# 즉 제일 먼저 들어온 값이 2번 stack에서 제일 위로 가는 것이다. 따라서 queue를 만족하게 된다.
# dequeue의 시간 복잡도를 보면, 조건 1의 경우 O(1)의 시간이 걸리지만, 조건 2의 경우 1번 stack에서 2번 stack으로 옮기는 과정이 O(n)의 시간이 걸린다.
# 하지만 항상 1번 stack에서 2번 stack으로 옮기는 과정이 일어나지 않으므로 평균적으로는 O(1)의 시간이 걸린다. (W.C는 O(n)이다.)
