import gradio as gr
import random

def classify_shops(number):
    shops = int(random.randint(0,number//100)) + number //10
    return shops

if __name__ == '__main__':
    theme = gr.themes.Soft()

    with gr.Blocks(theme=theme) as block:
        gr.Markdown("## tasks for exseed")
        
        gr.Markdown("###  Choose your budget")
        input = gr.Slider(minimum=500, maximum=10000, value=3000, label="", step=500, interactive=True)
        output = gr.Textbox(label="The number of shops found")
        input.change(classify_shops, input, output, "found")
        
        with gr.Row():
            input
            output
        
    block.launch()
