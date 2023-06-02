import gradio as gr

def greet(name, is_morning, temperature):
    salutation = "Good Morning" if is_morning else "Good evening"
    greetring  = f"{salutation} {name}. It is {temperature} degrees today"
    celsius    = (temperature -32) * 5 / 9
    return greetring, celsius

demo = gr.Interface(fn=greet, 
                    inputs=["text", "checkbox", gr.Slider(0, 100)], 
                    outputs=["text", "number"])
demo.launch()