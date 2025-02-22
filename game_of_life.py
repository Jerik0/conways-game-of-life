import random
import matplotlib.pyplot as plt
from matplotlib.table import Table
from pynput import keyboard
import time

# ======= HANDLE BOARD CREATION AND POPULATION ========
fig, ax = plt.subplots()
min_val, max_val = 0, 25
data = [[[] for _ in range(25)] for _ in range(25)]
table = ax.table(cellText=data, loc='center')
ax.axis('off')

# handle data
def set_data():
    print("setting data")
    for i in range(25):
        for j in range(25):
            random_number = random.randint(0, 50)
            if random_number < 13:
                data[i][j] = 1
            else:
                data[i][j] = 0
    print(data)

set_data()

def get_neighbors(row: int, column: int):
    neighbors = []
    for i in range(row - 1, row + 2):
        for j in range(column - 1, column + 2):
            if i == row and j == column:
                continue
            if i < 0 or i >= len(data) or j < 0 or j >= len(data[i]):
                continue
            neighbors.append(data[i][j])
    return neighbors

def simulate_board_change():
    set_data()
    color_cells()
    fig.canvas.draw()
    print(f"neighbors of (1, 1): {get_neighbors(1, 1)}")

def advance_board():
    print("advancing board")
    for i in range(25):
        for j in range(25):
            neighbors = get_neighbors(i, j)
            if data[i][j] == 1:
                if neighbors.count(1) == 2 or neighbors.count(1) == 3:
                    continue
                if neighbors.count(1) > 3:
                    data[i][j] = 0
                if neighbors.count(1) <= 1:
                    data[i][j] = 0

            if data[i][j] == 0:
                if neighbors.count(1) == 3:
                    data[i][j] = 1
    print(data)
    color_cells()
    fig.canvas.draw()

def run_every_x_ms(interval_ms, function):
    interval_seconds = interval_ms / 1000.0
    while True:
        start_time = time.time()
        function()
        end_time = time.time()
        elapsed_time = end_time - start_time
        sleep_time = interval_seconds - elapsed_time
        if sleep_time > 0:
            time.sleep(sleep_time)

    # for every cell on the board, check its neighbors
    # Birth: A dead cell with exactly three live neighbors becomes alive in the next generation
    # if 0 and has three live neighbors, change to 1 in next iteration.

    # Death by isolation: A live cell with one or fewer live neighbors dies in the next generation
    # if 1 and has one or fewer neighbors, change to 0

    # Death by overcrowding: A live cell with four or more live neighbors dies in the next generation
    # if 1 and has four or more 1 neighbors, change to 0

    # Survival: A live cell with two or three live neighbors lives on to the next generation
    # if 1 and has two or three 1 neighbors, stay the same

def on_key(event):
    if event.key == 'r':
        advance_board()

# helper functions
def get_column_data(column: int):
    column_data = []
    for row in data:
        column_data.append(row[column])
    return column_data

def get_row_data(row: int):
    return data[row]

def get_cell_data(row: int, column: int):
    return data[row][column]

def get_filled_coords():
    filled_coords = []
    for row in range(len(data)):
        for column in range(len(data[row])):
            if data[row][column] == 1:
                filled_coords.append((row, column))
    return filled_coords

def get_empty_coords():
    empty_coords = []
    for row in range(len(data)):
        for column in range(len(data[row])):
            if data[row][column] == 0:
                empty_coords.append((row, column))
    return empty_coords

def color_cells():
    for row in range(len(data)):
        for column in range(len(data[row])):
            if data[row][column] == 1:
                table[row, column].set_facecolor('black')
                table[row, column].get_text().set_color('black')
            else:
                table[row, column].set_facecolor('white')
                table[row, column].get_text().set_color('white')

# fill and show board
color_cells()

fig.canvas.mpl_connect('key_press_event', on_key)
plt.show()

# Example usage: Run the task every 500 milliseconds
run_every_x_ms(1000, advance_board)

# ========= TESTS =========
# for row in data:
#     print(row)
# print(get_column_data(1))
# print(get_row_data(0))
# print(get_cell_data(1, 1))
# print("filled coords:")
# print(get_filled_coords())



# Highlight a specific cell (e.g., row 1, column 1)
# cell = table[1, 1]
# cell.set_facecolor('lightgreen')
# ax.add_patch(cell)

# rules for the pieces to decide how to behave

# re-draw the board after pieces decide what to do

# def on_press(key):
#     try:
#         print('alphanumeric key {0} pressed'.format(key.char))
#         simulate_board_change()
#     except AttributeError:
#         print('special key {0} pressed'.format(key))
#
#
# def on_release(key):
#     print('{0} released'.format(key))
#     if key == keyboard.Key.esc:
#         # Stop listener
#         return False
#
# # Collect events until released
# with keyboard.Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()