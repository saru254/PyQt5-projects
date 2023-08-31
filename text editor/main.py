import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QVBoxLayout, QWidget
from PyQt5.QtPrintSupport import QPrinter

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        # Create actions
        self.new_action = QAction("New", self)
        self.open_action = QAction("Open", self)
        self.print_action = QAction("Print", self)
        self.save_action = QAction("Save", self)
        self.save_as_action = QAction("Save As...", self)
        self.undo_action = QAction("Undo", self)
        self.redo_action = QAction("Redo", self)
        self.cut_action = QAction("Cut", self)
        self.copy_action = QAction("Copy", self)
        self.paste_action = QAction("Paste", self)
        self.exit_action = QAction("Exit", self)

        # Connect actions to functions
        self.new_action.triggered.connect(self.new_file)
        self.open_action.triggered.connect(self.open_file)
        self.save_action.triggered.connect(self.save_file)
        self.print_action.triggered.connect(self.print_file)
        self.save_as_action.triggered.connect(self.save_file_as)
        self.undo_action.triggered.connect(self.text_edit.undo)
        self.redo_action.triggered.connect(self.text_edit.redo)
        self.cut_action.triggered.connect(self.text_edit.cut)
        self.copy_action.triggered.connect(self.text_edit.copy)
        self.paste_action.triggered.connect(self.text_edit.paste)
        self.exit_action.triggered.connect(self.close)
       
       
       
       
        # Create a menu bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        file_menu.addAction(self.new_action)
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)
        file_menu.addAction(self.save_as_action)
        file_menu.addSeparator()
        file_menu.addAction(self.print_action)
        file_menu.addSeparator()
        file_menu.addAction(self.exit_action)

        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction(self.undo_action)
        edit_menu.addAction(self.redo_action)
        edit_menu.addSeparator()
        edit_menu.addAction(self.cut_action)
        edit_menu.addAction(self.copy_action)
        edit_menu.addAction(self.paste_action)
        

        self.setWindowTitle("Simple Text Editor")
        self.setGeometry(100, 100, 800, 600)
        self.current_file = None
        
    def print_file(self):
        printer =QPrinter(QPrinter.HighResolution)
        dialog = QPrinter(printer, self)
        if dialog.exec_() == QPrinter.Accepted:
            self.text_edit.print(printer)

    def new_file(self):
        self.text_edit.clear()

    def open_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_name:
            with open(file_name, "r") as file:
                self.text_edit.setPlainText(file.read())

    def save_file(self):
        if self.current_file:
            with open(self.current_file, "w") as file:
                file.write(self.text_edit.toPlainText())
        else:
            self.save_file_as()

    def save_file_as(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File As", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_name:
            with open(file_name, "w") as file:
                file.write(self.text_edit.toPlainText())
                self.current_file = file_name
    
    
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = TextEditor()
    editor.show()
    sys.exit(app.exec_())
