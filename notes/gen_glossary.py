#!/usr/bin/python3
# AUTH: codenvibes
"""

"""


def generate_glossary():
    with open("glossary.md", "w") as readme:
        readme.write('<h1 align="center"><b>GLOSSARY</b></h1>')

        for letter in range(65, 91):
            readme.write('\n\n<br>\n\n## ' + chr(letter) + '\n')
            readme.write('<details>\n<summary><b><a href=" "> </a></b>')
            readme.write('</summary><br>\n\n\n<br><p align="center">')
            readme.write('※※※※※※※※※※※※</p><br>\n</details>\n\n')

if __name__ == "__main__":
    generate_glossary()