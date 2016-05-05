# mpi_combine_add.py

import sys

if len(sys.argv) < 3:
    raise ValueError("At least 3 arguments required! 2 input folders and 1 output folder.")

input_folders = sys.argv[1:-1]
output_folder = sys.argv[-1]

print("list of input folder")
print(input_folders)
print("output folder is: ", output_folder)
