# Gesture-Phase-Segmentation

Welcome to the Gesture Phase Segmentation project! This guide will assist you in navigating through the project repository and utilizing the analysis and models developed. If you are interested in segmenting gesture signals into different phases, you're in the right place.

## Table of Contents

1. [Introduction](#i-introduction)
2. [Exploratory Data Analysis](#iii-exploratory-data-analysis)
3. [Feature Engineering](#iv-feature-engineering)
4. [Machine Learning Model](#v-machine-learning-model)
5. [Conclusion](#vi-conclusion)

## I. Introduction
Welcome to this notebook on Gesture Phase Segmentation! In this project, we will be working with the Gesture Phase Segmentation dataset from the UCI Machine Learning Repository. The dataset is designed for the task of segmenting hand and body gesture signals into different phases, providing a valuable resource for understanding and classifying temporal aspects of hand and body movements. We use a1_raw.csv, a2_raw.csv and a3_raw.csv datasets.

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
1. **Decision Tree:**
The Decision Tree classifier, with parameters set at min_samples_split=20, random_state=99, and criterion='entropy', achieved an accuracy of 80.12%. While displaying effectiveness in certain phases, challenges were identified in others, as evident in the Confusion Matrix. The decision tree's hierarchical structure and extracted textual rules enhanced interpretability.

|           | Hold |Preparation  |  Rest | Retraction | Stroke |
|-----------|---------|---------|---------|---------|---------|
| precision | 0.72 | 0.53 | 0.90 | 0.61 | 0.87 |
| recall  | 0.75 | 0.56 | 0.92 | 0.66 | 0.81 |
| f1-score| 0.74 | 0.55 | 0.91 | 0.63 | 0.84 |
| support| 76 | 183 | 532 | 138 | 525 |

2. **Random Forest:**
The Random Forest model, consisting of 100 decision trees and employing the entropy criterion, demonstrated impressive performance with an accuracy of 91.20%. Precision and recall values were consistently high, as illustrated in the Classification Report. Feature importances were visualized to provide insights into the model's decision-making process.

|           | Hold |Preparation  |  Rest | Retraction | Stroke |
|-----------|---------|---------|---------|---------|---------|
| precision | 0.92 | 0.91 | 0.93 | 0.96 | 0.89 |
| recall  | 0.86 | 0.67 | 0.99 | 0.73 | 0.98 |
| f1-score| 0.88 | 0.77 | 0.96 | 0.83 | 0.93 |
| support| 76 | 183 | 532 | 138 | 525 |

3. **Support Vector Machine (SVM):**

3.1 **SVM with Linear Kernel**
The SVM with a Linear Kernel, despite not undergoing feature scaling, demonstrated competitive accuracy at 69.12%. Feature scaling techniques, such as MinMax Scaling and Standard Scaler, were explored to assess their impact on model performance.

Scaling Technique	Accuracy
None	69.12%
Cross Validation  67.42%
MinMax Scaling	 69.11%
Standard Scaler	79.09%

3.2 **SVM with Multiple Kernel**
SVM with RBF Kernel (Best Performing Model)
The SVM with RBF Kernel emerged as the best-performing model with an accuracy of 83.6%. Optimal hyperparameters, obtained through grid search, further enhanced its classification performance.

## V. Conclusion 
In summary, the SVM with RBF Kernel stands out as the most balanced and robust model for the given dataset. Its accuracy of 83.6% and detailed Classification Report, including precision, recall, and F1-score for each class, showcase its comprehensive performance across all gesture phases. This model excels in both accuracy and generalization, making it a strong candidate for applications where a well-rounded performance is crucial.

The Random Forest model, with its remarkable accuracy of 91.20%, also presents itself as a powerful classifier. Its Classification Report highlights outstanding precision and recall in phases 2 and 4, showcasing its proficiency in recognizing these specific gestures. While some misclassifications occur in phases 1 and 3, the overall macro and weighted F1 scores of 87% and 91%, respectively, underscore its strong performance and reliability.

The Decision Tree model, although achieving an accuracy of 80.12%, exhibits some limitations in precision and recall, particularly in phases 1 and 3. Despite these challenges, the model remains a solid choice, especially in scenarios where interpretability and simplicity take precedence.

Ultimately, the choice among these models depends on the specific requirements of the application. If a balance of accuracy and interpretability is essential, the SVM with RBF Kernel is recommended. For scenarios where high accuracy is paramount, the Random Forest model proves to be a formidable choice. The Decision Tree model, while slightly less accurate, remains valuable for its interpretability and simplicity, making it suitable for certain applications.
