import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QListWidget, QVBoxLayout, QWidget, QComboBox

class ToDoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List App")
        self.setGeometry(100, 100, 400, 500)
        self.setStyleSheet("background-color: lightblue;")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.task_input = QLineEdit(self)
        layout.addWidget(self.task_input)

        self.category_combo = QComboBox(self)
        self.category_combo.addItem("My Day")
        self.category_combo.addItem("Important")
        self.category_combo.addItem("Planned")
        self.category_combo.currentIndexChanged.connect(self.update_subcategories)
        layout.addWidget(self.category_combo)

        self.subcategory_combo = QComboBox(self)
        self.update_subcategories()  # Initialize subcategories based on the selected category
        layout.addWidget(self.subcategory_combo)

        self.add_button = QPushButton("Add Task", self)
        self.add_button.setStyleSheet("background-color: lightblue;")
        self.add_button.clicked.connect(self.add_task)
        layout.addWidget(self.add_button)

        self.task_list = QListWidget(self)
        layout.addWidget(self.task_list)

        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def update_subcategories(self):
        selected_category = self.category_combo.currentText()
        self.subcategory_combo.clear()

        if selected_category == "Planned":
            subcategories = ["Overdue", "Today", "Tomorrow", "This Week", "Later", "All Planned"]
            self.subcategory_combo.addItems(subcategories)

    def add_task(self):
        task_text = self.task_input.text()
        if task_text:
            category = self.category_combo.currentText()
            subcategory = self.subcategory_combo.currentText() if category == "Planned" else ""
            task = f"{category} - {subcategory}: {task_text}"
            self.task_list.addItem(task)
            self.task_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    todo_app = ToDoApp()
    todo_app.show()
    sys.exit(app.exec_())
