import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# -----------------------------
# Drone Class
# -----------------------------
class Drone:
    def __init__(self):
        self.t = 0
        self.pos = np.array([0.0, 50.0])

    def update(self, mode):
        if mode == "Straight":
            self.pos[0] += 1
        else:
            self.t += 0.2
            self.pos[0] += 1
            self.pos[1] += np.sin(self.t) * 3


# -----------------------------
# Missile Class
# -----------------------------
class Missile:
    def __init__(self):
        self.pos = np.array([0.0, 0.0])
        self.vel = np.array([2.0, 2.0])

    def update_basic(self, target_pos):
        direction = target_pos - self.pos
        direction = direction / (np.linalg.norm(direction) + 1e-5)
        self.vel = direction * 2
        self.pos += self.vel

    def update_proportional(self, target_pos, target_vel):
        N = 3

        rel_pos = target_pos - self.pos
        rel_vel = target_vel - self.vel

        los_rate = np.cross(rel_pos, rel_vel) / (np.linalg.norm(rel_pos)**2 + 1e-5)

        accel = N * los_rate * np.array([-rel_pos[1], rel_pos[0]])
        self.vel += accel * 0.1

        self.vel = self.vel / (np.linalg.norm(self.vel) + 1e-5) * 2
        self.pos += self.vel


# -----------------------------
# Main App
# -----------------------------
class SimulationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🚁 Drone Interception Simulator")

        self.mode = tk.StringVar(value="Straight")
        self.guidance = tk.BooleanVar(value=False)
        self.running = False

        self.create_widgets()
        self.reset_simulation()

    def create_widgets(self):
        frame = ttk.Frame(self.root)
        frame.pack(side=tk.TOP, fill=tk.X)

        ttk.Button(frame, text="▶ Start", command=self.start).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame, text="🔄 Reset", command=self.reset_simulation).pack(side=tk.LEFT, padx=5)

        ttk.Label(frame, text="Mode:").pack(side=tk.LEFT)
        ttk.Combobox(frame, textvariable=self.mode,
                     values=["Straight", "Zigzag"], width=10).pack(side=tk.LEFT)

        ttk.Checkbutton(frame, text="🧠 Guidance", variable=self.guidance).pack(side=tk.LEFT, padx=10)

        # Figure
        self.fig, self.ax = plt.subplots(figsize=(6, 6))
        self.ax.set_xlim(0, 100)
        self.ax.set_ylim(0, 100)
        self.ax.set_facecolor("black")  # dark background

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack()

    def reset_simulation(self):
        self.running = False

        self.drone = Drone()
        self.missile = Missile()

        self.drone_path = []
        self.missile_path = []

        self.ax.clear()
        self.ax.set_xlim(0, 100)
        self.ax.set_ylim(0, 100)
        self.ax.set_facecolor("black")

        # Trails
        self.drone_trail, = self.ax.plot([], [], color="cyan", linewidth=1)
        self.missile_trail, = self.ax.plot([], [], color="orange", linewidth=1)

        # Icons (markers)
        self.drone_icon, = self.ax.plot([], [], marker="^", markersize=12, color="cyan", label="Drone")
        self.missile_icon, = self.ax.plot([], [], marker=">", markersize=12, color="orange", label="Missile")

        self.ax.legend()
        self.canvas.draw()

    def start(self):
        if not self.running:
            self.running = True
            self.animate()

    def animate(self):
        if not self.running:
            return

        prev_drone_pos = self.drone.pos.copy()

        # Drone movement
        self.drone.update(self.mode.get())
        drone_vel = self.drone.pos - prev_drone_pos

        # Missile movement
        if self.guidance.get():
            self.missile.update_proportional(self.drone.pos, drone_vel)
        else:
            self.missile.update_basic(self.drone.pos)

        # Store paths
        self.drone_path.append(self.drone.pos.copy())
        self.missile_path.append(self.missile.pos.copy())

        dp = np.array(self.drone_path)
        mp = np.array(self.missile_path)

        # Trails
        self.drone_trail.set_data(dp[:, 0], dp[:, 1])
        self.missile_trail.set_data(mp[:, 0], mp[:, 1])

        # Icons (IMPORTANT: use list)
        self.drone_icon.set_data([self.drone.pos[0]], [self.drone.pos[1]])
        self.missile_icon.set_data([self.missile.pos[0]], [self.missile.pos[1]])

        self.canvas.draw()

        # Hit detection
        if np.linalg.norm(self.drone.pos - self.missile.pos) < 2:
            self.ax.text(30, 50, "💥 TARGET HIT!", color="yellow", fontsize=16)
            self.canvas.draw()
            self.running = False
            return

        self.root.after(50, self.animate)


# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = SimulationApp(root)
    root.mainloop()
