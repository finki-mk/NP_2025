import os

import yaml

with open("./config.yaml", "r") as file:
    config = yaml.safe_load(file)

source_folders = [course_spec.get("language", "") for course_spec in config['courses']]


def generate_index(course_spec: dict, html_files_directory: str):
    is_en = course_spec['language'] == 'en'

    html_files = [filename for filename in os.listdir(html_files_directory) if
                  filename.endswith('.html') and not filename.startswith("index")]
    html_files.sort(key=lambda el: int(el.split(".")[0]))  # Sort the filenames numerically

    index_content = '<html>\n<head>\n<meta charset="utf-8" />\n<title>Index</title>\n<link rel="stylesheet" href="style.css" />\n</head>\n<body>\n'
    index_content += '<img src="../img/logo_mk.png">'
    index_content += f'<h1>Аудиториски вежби по {course_spec["title"]}</h1>\n' if not is_en \
        else f'<h1>Auditory exercises in {course_spec["title"]}</h1>\n'

    index_content += f'<h2>Содржина</h2>\n' if not is_en else "<h2>Content</h2>"

    for filename in html_files:
        index_content += f'<a href="{filename}">{"Аудиториска вежба бр." if not is_en else "Auditory exercise #"} {filename.replace(".html", "")}</a><br>\n'

    index_content += '</body>\n</html>'

    with open(os.path.join(html_files_directory, 'index.html'), 'w') as index_file:
        index_file.write(index_content)


if __name__ == "__main__":
    for course_spec in config['courses']:
        generate_index(course_spec=course_spec, html_files_directory=f"./output/output_html/{course_spec['language']}")
