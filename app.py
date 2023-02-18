import sys
import os
from PyQt5 import QtWidgets, QtGui, QtCore



class MainWindow(QtWidgets.QMainWindow):
    title = "My Text Editor"
    def __init__(self):
        super().__init__()

        self.setWindowTitle("NLP")
        self.setGeometry(100, 100, 800, 600)

        self.current_file = ""
        self.editor= ""
        # rest of the __init__ method code...
        # Create the central widget and main layout
        self.central_widget = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QHBoxLayout()
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)

        # Create the file menu
        file_menu = self.menuBar().addMenu("File")

        # Create actions for file menu
        new_file_action = QtWidgets.QAction("New File", self)
        new_file_action.setShortcut("Ctrl+N")
        new_file_action.triggered.connect(self.new_file)

        open_file_action = QtWidgets.QAction("Open File", self)
        open_file_action.setShortcut("Ctrl+O")
        open_file_action.triggered.connect(self.open_file)

        open_folder_action = QtWidgets.QAction("Open Folder", self)
        open_folder_action.triggered.connect(self.open_folder)

        save_action = QtWidgets.QAction("Save", self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.save_file)

        save_as_action = QtWidgets.QAction("Save As...", self)
        save_as_action.triggered.connect(self.save_file_as)

        exit_action = QtWidgets.QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)

        # Add actions to file menu
        file_menu.addAction(new_file_action)
        file_menu.addAction(open_file_action)
        file_menu.addAction(open_folder_action)
        file_menu.addAction(save_action)
        file_menu.addAction(save_as_action)
        file_menu.addAction(exit_action)

        # Create the file explorer
        self.file_explorer = QtWidgets.QTreeView()
        self.file_explorer.setFixedWidth(250)
        self.dir_model = QtWidgets.QFileSystemModel()
        self.dir_model.setRootPath(QtCore.QDir.rootPath())
        self.file_explorer.setModel(self.dir_model)
        self.file_explorer.setRootIndex(self.dir_model.index(QtCore.QDir.rootPath()))
        self.file_explorer.hide()

        # Connect the clicked signal of the file explorer to a method that opens the selected file in the editor field
        self.file_explorer.clicked.connect(self.open_file_from_explorer)

        # Create a toggle button to show/hide the file explorer
        self.toggle_button = QtWidgets.QPushButton(">")
        self.toggle_button.setFixedWidth(25)
        self.toggle_button.setCheckable(True)
        self.toggle_button.clicked.connect(self.toggle_file_explorer)

        # Add the file explorer and toggle button to the main layout
        self.main_layout.addWidget(self.toggle_button)
        self.main_layout.addWidget(self.file_explorer)

        # Create the text editor
        self.text_edit = QtWidgets.QTextEdit()
        self.main_layout.addWidget(self.text_edit)

        self.show()

    def new_file(self):
        self.current_file = ""
        self.text_edit.clear()

    def open_file(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "", "Text files (*.txt);;All files (*.*)")
        if filename:
            with open(filename, "r") as f:
                text = f.read()
                self.text_edit.setText(text)
            self.current_file = filename

    def open_folder(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Open Folder", "")
        if directory:
            self.dir_model.setRootPath(directory)
            self.file_explorer.setRootIndex(self.dir_model.index(directory))
            self.file_explorer.show()

    def toggle_file_explorer(self):
        if self.toggle_button.isChecked():
            self.file_explorer.show()
        else:
            self.file_explorer.hide()

    def save_file(self):
        if self.current_file:
            text = self.text_edit.toPlainText()
            with open(self.current_file, 'w') as f:
                f.write(text)
        else:
            self.save_file_as()
    
    def save_file_as(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save File As", "", "Text files (*.txt);;All Files (*)")
        if filename:
            text = self.text_edit.toPlainText()
            with open(filename, 'w') as f:
                f.write(text)
            self.current_file = filename
            self.setWindowTitle(f"{self.current_file} - {self.title}")

    
    def toggle_file_explorer(self):
        if self.file_explorer.isVisible():
            self.file_explorer.hide()
        else:
            self.file_explorer.show()
    
    def open_file_from_explorer(self, index):
        file_path = self.dir_model.filePath(index)
        if os.path.isfile(file_path):
            with open(file_path, "r") as f:
                text = f.read()
                self.text_edit.setText(text)
            self.current_file = file_path



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())
