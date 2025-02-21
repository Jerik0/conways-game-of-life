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
            if random_number < 6:
                data[i][j] = 1
            else:
                data[i][j] = 0
    print(data)

set_data()

def simulate_board_change():
    set_data()
    # Redraw the canvas
    ax.clear()
    table = ax.table(cellText=data, loc='center')
    ax.axis('off')
    color_cells()
    fig.canvas.draw()

def on_key(event):
    print(event)
    if event.key == 'r':
        simulate_board_change()

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

def clear_board():
    for row in range(len(data)):
        for column in range(len(data[row])):
            table[row, column].set_facecolor('white')
            ax.add_patch(table[row, column])

def color_cells():
    clear_board()
    for coords in get_filled_coords():
        table[coords].set_facecolor('black')
        table[coords].get_text().set_color('black')
        ax.add_patch(table[coords])

    for coords in get_empty_coords():
        table[coords].get_text().set_color('white')
        ax.add_patch(table[coords])

def close_board():
    plt.close()

print("neighbors of cell (1, 1):")
print(get_neighbors(1, 1))

# fill and show board
color_cells()

fig.canvas.mpl_connect('key_press_event', on_key)
plt.show()

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

# ========= TESTS =========
# for row in data:
#     print(row)
# print(get_column_data(1))
# print(get_row_data(0))
# print(get_cell_data(1, 1))
# print("filled coords:")
# print(get_filled_coords())

# Birth: A dead cell with exactly three live neighbors becomes alive in the next generation
# Death by isolation: A live cell with one or fewer live neighbors dies in the next generation
# Death by overcrowding: A live cell with four or more live neighbors dies in the next generation
# Survival: A live cell with two or three live neighbors lives on to the next generation

# Highlight a specific cell (e.g., row 1, column 1)
# cell = table[1, 1]
# cell.set_facecolor('lightgreen')
# ax.add_patch(cell)

# rules for the pieces to decide how to behave

# re-draw the board after pieces decide what to do