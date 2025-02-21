import matplotlib.pyplot as plt
import random
import numpy as np
from matplotlib.ticker import MultipleLocator

fig, ax = plt.subplots()
min_val, max_val = 0, 25
data = [[[] for _ in range(25)] for _ in range(25)]

def set_data():
    for i in range(25):
        for j in range(25):
            random_number = random.randint(0, 50)
            if random_number < 6:
                data[i][j] = 1
            else:
                data[i][j] = 0

set_data()
table = ax.table(cellText=data, loc='center')

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
    for coords in get_filled_coords():
        table[coords].set_facecolor('black')
        ax.add_patch(table[coords])

    for coords in get_empty_coords():
        table[coords].get_text().set_color('white')
        ax.add_patch(table[coords])

color_cells()

# ========= TESTS =========
# print(get_column_data(1))
# print(get_row_data(0))
# print(get_cell_data(1, 1))
# print("filled coords:")
# print(get_filled_coords())
for row in data:
    print(row)


# plt.matshow(np.random.randint(0, 2, (25, 25)), cmap='viridis')

# ax.set_xlim(min_val, max_val)
# ax.set_ylim(min_val, max_val)
# ax.set_xticks([])
# ax.set_yticks([])
# ax.grid()
#
# plt.show()

# Highlight a specific cell (e.g., row 1, column 1)
# cell = table[1, 1]
# cell.set_facecolor('lightgreen')
# ax.add_patch(cell)

# Adjust table and axes properties
table.scale(1, 1)
ax.axis('off')

plt.show()

# draw the grid

# place pieces on the board

# rules for the pieces to decide how to behave

# re-draw the board after pieces decide what to do