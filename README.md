# Gesture-Phase-Segmentation
Introduction
Welcome to the Gesture Phase Segmentation project! This guide will assist you in navigating through the project repository and utilizing the analysis and models developed. If you are interested in segmenting gesture signals into different phases, you're in the right place.

## Table of Contents

1. [Introduction](#i-introduction)
2. [Exploratory Data Analysis](#iii-exploratory-data-analysis)
3. [Feature Engineering](#iv-feature-engineering)
4. [Machine Learning Model](#v-machine-learning-model)
5. [Conclusion](#vi-conclusion)
6. [How to Use](#vii-how-to-use)

## I. Introduction
Welcome to this notebook on Gesture Phase Segmentation! In this project, we will be working with the Gesture Phase Segmentation dataset from the UCI Machine Learning Repository. The dataset is designed for the task of segmenting hand gesture signals into different phases, providing a valuable resource for understanding and classifying temporal aspects of hand movements. We use a1_raw.csv, a2_raw.csv and a3_raw.csv datasets.

Our approach to solving the problem involves the following steps:
   1. Data Exploration: Gain insights into the structure of the dataset and the distribution of gesture phases.
   2. Preprocessing: Handle any missing values, normalize features, and segment continuous gesture signals into labeled phases.
   3. Feature Engineering: Identify and extract relevant features capturing the characteristics of different gesture phases.
   4. Model Selection: Choose a suitable classification algorithm for gesture phase segmentation.
   5. Training: Train the selected model on a subset of the dataset, reserving another portion for testing and validation.
   6. Evaluation: Assess the model's performance using metrics like accuracy, precision, recall, and F1 score.
   7. Fine-Tuning and Optimization: Iterate on the model, fine-tune hyperparameters, and optimize for better performance.

## II. Exploratory Data Analysis

In the exploratory data analysis (EDA) of the Gesture Phase Segmentation dataset, a comprehensive overview of the combined data from different sources (df_a1r, df_a2r, df_a3r) was undertaken, resulting in a unified data frame named df. This consolidation facilitated a nuanced examination of various body part movements during different phases of gestures. The descriptive statistics illuminated distinctive characteristics across body parts, such as the left and right hands, head, spine, left wrist, and right wrist. Key metrics, including mean, median, mode, and standard deviation, provided insights into the central tendencies and variability within each body part's movement dimensions.

Visualizations played a pivotal role in understanding the data distribution. Box plots were employed to succinctly depict the central tendency, spread, and identification of outliers for individual features. The decision to retain outliers was informed by their perceived relevance and potential significance in capturing unique or expressive gestures that contribute valuable information to different phases. Distribution plots, specifically histograms with kernel density estimation, offered a detailed view of the frequency distribution of feature values, aiding in assessing skewness and central tendencies.

The dataset encompassed five distinct phases: 'Rest,' 'Preparation,' 'Stroke,' 'Hold,' and 'Retraction.' Transformation of categorical features into numeric representations, along with a label encoding process, facilitated subsequent analysis. The correlation matrix and heatmap unveiled patterns of association or dependence between variables, providing a visual summary of correlations. This heatmap, with warmer and cooler colors indicating positive and negative correlations, respectively, served as a valuable guide for understanding relationships among features and potential multicollinearity. Overall, the EDA presented a comprehensive exploration of the dataset, laying the foundation for subsequent modeling decisions and insights into the intricate dynamics of gesture phases.

## III. Feature Engineering 
In this study, we conducted a thorough feature engineering process to enhance the dataset's informativeness for the classification of gesture phase segmentation. Our approach involved computing Euclidean distances between various pairs of body parts, thereby capturing the spatial relationships within the skeletal structure. This enabled us to quantify the relative positioning of limbs and joints, providing valuable insights into gestural dynamics. To incorporate temporal aspects, we calculated velocity and acceleration for each coordinate of body parts, ensuring uniformity and comparability across different dimensions through robust scaling. The robust nature of the RobustScaler, which is less sensitive to outliers, proved advantageous in handling the complex and dynamic nature of our dataset. The resultant dataset was enriched with features encapsulating both spatial intricacies and the dynamic nature of gestures, forming a solid foundation for subsequent machine-learning tasks. Furthermore, our evaluation of feature scaling techniques highlighted the superior performance of RobustScaler over MinMaxScaler, particularly in the presence of outliers that are common in dynamic datasets. The comprehensive analysis and feature engineering undertaken in this work contribute to the understanding of gestural dynamics and lay the groundwork for robust machine learning models in the domain of gesture phase segmentation. The processed dataset, along with the enriched features, is made publicly available for further research and exploration.

## IV. Machine Learning Model
Decision Tree
The Decision Tree classifier, with parameters set at min_samples_split=20, random_state=99, and criterion='entropy', achieved an accuracy of 80.12%. While displaying effectiveness in certain phases, challenges were identified in others, as evident in the Confusion Matrix. The decision tree's hierarchical structure and extracted textual rules enhanced interpretability.

Random Forest
The Random Forest model, consisting of 100 decision trees and employing the entropy criterion, demonstrated impressive performance with an accuracy of 91.20%. Precision and recall values were consistently high, as illustrated in the Classification Report. Feature importances were visualized to provide insights into the model's decision-making process.

Support Vector Machine (SVM)
SVM with Linear Kernel
The SVM with a Linear Kernel, despite not undergoing feature scaling, demonstrated competitive accuracy at 69.12%. Feature scaling techniques, such as MinMax Scaling and Standard Scaler, were explored to assess their impact on model performance.

Scaling Technique	Accuracy
None	69.12%
MinMax Scaling	...
Standard Scaler	...

SVM with RBF Kernel (Best Performing Model)
The SVM with RBF Kernel emerged as the best-performing model with an accuracy of 83.6%. Optimal hyperparameters, obtained through grid search, further enhanced its classification performance.
## V. Conclusion 

## VI. How to Use
