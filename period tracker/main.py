# typical imports for period tracker

import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QCalendarWidget, QVBoxLayout, QWidget, QFormLayout, QComboBox
from PyQt5.QtCore import Qt, Qdate, QTimer
from PyQt5.QtGui import QIcon

class period_tracker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Period Tracker App")
        self.setGeometry(100,100,800,600)