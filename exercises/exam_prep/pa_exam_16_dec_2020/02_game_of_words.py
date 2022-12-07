def is_in_range(row, col, mat_size):
    if 0 <= row < mat_size and 0 <= col < mat_size:
        return True
    return False

initial_string = list(input())
matrix_size = int(input())

matrix = []
player_position = []

for row in range(matrix_size):
    line = list(input())
    matrix.append(line)

    if "P" in line:
        player_position = [row, line.index('P')] #взимаме колоната на играча

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

movements = int(input())

for i in range(movements):
    direction = input()
    row = player_position[0]
    col = player_position[1]
    if direction in directions:
        next_row = row + directions[direction][0]
        next_col = col + directions[direction][1]

        if is_in_range(next_row, next_col, matrix_size):
            position = matrix[next_row][next_col]
            matrix[row][col] = "-"
            player_position = [next_row, next_col]

            if position.isalpha() and position != "P":
                initial_string += position
            matrix[next_row][next_col] = "P"

        else:
            if initial_string:
                initial_string = initial_string[:-1]
                # initial_string.pop()
            #     matrix[row][col] = 'P'
            #     continue
            # else:
            #     matrix[row][col] = 'P'
            #     continue

print(f"{''.join(map(str, initial_string))}")
print(*[''.join(row) for row in matrix], sep='\n')
