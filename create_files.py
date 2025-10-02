import os
import shutil

import pypandoc
import yaml

# Load config from config.yaml
with open("./config.yaml", "r") as file:
    config = yaml.safe_load(file)

source_folders = [course_spec.get("language","") for course_spec in config['courses']]

HTML_OUTPUT_DIR = './output/output_html'

def create_folder(path):
    dir_path = os.path.dirname(path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


for source_folder in source_folders:
    for doc in os.listdir(f"./src/{source_folder}"):
        doc_path = os.path.join(f"./src/{source_folder}", doc)
        html_path = os.path.join(HTML_OUTPUT_DIR, source_folder, doc.replace("md", "html"))
        create_folder(html_path)
        output = pypandoc.convert_file(
            source_file=doc_path,
            to='html',
            outputfile=html_path,
            extra_args=['-s', '--css=style.css']
        )


shutil.copytree("src/img", "output/output_html/img")

for folder in source_folders:
    shutil.copy2("style.css", f"output/output_html/{folder}/style.css")

