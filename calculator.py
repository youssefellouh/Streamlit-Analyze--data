import gradio as gr

def calculate(operation, num1, num2):
    if operation == "Addition":
        return num1 + num2
    elif operation == "Soustraction":
        return num1 - num2
    elif operation == "Multiplication":
        return num1 * num2
    elif operation == "Division":
        if num2 != 0:
            return num1 / num2
        else:
            return "Erreur : Division par zéro"

# Création de l'interface Gradio
with gr.Blocks() as demo:
    gr.Markdown("# Calculatrice Simple")
    
    operation = gr.Radio(label="Choisir l'opération", choices=["Addition", "Soustraction", "Multiplication", "Division"])
    num1 = gr.Number(label="Nombre 1")
    num2 = gr.Number(label="Nombre 2")
    
    calculate_button = gr.Button("Calculer")
    result = gr.Textbox(label="Résultat", interactive=False)
    
    calculate_button.click(calculate, inputs=[operation, num1, num2], outputs=result)

# Lancement de l'application
demo.launch()
