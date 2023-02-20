import openai
import os
import sys
import json
from pathlib import Path
from PyQt5 import QtWidgets, QtCore

from program_1 import Title
from program_2 import create_file_structure
from program_3 import write_tree_file_structure
from p_4 import generate_code
from program_5 import create_files_from_text
# from app import MainWindow

class editor(QtWidgets.QMainWindow):


# Set up OpenAI API key
    with open("files/api.txt") as f:
        openai.api_key = f.read().strip()

# Create an instance of the Title class from program_1
title = Title()

# Create a simple editor using PyQt5
app = QtWidgets.QApplication([])
window = QtWidgets.QWidget()
window.setWindowTitle("NLP Code Editor")

# PROGRAM_1
def add_project():
    # Get the user input from the text entry field
    project_name = pr1.text()

    # Call the add_project method from the Title class in program_1 with the user input
    title.add_project(f"{project_name}")

    # Clear the text entry field
    pr1.setText("")

# PROGRAM_2
def create_files():
    # Set the name of the root directory
    # root_dir = 'projects'
    root_dir_0= pr2.text()
    root_dir = "projects/"+root_dir_0

    # Load the file structure from a JSON file
    with open('files/p1.txt', 'r') as f:
        file_structure = json.load(f)

    # Create the file structure in the current working directory.
    create_file_structure(root_dir, file_structure)

    # folder_path = Path('./projects')
    folder_path_0 = pr2.text()   
    folder_path = Path('./projects/'+folder_path_0)
    output_file_path = Path('files/p3.txt')
    write_tree_file_structure(folder_path, output_file_path)

# PROGRAM_3
def read_folder():
    # folder_path = Path('./projects')
    folder_path_0 = pr3.text()   
    folder_path = Path('./projects/'+folder_path_0)
    output_file_path = Path('files/p3.txt')
    write_tree_file_structure(folder_path, output_file_path)

#  PROGRAM_4
def generate_program():
    # Read input text from file
    with open('files/p3.txt', 'r') as file:
        input_text = file.read()

    # Set up GPT-3 prompt
    prompt = f"{input_text}. generate more code for each file."

    # Generate code and write to file
    generated_code = generate_code(prompt)
    with open('files/p4.txt', 'w') as file:
        file.write(generated_code)

#PROGRAM_5
def write_into_files():
    directory_0 = pr2.text() or pr3.text()
    directory = 'projects/'+directory_0

    create_files_from_text(directory, 'files/p4.txt')

# FOR PROGRAM_1
# Create a label1 and text entry field for user input
label1 = QtWidgets.QLabel("Enter project name:")
pr1 = QtWidgets.QLineEdit()
button = QtWidgets.QPushButton("Add Project")
button.clicked.connect(add_project)

# FOR PROGRAM_2
# Create a label2 and text entry field for user input
label2 = QtWidgets.QLabel("Enter project directory:")
pr2 = QtWidgets.QLineEdit()
file_button = QtWidgets.QPushButton("Create Files")
file_button.clicked.connect(create_files)

# FOR PROGRAM_3
# Create a label2 and text entry field for user input
label3 = QtWidgets.QLabel("update project directory:")
pr3 = QtWidgets.QLineEdit()
read_button = QtWidgets.QPushButton("read folder")
read_button.clicked.connect(read_folder)

# FOR PROGRAM_4
# Create a button to generate code
generate_button = QtWidgets.QPushButton("generate code")
generate_button.clicked.connect(generate_program)

# FOR PROGRAM_5
# Create a label and text entry field for user input
write_button = QtWidgets.QPushButton("Write into Files")
write_button.clicked.connect(write_into_files)

# Create a layout for the window
layout = QtWidgets.QVBoxLayout()
layout.addWidget(label1)
layout.addWidget(pr1)
layout.addWidget(button)
layout.addWidget(label2)
layout.addWidget(pr2)
layout.addWidget(file_button)
layout.addWidget(label3)
layout.addWidget(pr3)
layout.addWidget(read_button)
layout.addWidget(generate_button)
# layout.addWidget(label5)
# layout.addWidget(pr5)
layout.addWidget(write_button)
window.setLayout(layout)

window.show()
app.exec_()

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     main_window = MainWindow()
#     sys.exit(app.exec_())

