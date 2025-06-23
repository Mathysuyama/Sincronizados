import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit,
    QPushButton, QCheckBox, QComboBox, QSlider, QProgressBar, QMessageBox
)
from PyQt6.QtCore import Qt

class WidgetDemoWindow(QWidget):
    """
    Uma janela demonstrando vários widgets comuns do PyQt6.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Demonstração de Widgets PyQt6')
        self.resize(450, 500)

       # LAYOUT: Um layout vertical para empilhar os widgets.
        main_layout = QVBoxLayout()

        # --- WIDGETS ---

        # 1. QLabel: Um texto fixo, usado para labels e títulos.
        title_label = QLabel("Componentes Comuns do PyQt6:")
        main_layout.addWidget(title_label)

        # 2. QLineEdit: Uma caixa de entrada de texto.
        self.text_input = QLineEdit("Escreva algo aqui...")
        main_layout.addWidget(self.text_input)

        # 3. QPushButton: Um botão clicável.
        self.button = QPushButton("Clique em Mim")
        self.button.clicked.connect(self.on_button_click) # Conecta o sinal 'clicked' ao nosso método
        main_layout.addWidget(self.button)

        # 4. QCheckBox: Uma caixa de seleção.
        self.checkbox = QCheckBox("Marque esta opção")
        main_layout.addWidget(self.checkbox)

        # 5. QComboBox: Uma lista de opções suspensa (dropdown).
        self.combo_box = QComboBox()
        self.combo_box.addItems(['Opção 1', 'Opção 2', 'Opção 3'])
        main_layout.addWidget(self.combo_box)

        # 6. QSlider: Um controle deslizante.
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0, 100)
        self.slider.setValue(50)
        main_layout.addWidget(self.slider)

        # 7. QProgressBar: Uma barra de progresso.
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        main_layout.addWidget(self.progress_bar)

        # --- FIM DOS WIDGETS ---

        # Adiciona um espaço flexível para empurrar os widgets para cima
        main_layout.addStretch()

        # Define o layout principal da janela
        self.setLayout(main_layout)

    def on_button_click(self):
    
        """
        Executado quando o botão é clicado (slot).
        Lê os valores de outros widgets e mostra uma caixa de diálogo.
        """
        
        text_value = self.text_input.text()
        checkbox_state = self.checkbox.isChecked()
        combo_value = self.combo_box.currentText()
        slider_value = self.slider.value()

        # Atualiza a barra de progresso com o valor do slider
        self.progress_bar.setValue(slider_value)

        # QMessageBox: Uma caixa de diálogo para mostrar informações.
        QMessageBox.information(
            self,
            "Informações dos Widgets",
            f"Texto: {text_value}\n"
            f"Checkbox marcado: {checkbox_state}\n"
            f"Opção selecionada: {combo_value}\n"
            f"Slider em: {slider_value}%"
        )
        
         
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WidgetDemoWindow()
    window.show()
    sys.exit(app.exec())