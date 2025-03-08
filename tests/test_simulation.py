import unittest
import numpy as np
from src.simulation import CellularAutomaton

class TestCellularAutomaton(unittest.TestCase):
    def setUp(self):
        self.ca = CellularAutomaton(grid_size=10, infection_prob=0.5, recovery_time=5, initial_infected=1)
    
    def test_initial_conditions(self):
        infected_count = np.sum(self.ca.grid == 1)
        self.assertEqual(infected_count, 1, "O número inicial de infectados deve ser 1")
    
    def test_simulation_step(self):
        self.ca.step()
        self.assertIn(1, self.ca.grid, "Deve haver células infectadas após um passo de simulação")
    
if __name__ == "__main__":
    unittest.main()
