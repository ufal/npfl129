import matplotlib.pyplot as plt
import numpy as np

from matplotlib.widgets import Slider

# Taken from gradient2
x_range = 100
num_samples = 100
num_noise = 20
mv = 35

f_x = np.random.rand(num_samples) * x_range - x_range / 2 + mv
f_y = np.array([i * 2 + np.random.normal(0, 10) + 5 for i in f_x]) # y = 2x + 5 + noise

## Interactive x slider
figure = plt.figure()
main_axes = figure.add_axes([0.05, 0.25, 0.9, 0.6])
shift_slider = Slider(
    ax=figure.add_axes([0.25, 0.15, 0.65, 0.03]),
    label='Shift factor',
    valmin=0,
    valmax=80,
    valinit=np.mean(f_x),
)
scale_slider = Slider(
    ax=figure.add_axes([0.25, 0.1, 0.65, 0.03]),
    label='Scale factor',
    valmin=0.1,
    valmax=50,
    valinit=np.std(f_x),
)

## Adapted from gradient2
def draw_loss_surface(xs, ys):
    lstsol = np.linalg.lstsq(np.stack([xs, np.ones(xs.size)], axis=1), ys, rcond=None)[0]
    delta = 0.2
    w = np.arange(lstsol[0] - 15, lstsol[0] + 15, delta)
    b = np.arange(lstsol[1] - 15, lstsol[1] + 15, delta)
    W, B = np.meshgrid(w, b)
    L =((W * np.expand_dims(xs, (1, 2)) + B - np.expand_dims(ys, (1, 2)))**2).mean(axis=0)
    main_axes.clear()
    main_axes.set_title("Loss surface after subtracting shift and dividing by scale", y=1.0)
    main_axes.set_aspect("equal")
    main_axes.set_xlim(w[0], w[-1])
    main_axes.set_ylim(b[0], b[-1])
    contour = main_axes.contour(W, B, L)
    main_axes.clabel(contour, inline=1, fontsize=10)
    main_axes.plot(lstsol[0], lstsol[1], 'bo')
    figure.canvas.draw_idle()
    
def update(*_):
    scale = scale_slider.val
    shift = shift_slider.val
    draw_loss_surface((f_x - shift) / scale, f_y)

update()
shift_slider.on_changed(update)
scale_slider.on_changed(update)
plt.show()