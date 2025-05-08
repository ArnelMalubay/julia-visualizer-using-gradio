import gradio as gr
from funcs import plot_julia_set

def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

with gr.Blocks() as demo:
    with gr.Sidebar():
        real = gr.Textbox(label = 'Real Part', value = '0')
        imag = gr.Textbox(label = 'Imaginary Part', value = '0')
        max_iter = gr.Slider(label = 'Specify the maximum number of iterations', minimum = 10, maximum = 2000, value = 500, step = 10)
        pixel_density = gr.Slider(label = 'Specify pixel density', minimum = 0.5, maximum = 2.5, value = 1.0, step = 0.1)
        colormap_choices = ['binary', 'inferno', 'magma', 'cividis','viridis', 'plasma', 'Pastel1', 'Pastel2', 'Paired', 'Accent', 'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern', 'rainbow', 'jet', 'turbo', 'gray', 'bone', 'pink', 'spring', 'summer', 'autumn', 'winter', 'cool', 'hot', 'copper']
        cmap = gr.Dropdown(label = 'Choose colormap', choices = colormap_choices, value = 'binary')
        banding = gr.Checkbox(label = 'Enable color bands', value = True)
        show_tick_marks = gr.Checkbox(label = 'Show tick marks', value = False)
        #submit = gr.form_submit_button('Generate Plot') 

demo.launch()