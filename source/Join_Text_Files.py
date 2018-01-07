import shutil
import time, glob

with open("All_Links.txt", 'wb') as outfile:
    for filename in glob.glob('*.txt'):
        if filename == "All_Links.txt":
            # don't want to copy the output into the output
            continue
        with open(filename, 'rb') as readfile:
            shutil.copyfileobj(readfile, outfile)


