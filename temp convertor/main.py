import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
import math


class TempConverter(QWidget):
  def __init__(self):
    super().__init__()
    self.init_ui()


def init_ui(self):
  self.setWindowTitle("TEMPERATURE CONVERTER")
  self.setGeometry(100,100,300,150)
  self.label_celsius = QLabel("Enter Temp in Celsius:")
  self.input_celsius =QLineEdit()
  self.label_fahrenheit = QLabel("Temp in Fahrenheit:")
  self.result_fahreheit = QLabel("")
  


















if __name == "__main__":
  app = QApplication(sys.argv)
  temp = TempConverter()
  temp.show()
  sys.exit(app.exec_())
  
