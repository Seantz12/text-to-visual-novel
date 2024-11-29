from zipfile import ZipFile
from parse import Parser
from wikipedia_extractor import *

import argparse
import os
import re
import shutil
import sys

def insert_script(script):
   with open('base_script.rpy', 'r') as file:
      file_contents = file.read()

      updated_contents = file_contents.replace('script', script)

   with open('script.rpy', 'w') as file:
      file.write(updated_contents)

def postparse_script(script):
    # need to replace things like escape characters
    escape_characters = ['%', '"', "'", '\\']

    script = re.sub(r'([\[\]%"\'\\])', r'\\\1', script)
    return script

def generate_script(sections):
    max_lines = 6
    script = ""
    for section in sections:
        section_title = section[0]
        parser = section[1]
        content = parser.parsed
        line_count = 0
        script += section_title + "\n\n"
        for paragraph in content:
            for sentence in paragraph:
                script += sentence
                script += "\n\n"
            script += "{clear}"
            script += "\n\n"
        script += "{clear}"
        script += "\n\n"
    return postparse_script(script)
        


if __name__ == "__main__":
    print("this is a test starting script!")
    print("if you're reading this, this is just a way for me to test out the basic structure")
    print("surely by the time i release this i will have a gui interface")

    sections = get_parsers_from_page_title("Visual Novel")
    script = generate_script(sections)
    insert_script(script)

    parser = argparse.ArgumentParser(
        prog='TTVN',
        description='Generate a visual novel from some text',
    )
    parser.add_argument('-d', '--directory')
    args = parser.parse_args()
    path = args.directory
    print(path)
    if not os.path.exists(path):
        print("wtf use a valid directory, i'll make an option to create one later")
        exit(1)

    if os.path.exists(f'{path}/TTVN-1.0-pc'):
        # DELETE IT
        shutil.rmtree(f'{path}/TTVN-1.0-pc')

    
    with ZipFile('TTVN-1.0-pc.zip', 'r') as zip:
        zip.extractall(path=path)

    print('now we gotta modify the script in the extracted directory...')
    script_path = f'{path}/TTVN-1.0-pc/game/script.rpy'

    os.remove(script_path)
    shutil.copy('script.rpy', script_path)
