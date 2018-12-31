## COMS 6901 Project Code 
### 1. Overview

The aim of this project is to analyze student's understanding and learning of a concept based on where they are looking at. For this purpose, we divide the student's eye-gaze data into four different categories - visual data, textual data, speaker and other. We use these different classes as features and try to find which class has the highest positive and negative correlation with the student's post exam score. We also try to predict using these scores as features whether the student will get an answer right or wrong.  

### 2. Dataset

For the analysis, we have analyzed the dataset in three different ways:
- ``data/complete_data.csv`` : File which contains data for all the questions. 
- ``data/infer.csv`` : File which contains data for only "infer" type of questions.
- ``data/recall.csv`` : File which contains data for only "recall" type of questions. 


### 3. Directory
The repository contains multiple jupyter notebooks which correspond to different components of the project. Below is a brief description for each of the files:
- ``feature-engineering.ipynb``: Deriving values of features required for model.  
- ``plotting-eye-data-on-video.ipynb``: Plotting data from eye-gaze data on particular frames.
- ``prediction_models.ipynb`` : Developing multiple classification models for prediction. 
- ``question-wise-analysis.ipynb`` : Analysis of data files mentioned above.  
- ``video_generation.py``: Script to plot eye-gaze data on frames and convert back to another video. 
