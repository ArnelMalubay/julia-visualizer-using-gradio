# This file is the main application file to host the application logic

# Importing gradio and the plot_julia_set function from funcs.py
import gradio as gr
from funcs import plot_julia_set

# Adding an application header 
with gr.Blocks() as demo:
    gr.Markdown("""
    <div style="text-align: center; font-size: 18px;">
        <h1 style="font-size: 32px;">Julia Set Generator 🌌</h1>
        <p>Use this interactive tool to generate visualizations of Julia Sets!</p>
        <h3 style="font-size: 24px;">Instructions:</h3>
        <ol style="display: inline-block; text-align: left; font-size: 18px;">
            <li><strong>Input the Real and Imaginary parts</strong> of the complex number <code>c</code>.</li>
            <li><strong>Adjust the max iterations</strong> to control the detail and depth.</li>
            <li><strong>Adjust the pixel density</strong> to control the resolution.</li>
            <li><strong>Choose a colormap</strong> to customize the appearance.</li>
            <li>Click <strong>"Generate Plot"</strong> to render the image.</li>
            <li>For more info, see this <a href="https://github.com/ArnelMalubay/julia-visualizer-using-gradio" target="_blank">GitHub repository</a>.</li>
        </ol>
    </div>
    """)
    # Adding all the interactive components of the application
    with gr.Row():
        with gr.Column():
            real = gr.Textbox(label = 'Real Part', value = '0', interactive = True)
            imag = gr.Textbox(label = 'Imaginary Part', value = '0', interactive = True)
        with gr.Column():
            max_iter = gr.Slider(label = 'Specify the maximum number of iterations', minimum = 10, maximum = 2000, value = 500, step = 10, interactive = True)
            pixel_density = gr.Slider(label = 'Specify pixel density', minimum = 0.5, maximum = 2.5, value = 1.0, step = 0.1, interactive = True)

    colormap_choices = ['binary', 'inferno', 'magma', 'cividis', 'viridis', 'plasma', 'Pastel1', 'Pastel2', 'Paired', 'Accent', 'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern', 'rainbow', 'jet', 'turbo', 'gray', 'bone', 'pink', 'spring', 'summer', 'autumn', 'winter', 'cool', 'hot', 'copper']
    cmap = gr.Dropdown(label = 'Choose colormap', choices = colormap_choices, value = 'binary', interactive = True)

    submit = gr.Button('Generate Plot')

    with gr.Row():
        image = gr.Image(label = 'Julia Set', width = 600, height = 450, interactive = False)

    submit.click(fn = plot_julia_set, inputs = [real, imag, max_iter, pixel_density, cmap], outputs = image)

demo.launch()