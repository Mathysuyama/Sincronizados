import PySimpleGUI as sg

# Define um tema visual para a janela
sg.theme('SystemDefaultForReal')

# 1. Define o layout da janela. Cada elemento tem uma 'key' para identificação.
layout = [
    # sg.Text: Um texto fixo, usado para labels e títulos.
    [sg.Text("Componentes Comuns do PySimpleGUI")],
    
    # sg.Input: Uma caixa de entrada de texto.
    [sg.Text("Caixa de Texto:"), sg.Input(default_text="Escreva algo aqui...", key='-INPUT-')],
    
    # sg.Checkbox: Uma caixa de seleção.
    [sg.Checkbox("Marque esta opção", default=False, key='-CHECKBOX-')],
    
    # sg.Combo: Uma lista de opções suspensa (dropdown).
    [sg.Text("Dropdown:"), sg.Combo(['Opção 1', 'Opção 2', 'Opção 3'], default_value='Opção 1', readonly=True, key='-COMBO-')],
    
    # sg.Slider: Um controle deslizante.
    [sg.Text("Slider:"), sg.Slider(range=(0, 100), default_value=50, orientation='h', key='-SLIDER-')],
    
    # sg.ProgressBar: Uma barra de progresso.
    [sg.Text("Progresso:"), sg.ProgressBar(100, orientation='h', size=(20, 20), key='-PROGRESS-')],
    
    # sg.Button: Um botão clicável.
    [sg.Button("Executar Ação", key='-BUTTON-'), sg.Button("Sair")]
]

# 2. Cria a janela com o layout definido
window = sg.Window('Demonstração de Widgets PySimpleGUI', layout)

# 3. Loop de eventos para ler as interações do usuário
while True:
    event, values = window.read()
    
    # Se o usuário fechar a janela ou clicar em "Sair"
    if event == sg.WIN_CLOSED or event == 'Sair':
        break
        
    # Se o usuário clicar no botão "Executar Ação"
    if event == '-BUTTON-':
        # Lê os valores de cada widget usando suas chaves
        text_value = values['-INPUT-']
        checkbox_state = values['-CHECKBOX-']
        combo_value = values['-COMBO-']
        slider_value = int(values['-SLIDER-']) # O valor do slider vem como float

        # Atualiza a barra de progresso com o valor do slider
        window['-PROGRESS-'].update(slider_value)
        
        # sg.popup: Uma forma fácil de mostrar uma caixa de diálogo
        sg.popup(
            f"Texto: {text_value}\n"
            f"Checkbox marcado: {checkbox_state}\n"
            f"Opção selecionada: {combo_value}\n"
            f"Slider em: {slider_value}%",
            title="Informações dos Widgets"
        )

# 4. Fecha a janela ao sair do loop
window.close()