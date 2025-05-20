# This file contains all the functions needed for plotting the Julia set.

# Importing necessary libraries
import numpy as np
from numba import vectorize
from matplotlib.colors import LogNorm
from matplotlib import cm
import matplotlib.pyplot as plt
import copy
from PIL import Image
from io import BytesIO

# This is a vectorized implementation (via numba) of the escape-time algorithm (with threshold = 2). 
@vectorize
def stability(z, c, max_iter):
  z_i = z
  for i in range(max_iter):
    z_i = z_i**2 + c
    if abs(z_i) >= 2:
      return (i+1)/max_iter 
    else:
      i += 1 
  return 1.0

# This computes for the normalized escape counts for a grid of complex numbers.
def get_stability_map(c, max_iter = 100, pixel_density = 1):
    x = np.linspace(-1.5, 1.5, int(1000 * pixel_density))
    y = np.linspace(-1.25, 1.25, int(750 * pixel_density))
    z = x[np.newaxis, :] + y[:, np.newaxis] * 1j
    return np.flipud(stability(z, c, max_iter))

# This plots the Julia set of a given complex number c.
def plot_julia_set(real, imag, max_iter = 500, pixel_density = 1.0, cmap = 'magma', banding = True, show_tick_marks = False):
  try:  
    c = complex(float(real), float(imag))
    stabilities = get_stability_map(c = c, max_iter = max_iter, pixel_density = pixel_density)

    fig, ax = plt.subplots(figsize = (8, 6), dpi = 100)
    if banding:
        my_cmap = copy.copy(cm.get_cmap(cmap))
        my_cmap.set_bad(eval(f'cm.{cmap}({1/max_iter})'))
        ax.imshow(stabilities, cmap = my_cmap, norm = LogNorm(), interpolation = None, aspect = 1.25 / 1.5)
    else:
        ax.imshow(stabilities, cmap = cmap, aspect = 1.25 / 1.5)

    if show_tick_marks:
        xtick_labels = np.linspace(-1.5, 1.5, 6)
        ax.set_xticks([(int(1000 * pixel_density) / 3) * (x + 1.5) for x in xtick_labels],
                      labels=['{:.1f}'.format(xtick) for xtick in xtick_labels])
        ytick_labels = np.linspace(-1.25, 1.25, 6)
        ax.set_yticks([-(int(750 * pixel_density) / 2.5) * (y - 1.25) for y in ytick_labels],
                      labels=['{:.1f}'.format(ytick) for ytick in ytick_labels])
    else:
        ax.set_xticks([])
        ax.set_yticks([])

    # Remove whitespace and axes
    plt.axis('off')
    fig.tight_layout(pad=0)

    # Save figure to buffer
    buf = BytesIO()
    fig.savefig(buf, format = 'png', bbox_inches = 'tight', pad_inches = 0)
    buf.seek(0)

    # Close the figure to free memory
    plt.close(fig)

    # Convert buffer to PIL Image
    return Image.open(buf)
  except:
     return 