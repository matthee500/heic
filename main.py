import os
import subprocess


def convert():

    directory = '.'

    for filename in os.listdir(directory):
        if filename.lower().endswith(".heic"):
            print('Converting %s...' % os.path.join(directory, filename))
            subprocess.run(["magick", "%s" % filename, "%s" % (filename[0:-5] + '.jpg')])
            continue


if __name__ == '__main__':
    convert()
    