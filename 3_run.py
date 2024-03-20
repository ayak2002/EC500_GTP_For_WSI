"""
    Usage:
        It's an entry of stage 3: constructing the graph, the meaning of which 
        from my point of view is to generate the initial embeddings. Add your 
        paths below and run this .py file. 

        The reference command is 
            python build_graphs.py --weights "path_to_pretrained_feature_extractor" --dataset "path_to_patches" --output "../graphs"
        i.e., 
            python build_graphs.py --weights "model.pth" --dataset "/Users/paul/Desktop/EC500_GTP_For_WSI/patch/*/" --output "/Users/paul/Desktop/EC500_GTP_For_WSI/graphs" 

    Input: 
        All the patches and the trained feature extractor
    Output:
        Graph embeddings
"""

import subprocess
import os


def build_graphs(dataset_path, output_path):
    """
    Runs build_graphs.py under feature_extractor with specified dataset and output paths.

    @param dataset_path: Path that meets the requirements of the glob module and
                        contains groups of patches 
    @param output_path: Path to the output graph embeddings
    """
    command = (
        f"cd feature_extractor && python build_graphs.py --weights \"model.pth\" --dataset \"{dataset_path}\" --output \"{output_path}\""
    )

    subprocess.run(command, shell=True)


dataset_path = "/Users/paul/Desktop/EC500_GTP_For_WSI/patch/*/"
output_path = "/Users/paul/Desktop/EC500_GTP_For_WSI/graphs"

build_graphs(dataset_path, output_path)
