import wx

# Define a classe da janela principal, herdando de wx.Frame
class MyFrame(wx.Frame):
    """
    Uma janela demonstrando vários widgets comuns do wxPython.
    """
    def __init__(self):
        # O construtor do Frame, com um título e tamanho um pouco maiores
        super().__init__(parent=None, title='Demonstração de Widgets wxPython', size=(450, 500))
        
        # O Panel continua sendo a "tela" para os widgets
        panel = wx.Panel(self)
        
        # SIZER: Um sizer vertical para empilhar os widgets um sobre o outro.
        # Esta é a forma moderna de gerenciar layouts.
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # --- WIDGETS ---

        # 1. wx.StaticText: Um texto fixo, usado para labels e títulos.
        label = wx.StaticText(panel, label="Componentes Comuns do wxPython:")
        main_sizer.Add(label, 0, wx.ALL | wx.EXPAND, 10)

        # 2. wx.TextCtrl: Uma caixa de entrada de texto para o usuário.
        self.text_ctrl = wx.TextCtrl(panel, value="Escreva algo aqui...")
        main_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)

        # 3. wx.Button: Um botão clicável.
        button = wx.Button(panel, label="Clique em Mim")
        button.Bind(wx.EVT_BUTTON, self.on_button_click) # Conecta o clique a um método
        main_sizer.Add(button, 0, wx.ALL | wx.CENTER, 5)

        # 4. wx.CheckBox: Uma caixa de seleção (marcar/desmarcar).
        self.checkbox = wx.CheckBox(panel, label="Marque esta opção")
        main_sizer.Add(self.checkbox, 0, wx.ALL, 5)

        # 5. wx.ComboBox: Uma lista de opções suspensa (dropdown).
        opcoes = ['Opção 1', 'Opção 2', 'Opção 3']
        self.combo_box = wx.ComboBox(panel, choices=opcoes, style=wx.CB_READONLY)
        main_sizer.Add(self.combo_box, 0, wx.ALL | wx.EXPAND, 5)

        # 6. wx.Slider: Um controle deslizante para selecionar um valor numérico.
        self.slider = wx.Slider(panel, value=50, minValue=0, maxValue=100, style=wx.SL_HORIZONTAL | wx.SL_LABELS)
        main_sizer.Add(self.slider, 0, wx.ALL | wx.EXPAND, 5)

        # 7. wx.Gauge: Uma barra de progresso.
        self.gauge = wx.Gauge(panel, range=100, style=wx.GA_HORIZONTAL)
        main_sizer.Add(self.gauge, 0, wx.ALL | wx.EXPAND, 5)

        # --- FIM DOS WIDGETS ---

        # Aplica o sizer ao painel. Agora o sizer controla a posição de tudo.
        panel.SetSizer(main_sizer)
        
        self.Centre()
        self.Bind(wx.EVT_CLOSE, self.on_close)

    def on_button_click(self, event):
        """
        Executado quando o botão é clicado.
        Lê os valores de outros widgets e mostra uma caixa de diálogo.
        """
        text_value = self.text_ctrl.GetValue()
        checkbox_state = self.checkbox.IsChecked()
        combo_value = self.combo_box.GetValue()
        slider_value = self.slider.GetValue()

        # Atualiza a barra de progresso com o valor do slider
        self.gauge.SetValue(slider_value)

        # wx.MessageBox: Uma caixa de diálogo simples para mostrar informações.
        wx.MessageBox(
            f"Texto: {text_value}\n"
            f"Checkbox marcado: {checkbox_state}\n"
            f"Opção selecionada: {combo_value}\n"
            f"Slider em: {slider_value}%",
            "Informações dos Widgets",
            wx.OK | wx.ICON_INFORMATION
        )

    def on_close(self, event):
        """
        Executado quando a janela está prestes a ser fechada.
        """
        print("A janela está fechando. Finalizando tarefas...")
        self.Destroy()

if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame()
    frame.Show()
    app.MainLoop()