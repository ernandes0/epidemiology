from src.simulation import CellularAutomaton
from src.visualization import plot_simulation

def main():
    print("Iniciando simulação...")
    ca = CellularAutomaton(grid_size=50, infection_prob=0.3, recovery_time=10, initial_infected=3)
    simulation_frames = ca.run_simulation(steps=50)
    print("Simulação concluída. Gerando visualização...")
    plot_simulation(simulation_frames)

if __name__ == "__main__":
    main()
