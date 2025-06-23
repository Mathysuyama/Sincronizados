import wx

# Define a classe da janela principal, herdando de wx.Frame
class MyFrame(wx.Frame):
    """
    Esta é a classe para a nossa janela principal.
    """
    def __init__(self):
        # Chama o construtor da classe pai (wx.Frame)
        super().__init__(parent=None, title='Minha Primeira Janela wxPython', size=(400, 300))
        
        # Adiciona um painel à janela para colocar widgets
        panel = wx.Panel(self)
        
        # Adiciona um texto estático (label) ao painel
        wx.StaticText(panel, label="Olá, wxPython!", pos=(130, 50))
        
        # Centraliza a janela na tela
        self.Centre()
        
        
        self.Bind(wx.EVT_CLOSE, self.on_close)

if __name__ == '__main__':
    # Cria a instância da aplicação
    app = wx.App()
    
    # Cria a instância da nossa janela
    frame = MyFrame()
    
    # Mostra a janela
    frame.Show()
    
    # Inicia o loop de eventos da aplicação
    app.MainLoop()
    
# Fim do código
# Este é um exemplo simples de uma janela usando wxPython.
    