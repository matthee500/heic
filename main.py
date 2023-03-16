import os
import subprocess

def convert(directory='.'):
    for filename in os.listdir(directory):
        if filename.lower().endswith(".heic"):
            filepath = os.path.join(directory, filename)
            print(f'Converting {filepath}...')
            try:
                subprocess.run(["magick", filepath, filepath[:-5] + '.jpg'], check=True)
                print(f'Successfully converted {filepath}')
            except subprocess.CalledProcessError:
                print(f'Error converting {filepath}')

if __name__ == '__main__':
    convert()