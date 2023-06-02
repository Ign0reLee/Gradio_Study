import gradio as gr

pil_img = gr.Image(shape=(100,100), type="pil")
np_img  = gr.Image(shape=(100,100), invert_colors=True,type="numpy")