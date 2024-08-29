def island_perimeter(grid):
    """
    Returns the perimeter of the island described in the grid.

    Parameters:
    grid (list of list of int): A 2D grid representing the map, where 0 is water and 1 is land.

    Returns:
    int: The perimeter of the island.
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:  # It's land
                # Check the four neighbors (up, down, left, right)
                # Up
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                # Down
                if row == rows - 1 or grid[row + 1][col] == 0:
                    perimeter += 1
                # Left
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                # Right
                if col == cols - 1 or grid[row][col + 1] == 0:
                    perimeter += 1

    return perimeter