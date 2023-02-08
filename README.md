# heic
This script converts all the .HEIC files in the current directory to .JPG files using the ImageMagick command line tool. The ImageMagick tool needs to be installed and added to the PATH environment variable to run this script successfully.

Here's how it works:

1. The script starts by defining the convert function.

2. The convert function sets the current directory (.) as the target directory for the conversion.

3. The function then loops through all the files in the directory and checks if the file extension is .HEIC.

4. If the file extension is .HEIC, the function prints a message indicating that the file is being converted and then uses the subprocess.run function to call the ImageMagick tool and convert the file to a .JPG file.

5. Finally, the script calls the convert function when it's executed as a standalone script.