directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "up_left": (-1, -1),
    "up_right": (-1, 1),
    "down_left": (1, -1),
    "down_right": (1, 1)
}


def move_up(row, col):
    return row - 1, col


def move_down(row, col):
    return row + 1, col


def move_left(row, col):
    return row, col - 1


def move_right(row, col):
    return row, col + 1


def move_up_left(row, col):
    return row - 1, col - 1


def move_up_right(row, col):
    return row - 1, col + 1


def move_down_left(row, col):
    return row + 1, col - 1


def move_down_right(row, col):
    return row + 1, col + 1


def move_rover(direction, row, col):  # движим се по матрицата
    if direction == "up":
        return row - 1, col
    if direction == "down":
        return row + 1, col
    if direction == "left":
        return row, col - 1
    if direction == "right":
        return row, col + 1


def reposition_rover(row, col,
                     size):  # прескачаме матрицата - от края местим в началото и от горе местим долу и обратното
    if row < 0:
        return size - 1, col
    if row >= size:
        return 0, col
    if col < 0:
        return row, size - 1
    if col >= size:
        return row, 0


def is_outside(row, col, size):  # правим проверка дали е в матрицата
    return row < 0 or col < 0 or row >= size or col >= size


n = input().split()
stack = []

for _ in range(len(n)):
    stack.append(n.pop())

print(' '.join(stack))
