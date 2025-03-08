import numpy as np
import matplotlib.pyplot as plt
from src.visualization import plot_simulation

class CellularAutomaton:
    def __init__(self, grid_size=50, infection_prob=0.3, recovery_time=10, initial_infected=1):
        self.grid_size = grid_size
        self.infection_prob = infection_prob
        self.recovery_time = recovery_time
        self.grid = np.zeros((grid_size, grid_size), dtype=int)
        self.time_infected = np.zeros((grid_size, grid_size), dtype=int)
        self._initialize_infected(initial_infected)
    
    def _initialize_infected(self, initial_infected):
        for _ in range(initial_infected):
            x, y = np.random.randint(0, self.grid_size, size=2)
            self.grid[x, y] = 1
    
    def step(self):
        new_grid = self.grid.copy()
        new_time_infected = self.time_infected.copy()
        
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                if self.grid[x, y] == 1:
                    new_time_infected[x, y] += 1
                    if new_time_infected[x, y] >= self.recovery_time:
                        new_grid[x, y] = 2
                    else:
                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < self.grid_size and 0 <= ny < self.grid_size:
                                if self.grid[nx, ny] == 0 and np.random.rand() < self.infection_prob:
                                    new_grid[nx, ny] = 1
        
        self.grid = new_grid
        self.time_infected = new_time_infected
    
    def run_simulation(self, steps=50):
        frames = []
        for _ in range(steps):
            frames.append(self.grid.copy())
            self.step()
        return frames

if __name__ == "__main__":
    ca = CellularAutomaton()
    simulation_frames = ca.run_simulation(steps=50)
    plot_simulation(simulation_frames)
