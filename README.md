# EC500: GTP for WSI  

Prostate cancer (PCa) is the second most common cancer among males worldwide, resulting in 350,000 deaths annually. We can help decrease mortality by developing a more precise diagnosis. Automated deep learning systems show promise in accurately grading PCa. However, there is always the risk of missing cancers or the risk of overgrazing, resulting in unnecessary treatment. Our task for this project is to tune a graph transformer model to detect PCa on Whole-Slide Images (WSI) of prostate tissue samples and estimate the severity of the disease using the Gleason grading system.

### Workflow

The basic idea is to implement the whole model step by step and create an entrance for each stage. Usages are included in the entrance files. Then we will analyze and adjust the structure of the model to achieve the best performance. 

To build the model, run `{Step Number}_run.py` one by one. 

### Credits 

- A graph-transformer for whole slide image classification: [https://github.com/vkola-lab/tmi2022](https://github.com/vkola-lab/tmi2022)

- Prostate cANcer graDe Assessment (PANDA) Challenge: [https://www.kaggle.com/c/prostate-cancer-grade-assessment/data](https://www.kaggle.com/c/prostate-cancer-grade-assessment/data)
