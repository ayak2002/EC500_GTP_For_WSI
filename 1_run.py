import os
import subprocess

# Process all .tiff files in the given directory with the specified command
def process_tiff_files(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    for filename in os.listdir(input_dir):
        if filename.endswith(".tiff"):
            filepath = os.path.join(input_dir, filename)
            command = f"python 1_tile_WSI.py -s 512 -e 0 -j 32 -B 50 -M 1 -o \"{output_dir}\" \"{filepath}\""
            print(f"Tiling {filename}...")
            subprocess.run(command, shell=True)

# Directory containing .tiff files
input_dir = "minisample/train_images"
# Directory to store the output patches
output_dir = "patch"

process_tiff_files(input_dir, output_dir)
