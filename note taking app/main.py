import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QFileDialog, QInputDialog, QMessageBox, QListWidget, QListWidgetItem, QLineEdit, QAction, QMenu, QActionGroup, QLabel
from PyQt5.QtCore import Qt, QDate
from spellchecker import SpellChecker  # You need to install 'pyspellchecker' for grammar check
from datetime import datetime

class Note:
    def __init__(self, title, content, date):
        self.title = title
        self.content = content
        self.date = date

class NoteTakingApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.notes = []  # List to store notes
        self.current_note = None  # Currently selected note

        self.initUI()

    def initUI(self):
        # Create main widgets
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Create note list widget
        self.note_list_widget = QListWidget()
        self.note_list_widget.setSelectionMode(QListWidget.SingleSelection)
        self.note_list_widget.itemClicked.connect(self.show_selected_note)
        self.layout.addWidget(self.note_list_widget)

        # Create note editor widget
        self.note_editor_widget = QWidget()
        self.note_editor_layout = QVBoxLayout(self.note_editor_widget)

        self.title_edit = QLineEdit()
        self.note_editor_layout.addWidget(self.title_edit)

        self.content_edit = QTextEdit()
        self.note_editor_layout.addWidget(self.content_edit)

        self.layout.addWidget(self.note_editor_widget)

        # Create buttons for actions
        self.button_layout = QHBoxLayout()
        self.layout.addLayout(self.button_layout)

        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_note)
        self.button_layout.addWidget(self.save_button)

        self.delete_button = QPushButton("Delete")
        self.delete_button.clicked.connect(self.delete_note)
        self.button_layout.addWidget(self.delete_button)

        # Create menu bar
        self.menu_bar = self.menuBar()

        self.file_menu = self.menu_bar.addMenu("File")
        self.new_note_action = QAction("New Note", self)
        self.new_note_action.triggered.connect(self.new_note)
        self.file_menu.addAction(self.new_note_action)

        self.save_note_action = QAction("Save Note", self)
        self.save_note_action.triggered.connect(self.save_note)
        self.file_menu.addAction(self.save_note_action)

        self.edit_menu = self.menu_bar.addMenu("Edit")
        self.copy_action = QAction("Copy", self)
        self.copy_action.triggered.connect(self.copy_text)
        self.edit_menu.addAction(self.copy_action)

        self.paste_action = QAction("Paste", self)
        self.paste_action.triggered.connect(self.paste_text)
        self.edit_menu.addAction(self.paste_action)

        self.view_menu = self.menu_bar.addMenu("View")
        self.show_title_action = QAction("Show Titles", self)
        self.show_title_action.setCheckable(True)
        self.show_title_action.setChecked(True)
        self.show_title_action.triggered.connect(self.toggle_show_titles)
        self.view_menu.addAction(self.show_title_action)

        self.show_content_action = QAction("Show Content", self)
        self.show_content_action.setCheckable(True)
        self.show_content_action.setChecked(True)
        self.show_content_action.triggered.connect(self.toggle_show_content)
        self.view_menu.addAction(self.show_content_action)
        
        #create search bar.
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search Notes")
        self.search_bar.textChanged.connect(self.search_notes)
        self.layout.addWidget(self.search_bar)
        
        
        # Initialize spellchecker
        self.spellchecker = SpellChecker()

        # Set the main window properties
        self.setWindowTitle("Note Taking App")
        self.setGeometry(100, 100, 800, 600)
        
    def search_notes(self):
         search_query = self.search_bar.text().strip().lower()
         
         #filtering notes based on search query
         filtered_notes = [note for note in self.notes if
                           search_query in note.title.lower() or search_query in note.content.lower()]
         self.note_list_widget.clear()
         for note in filtered_notes:
             item = QListWidgetItem(note.title)
             self.note_list_widget.addItem(item)      
    def load_notes(self):
        try:
            with open('notes.json', 'r') as file:
                data = json.load(file)
                self.notes = [Note(note['title'], note['content'], note['date']) for note in data]
                self.update_note_list()
        except FileNotFoundError:
            self.notes = []
            
    def save_notes(self):
        data = [{'title': note.title, 'content': note.content, 'date': note.date} for note in self.notes]
        with open('notes.json', 'w') as file:
            json.dump(data, file)
            
    def new_note(self):
        title, ok = QInputDialog.getText(self, "New Note", "Enter Note Title:")
        if ok:
            self.title_edit.setText(title)
            self.content_edit.clear()
            self.current_note = None
            self.save_notes()

    def save_note(self):
        title = self.title_edit.text()
        content = self.content_edit.toPlainText()
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if self.current_note:
            self.current_note.title = title
            self.current_note.content = content
            self.current_note.date = date
            self.update_note_list()
        else:
            note = Note(title, content, date)
            self.notes.append(note)
            self.update_note_list()
            self.save_notes()

    def delete_note(self):
        if self.current_note:
            self.notes.remove(self.current_note)
            self.current_note = None
            self.title_edit.clear()
            self.content_edit.clear()
            self.update_note_list()
            self.save_notes()

    def show_selected_note(self, item):
        index = self.note_list_widget.currentRow()
        self.current_note = self.notes[index]
        self.title_edit.setText(self.current_note.title)
        self.content_edit.setPlainText(self.current_note.content)

    def update_note_list(self):
        self.note_list_widget.clear()
        for note in self.notes:
            item = QListWidgetItem(note.title)
            self.note_list_widget.addItem(item)

    def copy_text(self):
        selected_text = self.content_edit.textCursor().selectedText()
        if selected_text:
            clipboard = QApplication.clipboard()
            clipboard.setText(selected_text)

    def paste_text(self):
        clipboard = QApplication.clipboard()
        self.content_edit.insertPlainText(clipboard.text())

    def toggle_show_titles(self):
        self.note_list_widget.setVisible(self.show_title_action.isChecked())

    def toggle_show_content(self):
        self.content_edit.setVisible(self.show_content_action.isChecked())

def main():
    app = QApplication(sys.argv)
    window = NoteTakingApp()
    window.load_notes()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
