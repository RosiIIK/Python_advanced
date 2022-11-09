#not in judge, not ready!!!

numbers = list(map(int,input().split()))
target = int(input())

for number in numbers:
    second_numbers = numbers
    second_numbers.remove(number)
    for second in second_numbers:
        if number + second == target:
            print(f"{number} + {second} = {target}")
