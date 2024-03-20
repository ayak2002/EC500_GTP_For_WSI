"""
    Usage:
        It's an entry of stage 2: training a patch feature extractor. Just modify the paths 
        accordingly and run the code.

    Input: 
        All the patches from different WSIs
    Output:
        A feature extractor model, which will be in feature_extractor/runs
"""


import os
import csv
import subprocess


def write_paths_to_csv(root_dir, csv_dir, script_dir, origin_dir):
    """
    Writes paths of .jpeg images located in '1.0' subfolders of directories ending with '_files'
    to a CSV file. Executes the feature extractor then. 
    
    :param root_dir: Path to the directory containing folders ending with '_files'.
    :param csv_dir: Path to the CSV file to write the image paths to.
    :param script_dir: Path to the directory of the feature extractor. 
    :param origin_dir: Path to this current working directory. 
    """
    all_image_paths = [] 

    for item in os.listdir(root_dir):
        folder_path = os.path.join(root_dir, item)
        if os.path.isdir(folder_path) and item.endswith('_files'):
            subfolder_path = os.path.join(folder_path, '1.0')
            if os.path.exists(subfolder_path):
                image_paths = [
                    os.path.join(subfolder_path, img) for img in os.listdir(subfolder_path)
                    if img.endswith('.jpeg')
                ]
                all_image_paths.extend(image_paths)

            #     with open(csv_dir, 'w', newline='') as csvfile:
            #         writer = csv.writer(csvfile)
            #         for path in image_paths:
            #             writer.writerow([path])

            # os.chdir(script_dir)
            # subprocess.call(['python', 'run.py'])
            # os.chdir(origin_dir)

    if all_image_paths:
        with open(csv_dir, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for path in all_image_paths:
                writer.writerow([path])
    
    os.chdir(script_dir)
    subprocess.call(['python', 'run.py'])
    os.chdir(origin_dir)


patches_dir = "/Users/paul/Desktop/EC500_GTP_For_WSI/patch"
csv_dir = "/Users/paul/Desktop/EC500_GTP_For_WSI/feature_extractor/all_patches.csv"
script_dir = "/Users/paul/Desktop/EC500_GTP_For_WSI/feature_extractor"
origin_dir = "/Users/paul/Desktop/EC500_GTP_For_WSI"
write_paths_to_csv(patches_dir, csv_dir, script_dir, origin_dir)
