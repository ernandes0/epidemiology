import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def plot_simulation(frames):
    fig, ax = plt.subplots()
    cmap = plt.get_cmap("viridis", 3)
    
    def update(frame):
        ax.clear()
        ax.imshow(frames[frame], cmap=cmap, vmin=0, vmax=2)
        ax.set_title(f"Step {frame}")
    
    ani = animation.FuncAnimation(fig, update, frames=len(frames), repeat=False)
    plt.show()
    
if __name__ == "__main__":
    test_frames = [np.random.randint(0, 3, (50, 50)) for _ in range(50)]
    plot_simulation(test_frames)
