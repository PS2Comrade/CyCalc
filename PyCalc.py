import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 300, 400)

        # Layouts
        vbox = QVBoxLayout()
        hbox_input = QHBoxLayout()
        hbox_buttons = QVBoxLayout()

        # Input field
        self.input_field = QLineEdit()
        hbox_input.addWidget(self.input_field)

        # Buttons
        buttons = [
            ('7', self.on_click), ('8', self.on_click), ('9', self.on_click), ('/', self.on_click),
            ('4', self.on_click), ('5', self.on_click), ('6', self.on_click), ('*', self.on_click),
            ('1', self.on_click), ('2', self.on_click), ('3', self.on_click), ('-', self.on_click),
            ('0', self.on_click), ('.', self.on_click), ('=', self.calculate), ('+', self.on_click)
        ]

        for i in range(0, len(buttons), 4):
            hbox = QHBoxLayout()
            for j in range(4):
                button_text, handler = buttons[i + j]
                button = QPushButton(button_text)
                button.clicked.connect(handler)
                hbox.addWidget(button)
            hbox_buttons.addLayout(hbox)

        vbox.addLayout(hbox_input)
        vbox.addLayout(hbox_buttons)
        self.setLayout(vbox)

    def on_click(self):
        button = self.sender()
        current_value = self.input_field.text()
        new_value = current_value + button.text()
        self.input_field.setText(new_value)

    def calculate(self):
        try:
            result = eval(self.input_field.text())
            self.input_field.setText(str(result))
        except Exception:
            self.input_field.setText("Error")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())
