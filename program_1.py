import openai
import os

with open("api.txt") as f:
    openai.api_key = f.read().strip()

class Title:
    def __init__(self):
        self.projects = []



    def add_project(self, project_name):
        completions = openai.Completion.create(
            engine="text-davinci-002",
            prompt="Create file structure(The structure should be represented as a dictionary in Python with title of the project within curly braces, with each directory represented as a nested dictionary and each file represented as a key with an empty string as the value ,property name should be enclosed in double quotes ) for {} ".format(project_name),
            max_tokens=500,
            n=1,
            stop=None,
            temperature=0.5,
        )
        code = completions.choices[0].text
        self.projects.append((project_name, code))
        self.write_to_file(project_name, code)

    def remove_project(self, project_name):
        for index, project in enumerate(self.projects):
            if project[0] == project_name:
                self.projects.pop(index)
                os.remove("{}.txt".format(project_name))
                break

    def display_title(self):
        for project in self.projects:
            print("Project: {}\nCode:\n{}\n".format(project[0], project[1]))

    def write_to_file(self, project_name, code):
        with open("p1.txt".format(project_name), "w") as f:
            f.write(code)

title = Title()
# title.add_project("portfolio website")
title.display_title()
