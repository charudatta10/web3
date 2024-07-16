import os
import subprocess

if input("Do you want create directories? ")== "y":
    list_dirs = ["archive", "data", "src", "test"]
    for dir in list_dirs:
        if not os.path.exists(dir):
            print('Creating Directory: ' + dir)
            os.makedirs(dir)
            with open(os.path.join(dir, "__init__.py"), "w") as f:
                pass

        
if input("Do you want to create files? ")== "y":
    list_files = [".getattribute", ".gitignore", "license", "main.py", "requirement.txt"]
    for file in list_files:
        if not os.path.exists(file):
            print('Creating Files: ' + file)
            with open(file, "w") as f:
                pass  

if input("Is repo version controlled with git? ")== "y":
    subprocess.run(["git", "init"])

if input("Is repo is having mkdocs documentation? ")== "y": 
    subprocess.run(["mkdocs", "new", "."])

if input("Is repo configuration managed by dynaconf? ")== "y": 
    subprocess.run(["dynaconf", "init","-f","json"])

if input("Is readme and readmex needed to be generated? ")== "y":
    subprocess.run(["python", "C:/Users/chaitrali/Documents/GitHub/readme-generator/src/readme_generator.py"])
    
if input("Do you want to create assets directories? ")== "y":
    list_dirs = ["docs/assets","docs/assets/css", "docs/assets/img", "docs/assets/js"]
    for dir in list_dirs:
        if not os.path.exists(dir):
            print('Creating Directory: ' + dir)
            os.mkdir(dir) 

if input("Do you want to create initial commit? ")== "y":
    subprocess.run(["git", "add","."])
    subprocess.run(["git", "commit","-m","Initial commit"])
        
if input("Do you want create executable file?")== "y":
    file_name = input("Enter main file name: ")
    subprocess.run(["pyintsaller", f"src/{file_name}", "-onefile"])
