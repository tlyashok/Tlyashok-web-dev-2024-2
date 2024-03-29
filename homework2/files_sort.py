import os
import sys

def list_files(directory):
    files_by_extension = {}
    for filename in sorted(os.listdir(directory)):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            _, extension = os.path.splitext(filename)
            files_by_extension.setdefault(extension, []).append(filename)

    for extension, files in sorted(files_by_extension.items()):
        for filename in files:
            print(filename)