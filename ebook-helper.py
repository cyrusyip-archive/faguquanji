from os import listdir, rename, walk
from os.path import isfile, join
import subprocess, os


# return name of file to be kept after conversion.
# we are just changing the extension. mobi here.
def get_final_filename(f):
    f = f.split(".")
    filename = ".".join(f[0:-1])
    processed_file_name = filename+".mobi"
    return processed_file_name

# return file extension. pdf or epub or mobi
def get_file_extension(f):
    return f.split(".")[-1]

mypath = "."
bin_file = "/Applications/calibre.app/Contents/MacOS/ebook-convert"

for root, dirs, files in walk('.'):
    for f in files:
        if f.lower().endswith('.epub'):
            src = os.path.abspath(root + '/' + f)
            dest = get_final_filename(src)

            if not os.path.exists(dest):
                subprocess.call([bin_file, src, dest]) 
                print('converted ' + dest)
