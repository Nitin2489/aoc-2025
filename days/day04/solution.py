from utilities.parse import Parse

'''
Input: a grid consisting of "." and "@" characters

@ represents a roll of paper
. represents empty space

Need to find the total number of rolls of paper that the forklift can access

The forklift can only access a roll of paper if there are fewer than 4 rolls of paper in the adjacent 8 positions.
'''

def check_adjacent(grid, row, col) -> int:
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    count = 0
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]): # check bounds (edges of grid)
            if grid[r][c] == '@':
                count += 1
    return count

def part1(data: str) -> int:
    grid = Parse.to_2d_list(data)
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '@' and check_adjacent(grid, row, col) < 4:
                count += 1
    return count

def part2(data: str) -> int:
    grid = Parse.to_2d_list(data)
    return 0
