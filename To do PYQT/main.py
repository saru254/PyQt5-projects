import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QCheckBox, QComboBox, QCalendarWidget
from PyQt5.QtCore import Qt, QDate

class ToDoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List App")
        self.setGeometry(100, 100, 800, 600)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QHBoxLayout()
        self.central_widget.setLayout(self.layout)
        
        self.task_list = QListWidget()
        self.layout.addWidget(self.task_list)
        
        self.right_panel = QWidget()
        self.layout.addWidget(self.right_panel)
        self.right_layout = QVBoxLayout()
        self.right_panel.setLayout(self.right_layout)
        
        self.task_title = QLineEdit()
        self.right_layout.addWidget(QLabel("Task Title:"))
        self.right_layout.addWidget(self.task_title)
        
        self.task_description = QLineEdit()
        self.right_layout.addWidget(QLabel("Task Description:"))
        self.right_layout.addWidget(self.task_description)
        
        self.due_date = QCalendarWidget()
        self.right_layout.addWidget(QLabel("Due Date:"))
        self.right_layout.addWidget(self.due_date)
        
        self.priority_combo = QComboBox()
        self.priority_combo.addItems(["High", "Medium", "Low"])
        self.right_layout.addWidget(QLabel("Priority:"))
        self.right_layout.addWidget(self.priority_combo)
        
        self.add_button = QPushButton("Add Task")
        self.add_button.clicked.connect(self.add_task)
        self.right_layout.addWidget(self.add_button)
        
        #Dark mode.
        self.dark_mode_button = QPushButton("Dark Mode")
        self.dark_mode_button.clicked.connect(self.toggle_dark_mode)
        self.right_layout.addWidget(self.dark_mode_button)
        
        
        # Initial theme setup
        self.dark_mode = False
        self.set_light_theme()  # Default light mode
        
    def set_light_theme(self):
        app.setStyle("Fusion")
        palette = self.palette()
        palette.setColor(palette.Window, Qt.white)
        palette.setColor(palette.WindowText, Qt.black)
        palette.setColor(palette.Base, Qt.white)
        palette.setColor(palette.AlternateBase, Qt.lightGray)
        palette.setColor(palette.ToolTipBase, Qt.white)
        palette.setColor(palette.ToolTipText, Qt.black)
        palette.setColor(palette.Text, Qt.black)
        palette.setColor(palette.Button, Qt.lightGray)
        palette.setColor(palette.ButtonText, Qt.black)
        palette.setColor(palette.BrightText, Qt.red)
        palette.setColor(palette.Link, Qt.blue)
        palette.setColor(palette.Highlight, Qt.blue)
        palette.setColor(palette.HighlightedText, Qt.white)
        self.setPalette(palette)
        
    def set_dark_theme(self):
        app.setStyle("Fusion")
        palette = self.palette()
        palette.setColor(palette.Window, Qt.black)
        palette.setColor(palette.WindowText, Qt.white)
        palette.setColor(palette.Base, Qt.darkGray)
        palette.setColor(palette.AlternateBase, Qt.darkGray)
        palette.setColor(palette.ToolTipBase, Qt.black)
        palette.setColor(palette.ToolTipText, Qt.white)
        palette.setColor(palette.Text, Qt.white)
        palette.setColor(palette.Button, Qt.darkGray)
        palette.setColor(palette.ButtonText, Qt.white)
        palette.setColor(palette.BrightText, Qt.red)
        palette.setColor(palette.Link, Qt.blue)
        palette.setColor(palette.Highlight, Qt.blue)
        palette.setColor(palette.HighlightedText, Qt.white)
        self.setPalette(palette)
        
    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode
        if self.dark_mode:
            self.set_dark_theme()
        else:
            self.set_light_theme()
            
               
    def add_task(self):
        title = self.task_title.text()
        description = self.task_description.text()
        due_date = self.due_date.selectedDate().toString(Qt.ISODate)
        priority = self.priority_combo.currentText()
        
        task_info = f"Title: {title}\nDescription: {description}\nDue Date: {due_date}\nPriority: {priority}"
        self.task_list.addItem(task_info)
        
        self.task_title.clear()
        self.task_description.clear()
        self.due_date.setSelectedDate(QDate.currentDate())
        self.priority_combo.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    todo_app = ToDoApp()
    todo_app.show()
    sys.exit(app.exec_())
