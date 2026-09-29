import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Initial Parameter
x_op_init = 50.0
a_init = 1.1
c_init = 0.00005
x0_init = 10.0
steps = 100

def run_simulation(x0, x_op, a, c, steps):
    x = np.zeros(steps + 1)
    x[0] = x0
    for t in range(steps):
        fx = -c * (x[t] - x_op)**2 + a
        x[t+1] = max(0.0, fx * x[t])  # Prevent negative population
    return x


fig, ax = plt.subplots(figsize=(8, 6))
plt.subplots_adjust(bottom=0.35)

t = np.arange(steps + 1)
population = run_simulation(x0_init, x_op_init, a_init, c_init, steps)
line, = ax.plot(t, population, lw=2, color='tab:blue')

ax.set_xlabel('Time step (t)')
ax.set_ylabel('Population (x)')
ax.set_title('Optimal Population Size Model')
ax.grid(True, linestyle='--', alpha=0.6)

# Define axes for sliders
ax_xop = plt.axes([0.2, 0.20, 0.65, 0.03])
ax_a   = plt.axes([0.2, 0.13, 0.65, 0.03])
ax_c   = plt.axes([0.2, 0.06, 0.65, 0.03])

# Create Sliders
s_xop = Slider(ax_xop, '$x_{op}$', 10.0, 100.0, valinit=x_op_init, valfmt='%.1f')
# if a > 1, population can grow; if a < 1, population will decline
s_a   = Slider(ax_a, '$a$', 1.0, 2.0, valinit=a_init, valfmt='%.3f') 
s_c   = Slider(ax_c, '$c$', 0.00001, 0.0005, valinit=c_init, valfmt='%.5f')

# Update function for sliders
def update(val):
    x_op = s_xop.val
    a = s_a.val
    c = s_c.val
    
    new_pop = run_simulation(x0_init, x_op, a, c, steps)
    line.set_ydata(new_pop)
    ax.relim()
    ax.autoscale_view(scalex=False, scaley=True)
    fig.canvas.draw_idle()

# Attach update sliders
s_xop.on_changed(update)
s_a.on_changed(update)
s_c.on_changed(update)

plt.show()
