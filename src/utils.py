import numpy as np

def generate_random_grid(grid_size, infected_count):
    """Gera uma grade inicial aleatória com um número específico de infectados."""
    grid = np.zeros((grid_size, grid_size), dtype=int)
    for _ in range(infected_count):
        x, y = np.random.randint(0, grid_size, size=2)
        grid[x, y] = 1
    return grid
