# Stack을 위한 클래스
class Stack:
    def __init__(self):  # Stack 객체 초기화
        self.stack = []  # 값이 저장된 스택
        self.stack_max = []  # max값이 갱신될 때마다 저장하기 위한 스택
        self.max_value = None  # max

    def push(self, x):  # push 메소드
        self.stack.append(x)  # Stack에 x를 push
        if self.max_value is None:  # 처음으로 push하는 값이면 max값 갱신후 스택에 저장
            self.max_value = x
            self.stack_max.append(x)
            return
        if self.max_value <= x:  # 기존의 max값보다 x가 더 크면 max값 갱신후 스택에 저장
            self.max_value = x
            self.stack_max.append(x)
            return

    def pop(self):  # pop 메소드
        if len(self.stack) == 0:  # 스택이 비어있다면 "EMPTY" 반환
            return "EMPTY"
        pop_value = self.stack.pop()  # 값이 저장된 스택에서 pop
        if pop_value == self.max_value:  # pop한 값이 max값과 같다면 max값 재설정
            self.stack_max.pop()  # stack_max에서 max값을 pop하고 새로운 max 설정
            if len(self.stack_max) == 0:  # pop한 뒤 스택이 비어있다면 새로운 max 설정을 넘어감
                return pop_value
            self.max_value = self.stack_max[-1]  # max값 재설정
            return pop_value
        else:  # pop한 값이 max값 보다 작으면 max값을 변경하지 않고 pop
            return pop_value

    def max(self):  # max 메소드
        if len(self.stack) == 0:    # 스택이 비어있다면 "EMPTY" 반환
            return "EMPTY"
        return self.max_value   # max값 반환


p, q = [], []
check = "None"
S = Stack()
while check != "exit":  # exit가 나올때까지 입력
    check = input()
    q.append(check)

p = [k.split(" ") for k in q]  # 연산과 값을 분리 후 저장

for i in range(len(p)):  # string으로 저장된 값을 integer로 변환
    if p[i][0] == "push":
        p[i][1] = int(p[i][1])

for j in range(len(p)):  # 해당하는 연산 수행
    if p[j][0] == "exit":  # exit인 경우 종료
        break
    elif p[j][0] == "push":  # push인 경우
        S.push(p[j][1])
    elif p[j][0] == "pop":  # pop인 경우
        print(S.pop())
    elif p[j][0] == "max":  # max인 경우
        print(S.max())

# push 메소드에서는 스택에 값을 저장하는데 O(1)의 시간이 걸린다. 또한 push시 max값 설정, stack_max에 값을 push하는 것이므로 O(1)의 시간이 걸린다.
# pop 메소드에서는 스택에서 값을 pop하는데 O(1)의 시간이 걸린다. 또한 max값을 재설정 할 경우 stack_max에서 pop하는 것이므로 마찬가지로 O(1)의 시간이 걸린다.
# max 메소드에서는 class Stack에서 max_value를 관리하고 있으므로 해당하는 값만 가져오면 된다. 즉 O(1)의 시간이 걸린다.