import openai
import os
import tkinter as tk
import json
from pathlib import Path

from program_1 import Title
from program_2 import create_file_structure
from program_3 import write_tree_file_structure
from program_4 import generate_code
from program_5 import create_files_from_text

# Set up OpenAI API key
with open("files/api.txt") as f:
    openai.api_key = f.read().strip()

# Create an instance of the Title class from program_1
title = Title()

# Create a simple editor using Tkinter
root = tk.Tk()
root.title("Simple Editor")

# PROGRAM_1
def add_project():
    # Get the user input from the text entry field
    project_name = pr1.get()

    # Call the add_project method from the Title class in program_1 with the user input
    title.add_project(f"{project_name}")

    # Clear the text entry field
    pr1.delete(0, tk.END)

# PROGRAM_2
def create_files():
    # Set the name of the root directory
    # root_dir = 'projects'
    root_dir_0= pr2.get()
    root_dir = "projects/"+root_dir_0

    # Load the file structure from a JSON file
    with open('files/p1.txt', 'r') as f:
        file_structure = json.load(f)

    # Create the file structure in the current working directory.
    create_file_structure(root_dir, file_structure)

    # folder_path = Path('./projects')
    folder_path_0 = pr2.get()   
    folder_path = Path('./projects/'+folder_path_0)
    output_file_path = Path('files/p3.txt')
    write_tree_file_structure(folder_path, output_file_path)

# PROGRAM_3
def read_folder():
    # folder_path = Path('./projects')
    folder_path_0 = pr3.get()   
    folder_path = Path('./projects/'+folder_path_0)
    output_file_path = Path('files/p3.txt')
    write_tree_file_structure(folder_path, output_file_path)

#  PROGRAM_4
def generate_program():
    # Read input text from file
    with open('files/p3.txt', 'r') as file:
        input_text = file.read()

    # Generate code using recursion
    generated_code = generate_code(input_text)

    # Write generated code to file
    with open('files/p4.txt', 'w') as file:
        file.write(generated_code)

#PROGRAM_5
def write_into_files():
    directory_0 = pr5.get()
    directory = 'projects/'+directory_0

    create_files_from_text(directory, 'files/p4.txt')

# FOR PROGRAM_1
# Create a label1 and text entry field for user input
label1 = tk.Label(root, text="Enter project name:")
label1.pack(side=tk.LEFT)
pr1 = tk.Entry(root)
pr1.pack(side=tk.LEFT)

# Create a button to submit user input and call the add_project function
button = tk.Button(root, text="Add Project", command=add_project)
button.pack(side=tk.LEFT)

# FOR PROGRAM_2
# Create a label2 and text entry field for user input
label2 = tk.Label(root, text="Enter project directory:")
label2.pack(side=tk.LEFT)
pr2 = tk.Entry(root)
pr2.pack(side=tk.LEFT)

# Create a button to create the file structure
file_button = tk.Button(root, text="Create Files", command=create_files)
file_button.pack(side=tk.LEFT)

# FOR PROGRAM_3
# Create a label2 and text entry field for user input
label3 = tk.Label(root, text="update project directory:")
label3.pack(side=tk.LEFT)
pr3 = tk.Entry(root)
pr3.pack(side=tk.LEFT)

# Create a button to create the file structure
file_button = tk.Button(root, text="read folder", command=read_folder)
file_button.pack(side=tk.LEFT)

# FOR PROGRAM_4

# Create a button to create the file structure
file_button = tk.Button(root, text="generate code", command=generate_program)
file_button.pack(side=tk.LEFT)

# FOR PROGRAM_5
# Create a label2 and text entry field for user input
label5 = tk.Label(root, text="update project directory:")
label5.pack(side=tk.LEFT)
pr5 = tk.Entry(root)
pr5.pack(side=tk.LEFT)

# Create a button to create the file structure
file_button = tk.Button(root, text="write", command=write_into_files)
file_button.pack(side=tk.LEFT)


# Call the display_title method from the Title class in program_1 to show any existing projects
title.display_title()

# Start the main loop for the simple editor
root.mainloop()
