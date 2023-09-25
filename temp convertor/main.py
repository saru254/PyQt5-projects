import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class TemperatureConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Temperature Converter")
        self.setGeometry(100, 100, 300, 150)

        self.label_celsius = QLabel("Enter Temperature in Celsius:")
        self.input_celsius = QLineEdit()
        self.label_fahrenheit = QLabel("Temperature in Fahrenheit:")
        self.result_fahrenheit = QLabel("")

        self.convert_button = QPushButton("Convert")
        self.convert_button.clicked.connect(self.convert_temperature)

        layout = QVBoxLayout()
        layout.addWidget(self.label_celsius)
        layout.addWidget(self.input_celsius)
        layout.addWidget(self.label_fahrenheit)
        layout.addWidget(self.result_fahrenheit)
        layout.addWidget(self.convert_button)

        self.setLayout(layout)

    def convert_temperature(self):
        try:
            celsius = float(self.input_celsius.text())
            fahrenheit = (celsius * 9/5) + 32
            self.result_fahrenheit.setText(f"Result: {fahrenheit:.2f} °F")
        except ValueError:
            self.result_fahrenheit.setText("Invalid input. Please enter a number.")

def main():
    app = QApplication(sys.argv)
    converter = TemperatureConverter()
    converter.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
