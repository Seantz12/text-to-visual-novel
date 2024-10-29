from zipfile import ZipFile

import argparse
import os
import shutil
import sys

if __name__ == "__main__":
    print("this is a test starting script!")
    print("if you're reading this, this is just a way for me to test out the basic structure")
    print("surely by the time i release this i will have a gui interface")

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

    if not os.path.exists(script_path):
        print('wtf no script')
        exit(1)

    os.remove(script_path)
    shutil.copy('script.rpy', script_path)
