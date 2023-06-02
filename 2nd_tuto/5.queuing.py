import gradio as gr


def greet(name):
    return "Hello" + name + "!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text", theme=gr.themes.Monochrome())

with gr.Interface(greet, inputs="text", outputs="text",css=".gradio-container {background-color: red}") as demo:
    img = gr.Image("./data/cat.jpg").style(height="24", rounded=False)
    demo.queue(concurrency_count=3)
    demo.launch(share=True, auth=("username", "password"))


with gr.Blocks() as demo2:
    num1 = gr.Number()
    num2 = gr.Number()
    output = gr.Number()
    gr.Button("Add").click(
        lambda a, b: a + b, [num1, num2], output)
    gr.Button("Multiply").click(
        lambda a, b: a * b, [num1, num2], output, queue=True) # error
        #ValueError: The queue is enabled for event 1 but the queue has not been enabled for the app. 
        #Please call .queue() on your app. Consult https://gradio.app/docs/#blocks-queue for information on how to configure the queue.

demo2.launch()