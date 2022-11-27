iterations = int(input())

stack = []
stack_is_empty = False
for q in range(iterations):
    queries = list(map(int, input().split()))
    stack_is_empty = False
    if queries[0] == 1:
        stack.append(queries[1])
    elif queries[0] == 2:
        if len(stack) > 0:
            stack.pop()
        else:
            stack_is_empty = True
            continue
    elif queries[0] == 3:
        if len(stack) > 0:
            print(max(stack))
    elif queries[0] == 4:
        if len(stack) > 0:
            print(min(stack))

reversed_stack = []
for _ in range(len(stack)):
    reversed_stack.append(str(stack.pop()))

print(', '.join(reversed_stack))
