"""
    Usage:
        This is a script that splits the training, validation and testing set, 
        and the proportion is 7:1:2. Run this script before running 4_train.sh 
        and 4_test.sh. 

        Also you can run the training and testing scripts here by commenting 
        prepare_input_for_transformer and uncommenting the sub-processes. BUT 
        remember to SET UP the hyperparameters first! These are mainly in 4_{train, test}.sh 
        and option.py. 

    Input: 
        Graph embeddings
    Output: 
        Classification result
"""


import pandas as pd
import os
from sklearn.model_selection import train_test_split
import subprocess


def prepare_input_for_transformer(label_path, graph_path):
    """
    Reads a CSV file for image_id and corresponding labels, iterates over subfolders
    within a specified base directory to match labels, and then splits the data into
    training and validation sets which are saved to text files.

    @param label_path: Path to the CSV file containing image_id and labels
    @param graph_path: Path to the base directory containing graphs named after each image_id
    """
    data = pd.read_csv(label_path)
    id_label_map = dict(zip(data['image_id'], data['isup_grade']))
    
    samples = []
    for subfolder in os.listdir(graph_path):
        if subfolder in id_label_map:
            # prepare the sample-label pair
            samples.append(f"{subfolder}\t{id_label_map[subfolder]}")

    train_val_samples, test_samples = train_test_split(samples, test_size=0.2, random_state=42)
    train_samples, val_samples = train_test_split(train_val_samples, test_size=0.125, random_state=42)
    
    with open('graphs/train_set.txt', 'w') as f_train:
        f_train.write('\n'.join(train_samples))
        
    with open('graphs/val_set.txt', 'w') as f_val:
        f_val.write('\n'.join(val_samples))

    with open('graphs/test_set.txt', 'w') as f_test:
        f_test.write('\n'.join(test_samples))


if __name__ == '__main__':
    label_path = "minisample/train.csv"
    graph_path = "graphs/simclr_files"
    prepare_input_for_transformer(label_path, graph_path)

    # train_script_path = './4_train.sh'
    # result = subprocess.run([train_script_path], capture_output=True, text=True, shell=True)
    # print("STDOUT:", result.stdout)
    # print("STDERR:", result.stderr)

    # test_script_path = './4_test.sh'
    # result = subprocess.run([test_script_path], capture_output=True, text=True, shell=True)
    # print("STDOUT:", result.stdout)
    # print("STDERR:", result.stderr)
