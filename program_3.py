import os
from pathlib import Path

def write_tree_file_structure(folder_path, output_file_path):
    with open(output_file_path, 'w') as output_file:
        write_tree_file_structure_helper(folder_path, output_file, 0)

def write_tree_file_structure_helper(folder_path, output_file, level):
    indent = '\t' * level
    output_file.write(f'{indent}{folder_path.name}/\n')

    for item in folder_path.iterdir():
        if item.is_file():
            output_file.write(f'{indent}\t{item.name}/\n')
        elif item.is_dir():
            write_tree_file_structure_helper(item, output_file, level + 1)

# if __name__ == '__main__':
#     folder_path = Path('./projects/E-commerce Website')
#     output_file_path = Path('p3.txt')
#     write_tree_file_structure(folder_path, output_file_path)
