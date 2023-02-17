import os

def create_files_from_text(directory, filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.html') or file.endswith('.css') or file.endswith('.js') or file.endswith('.py') or file.endswith('.java') or file.endswith('.txt'):
                    with open(os.path.join(root, file), 'w') as f_out:
                        for i, line in enumerate(lines):
                            line = line.strip()
                            if line.startswith('//') and line.endswith('//'):
                                line = line[2:-2]  # remove comment delimiters
                            
                            elif line.startswith('<!--') and line.endswith('-->'):
                                line = line[5:-4]  # remove comment delimiters
                            elif line.startswith('#') or line.startswith('/'):
                                line = line[1:]  # remove comment delimiters 
                            elif line.startswith('#') or line.startswith('/'):
                                line = line.split()[1]  # remove comment delimiters
                            if line == file:
                                code = []
                                j = i + 1
                                while j < len(lines):
                                    next_line = lines[j].strip()
                                    if next_line.startswith('//') and next_line.endswith('//') or next_line.startswith('/') and next_line.endswith('/') or next_line.startswith('#') or next_line.startswith('/') or next_line.startswith('<!--') and next_line.endswith('-->'):
                                        break  # stop if a comment delimiter is encountered
                                    if next_line.endswith('.html') or next_line.endswith('.css') or next_line.endswith('.js') or next_line.endswith('.java') or next_line.endswith('.py') or next_line.endswith('.jpg') or next_line.endswith('.png') or next_line.endswith('.gif') or next_line.endswith('.txt'):
                                        break  # stop if the next file name is encountered
                                    code.append(next_line)
                                    j += 1
                                f_out.write('\n'.join(code))
                                break



# create_files_from_text('./projects/E-commerce Website', 'files/p4.txt')

# import os

# def create_files_from_text(directory, filename):
#     with open(filename, 'r') as f:
#         lines = f.readlines()
#         for root, dirs, files in os.walk(directory):
#             for file in files:
#                 if file.endswith('.html') or file.endswith('.css') or file.endswith('.js') or file.endswith('.py'):
#                     with open(os.path.join(root, file), 'w') as f_out:
#                         for i, line in enumerate(lines):
#                             if file.strip('/') == line.strip().strip('/').split('/')[-1].strip():
#                                 code = []
#                                 j = i + 1
                                
#                                 while j < len(lines) and not lines[j].strip().endswith((".html", ".css", ".js", ".py")):
#                                     code.append(lines[j].strip())
#                                     j += 1
#                                 f_out.write("\n".join(code))
#                                 break




# create_files_from_text('./nlp_code_editor/Hand_Gesture_Detection', 'p4.txt')


# import os

# def create_files_from_text(directory, filename):
#     with open(filename, 'r') as f:
#         lines = f.readlines()
#         for root, dirs, files in os.walk(directory):
#             for file in files:
#                 if file.endswith('.html') or file.endswith('.css') or file.endswith('.js') or file.endswith('.py'):
#                     with open(os.path.join(root, file), 'w') as f_out:
#                         for i, line in enumerate(lines):
#                             if line.startswith(file):
#                                 code = []
#                                 j = i + 1
#                                 while j < len(lines) and not any(lines[j].strip().endswith(ext) for ext in ['.html', '.css', '.js', '.py', '.jpg', '.png', '.gif','.java']):

#                                     code.append(lines[j].strip())
#                                     j += 1
#                                 f_out.write("\n".join(code))
#                                 break


# create_files_from_text('./nlp_code_editor/Portfolio Website', 'p4.txt')
