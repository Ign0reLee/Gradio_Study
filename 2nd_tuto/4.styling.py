import gradio as gr


def greet(name):
    return "Hello" + name + "!"

# demo = gr.Interface(fn=greet, inputs="text", outputs="text", theme=gr.themes.Monochrome())

with gr.Interface(greet, inputs="text", outputs="text",css=".gradio-container {background-color: red}")as demo:
    img = gr.Image("./data/cat.jpg").style(height="24", rounded=False)
    demo.launch(share=True, auth=("username", "password"))