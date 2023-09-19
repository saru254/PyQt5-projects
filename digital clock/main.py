import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QTimeEdit, QSlider, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer, QTime, QDate, Qt

class DigitalClockApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Digital Clock")
        self.setGeometry(100, 100, 400, 250)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.clock_label = QLabel(self)
        layout.addWidget(self.clock_label)
        self.clock_label.setStyleSheet("font-size: 36pt")

        self.date_label = QLabel(self)
        layout.addWidget(self.date_label)

        self.alarm_time_edit = QTimeEdit(self)
        layout.addWidget(self.alarm_time_edit)

        self.set_alarm_button = QPushButton("Set Alarm", self)
        layout.addWidget(self.set_alarm_button)
        self.set_alarm_button.clicked.connect(self.set_alarm)

        self.brightness_slider = QSlider(Qt.Horizontal, self)
        layout.addWidget(self.brightness_slider)
        self.brightness_slider.setMinimum(0)
        self.brightness_slider.setMaximum(100)
        self.brightness_slider.setValue(100)  # Default brightness
        self.brightness_slider.valueChanged.connect(self.set_brightness)

        self.alarm_timer = QTimer(self)
        self.alarm_timer.timeout.connect(self.check_alarm)

        self.update_clock()
        self.update_date()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)  # Update clock every 1 second

    def update_clock(self):
        current_time = QTime.currentTime()
        self.clock_label.setText(current_time.toString("hh:mm:ss"))

    def update_date(self):
        current_date = QDate.currentDate()
        self.date_label.setText(current_date.toString("dddd, MMMM d, yyyy"))

    def set_alarm(self):
        alarm_time = self.alarm_time_edit.time()
        self.alarm_timer.start(1000)
        self.alarm_time = alarm_time

    def check_alarm(self):
        current_time = QTime.currentTime()
        if current_time == self.alarm_time:
            print("Alarm triggered!")
            self.alarm_timer.stop()

    def set_brightness(self):
        brightness = self.brightness_slider.value()
        brightness_pct = brightness / 100.0
        self.setStyleSheet(f"background-color: rgba(255, 255, 255, {brightness_pct});")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock_app = DigitalClockApp()
    clock_app.show()
    sys.exit(app.exec_())
