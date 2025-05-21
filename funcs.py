# This file contains all the functions needed for plotting the Julia set.

# Importing necessary libraries
import numpy as np
from numba import vectorize
from matplotlib.colors import LogNorm
from matplotlib import cm
import gradio as gr

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
def plot_julia_set(real, imag, max_iter = 500, pixel_density = 1.0, cmap = 'magma'):
  try:
    c = complex(float(real), float(imag))
    stabilities = get_stability_map(c = c, max_iter = max_iter, pixel_density = pixel_density)
    # Normalize values for log scaling; induces image banding
    norm = LogNorm(vmin = 1 / max_iter, vmax = 1.0)
    normalized = norm(stabilities)  # Now between 0 and 1, log-scaled
    # Apply colormap
    rgba_img = cm.get_cmap(cmap)(normalized)  # shape (H, W, 4), values in [0, 1]
    # Drop alpha channel and convert to uint8
    rgb_img = (rgba_img[:, :, :3] * 255).astype("uint8")
    return rgb_img  # NumPy array
  except Exception as e:
    raise gr.Error(f"Error generating image: {e}")