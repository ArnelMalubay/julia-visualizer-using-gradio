# Julia Set Visualizer using Gradio
This is a simple Gradio implementation of my Julia Set visualizer previously implemented and deployed in Streamlit.

<p align="center"><img src="assets/app_screenshot.png" width="700"/></p>

Accessing the App
=================

To access this app, you can either

1. Clone the repository. Then, run 

`pip install -r requirements.txt`

on the terminal. It is ideal to create a virtual environment first before proceeding to the installation of the required libraries. Once done, you can then run

`python app.py`

on the terminal and use the app on your local server.

OR

Access the app via HuggingFace Spaces through this link (to add).

2. Once you have access to the app, you can then input any complex number `c` that you want to generate the Julia set of the function `f(z) = z^2 + c`. 

### Recommended Julia Set Seeds

These complex numbers are known to generate visually interesting Julia sets:

| Real Part      | Imaginary Part   |
|----------------|------------------|
| -0.1156437876  | 0.8690819138     |
| -0.7269        | 0.1889           |
| -0.5125114984  | 0.5212955731     |
| -0.4           | 0.6              |
| -0.5012149299  | -0.5637838176    |
| 0              | -0.8             |
| -0.8           | 0.156            |
| -0.7773672345  | -0.1782126754    |
| -0.06353957916 | -0.6992547595    |
| -0.5064253507  | 0.5981400301     |
| 0.2803481964   | -0.5273108717    |