import os
import subprocess

def convert(directory='.'):
    # Iterate over all files in the specified directory
    for filename in os.listdir(directory):
        # Check if the file is a .heic file
        if filename.lower().endswith(".heic"):
            filepath = os.path.join(directory, filename)
            print(f'Converting {filepath}...')
            try:
                # Use the magick command to convert the .heic file to a .jpg file
                subprocess.run(["magick", filepath, filepath[:-5] + '.jpg'], check=True)
                print(f'Successfully converted {filepath}')
            except subprocess.CalledProcessError:
                # Catch any errors that may occur during conversion
                print(f'Error converting {filepath}')

if __name__ == '__main__':
    # Run the convert function when the script is executed
    convert()