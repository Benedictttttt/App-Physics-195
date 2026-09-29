import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Initial conditions and simulation length
steps = 100
x0, y0 = 1.0, 1.0


def run_simulation(a, b, r_x, r_y, K_x, K_y):
    x, y = x0, y0
    xresult, yresult = [x], [y]

    for _ in range(steps):
        nextx = x + r_x * x * (1 - (x + a * y) / K_x)
        nexty = y + r_y * y * (1 - (y + b * x) / K_y)
        x, y = nextx, nexty
        xresult.append(x)
        yresult.append(y)

    return xresult, yresult


# Set up figure and layout
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(bottom=0.35)  # Leave space for sliders

# Initial plot
xres, yres = run_simulation(a=1.1, b=1.7, r_x=2.3, r_y=1.2, K_x=2.6, K_y=1.6)
(line_x,) = ax.plot(xres, 'b-', label='x')
(line_y,) = ax.plot(yres, 'g--', label='y')
ax.set_title('Interactive Competitive Lotka-Volterra Model')
ax.set_xlabel('Time')
ax.set_ylabel('Population')
ax.legend()
ax.grid(True)

# Define slider axes locations [left, bottom, width, height]
ax_a = plt.axes([0.15, 0.22, 0.25, 0.03])
ax_b = plt.axes([0.60, 0.22, 0.25, 0.03])
ax_rx = plt.axes([0.15, 0.15, 0.25, 0.03])
ax_ry = plt.axes([0.60, 0.15, 0.25, 0.03])
ax_Kx = plt.axes([0.15, 0.08, 0.25, 0.03])
ax_Ky = plt.axes([0.60, 0.08, 0.25, 0.03])

# Create Sliders
s_a = Slider(ax_a, 'a', 0.0, 3.0, valinit=1.1)
s_b = Slider(ax_b, 'b', 0.0, 3.0, valinit=1.7)
s_rx = Slider(ax_rx, 'r_x', 0.0, 4.0, valinit=2.3)
s_ry = Slider(ax_ry, 'r_y', 0.0, 4.0, valinit=1.2)
s_Kx = Slider(ax_Kx, 'K_x', 0.1, 5.0, valinit=2.6)
s_Ky = Slider(ax_Ky, 'K_y', 0.1, 5.0, valinit=1.6)


# Update function called whenever a slider moves
def update(val):
    xres, yres = run_simulation(
        s_a.val, s_b.val, s_rx.val, s_ry.val, s_Kx.val, s_Ky.val
    )
    line_x.set_ydata(xres)
    line_y.set_ydata(yres)

    # Dynamically adjust y-axis limits to keep population visible
    all_vals = xres + yres
    ax.set_ylim(min(all_vals) * 1.1, max(all_vals) * 1.1)
    fig.canvas.draw_idle()


# Attach update function to slider events
s_a.on_changed(update)
s_b.on_changed(update)
s_rx.on_changed(update)
s_ry.on_changed(update)
s_Kx.on_changed(update)
s_Ky.on_changed(update)

plt.show()
