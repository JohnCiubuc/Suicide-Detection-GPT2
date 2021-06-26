# Suicide-Detection-GPT2

Proof-of-concept to determine potential suicide/depression risk from text. Idea was developed by a collaboration between myself and Ebrahim Payberah

This repository has a Dataset to load into google collab. 20,000 suicide/non-suicide train (even split), 10,000 suicide/non-suicide test (even split).

Original dataset source [on kaggle by Nikhileswar Komati](https://www.kaggle.com/nikhileswarkomati/suicide-watch?select=Suicide_Detection.csv). Cleaned and formatted for pytorch

Original GPT-2 text classification by [George Mihaila](https://github.com/gmihaila)

# Parser

[`sd_parser.py`](https://github.com/JohnCiubuc/Suicide-Detection-GPT2/blob/main/sd_parser.py) was used to generate `sd.tar.xz` from `Suicide_Detection.csv` (not provided) from the kaggle link above.

# Training Model

Collab notebook [located here](https://colab.research.google.com/github/JohnCiubuc/Suicide-Detection-GPT2/blob/main/suicide_detection_gpt2_finetune_classification.ipynb)

# Running / Predict Model

While training model collab does have prediction at the end, if you wish to just load pre-trained model and predict from that, [open this collab notebook instead](https://colab.research.google.com/github/JohnCiubuc/Suicide-Detection-GPT2/blob/main/Load%20and%20Predict%3A%20suicide_detection_gpt2.ipynb)
