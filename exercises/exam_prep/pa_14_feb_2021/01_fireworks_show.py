#90/100
from collections import deque

firework_effects = deque([int(el) for el in input().split(", ") if int(el) > 0])
explosive_power = [int(el) for el in input().split(", ") if int(el) > 0]

palm_firework = 0
willow_firework = 0
crossette_firework = 0

while firework_effects and explosive_power:
    sum_of_match = firework_effects[0] + explosive_power[-1]
    if sum_of_match % 3 == 0 and sum_of_match % 5 != 0:
        palm_firework += 1
        firework_effects.popleft()
        explosive_power.pop()
    elif sum_of_match % 5 == 0 and sum_of_match % 3 != 0:
        willow_firework += 1
        firework_effects.popleft()
        explosive_power.pop()
    elif sum_of_match % 3 == 0 and sum_of_match % 5 == 0:
        crossette_firework += 1
        firework_effects.popleft()
        explosive_power.pop()
    else:
        if firework_effects[0] > 1:
            firework_effects[0] -= 1
            firework_effects.append(firework_effects.popleft())


    if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
        break

if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(map(str, firework_effects))}")

if explosive_power:
    print(f"Explosive Power left: {', '.join(map(str, explosive_power))}")

print(f"Palm Fireworks: {palm_firework}")
print(f"Willow Fireworks: {willow_firework}")
print(f"Crossette Fireworks: {crossette_firework}")
