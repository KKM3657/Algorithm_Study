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
    if p[j][0] == "exit":
        break
    elif p[j][0] == "enq":
        enq(p[j][1])
    elif p[j][0] == "deq":
        print(deq())
    else:
        continue
