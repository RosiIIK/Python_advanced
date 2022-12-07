from collections import deque

males = [int(el) for el in input().split() if int(el) > 0]
females = deque([int(el) for el in input().split() if int(el) > 0])

match_counter = 0

while males and females:
    if males[-1] % 25 == 0:
        males.pop()
        if males:
            males.pop()

    elif females[0] % 25 == 0:
        females.popleft()
        if females:
            females.popleft()

    elif males[-1] == females[0]:
        match_counter += 1
        males.pop()
        females.popleft()

    else:
        females.popleft()
        males[-1] -= 2
        if males[-1] <= 0:
            males.pop()


if match_counter > 0:
    print(f"Matches: {match_counter}")

if males:
    males.reverse()
    print(f"Males left: {', '.join([str(el) for el in males])}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join([str(el) for el in females])}")
else:
    print("Females left: none")

