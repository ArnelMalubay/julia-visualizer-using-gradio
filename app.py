import gradio as gr
from funcs import plot_julia_set

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            real = gr.Textbox(label = 'Real Part', value = '0', interactive = True)
            imag = gr.Textbox(label = 'Imaginary Part', value = '0', interactive = True)
        with gr.Column():
            max_iter = gr.Slider(label = 'Specify the maximum number of iterations', minimum = 10, maximum = 2000, value = 500, step = 10, interactive = True)
            pixel_density = gr.Slider(label = 'Specify pixel density', minimum = 0.5, maximum = 2.5, value = 1.0, step = 0.1, interactive = True)
    colormap_choices = ['binary', 'inferno', 'magma', 'cividis','viridis', 'plasma', 'Pastel1', 'Pastel2', 'Paired', 'Accent', 'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern', 'rainbow', 'jet', 'turbo', 'gray', 'bone', 'pink', 'spring', 'summer', 'autumn', 'winter', 'cool', 'hot', 'copper']
    cmap = gr.Dropdown(label = 'Choose colormap', choices = colormap_choices, value = 'binary', interactive = True)    
    submit = gr.Button('Generate Plot') 
    with gr.Row():
        image = gr.Image(label = 'Julia Set', width = 800, height = 600, interactive = False)
    submit.click(fn = plot_julia_set, inputs = [real, imag, max_iter, pixel_density, cmap], outputs = image)

demo.launch()