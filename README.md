# **Mental Health Prediction Model**

This project uses Machine Learning (ML) to predict mental health conditions in individuals based on their demographic and social information. The goal is to build a model that can be useful for early screening and intervention.

## 

## **Technology Stack**

This project uses Python for the core ML logic, but the concepts are designed to be easily integrated into a full-stack web application (e.g., using Node.js/React as a deployment layer).

* **Core ML Language:** Python  
* **Libraries:** Scikit-learn, Pandas, NumPy, Matplotlib, Seaborn  
* **Models Evaluated:** AdaBoost, Random Forest, Decision Tree, Logistic Regression, and more.

## 

## **Methodology: How We Built It**

We followed a standard ML workflow, focusing on high accuracy and clear results:

1. **Data Preparation:** Cleaned the raw dataset (from Kaggle) by handling missing values and converting text data into a format suitable for the models.  
2. **Feature Selection (Wrapper Approach):** To ensure the model focused only on the most predictive factors, we used a **wrapper approach**. This means we used the model itself as a tool to test different combinations of features, finding the optimal subset for the best performance.  
3. **Model Selection:** We tested various classification algorithms to find the best fit. **AdaBoost Classifier** was ultimately selected as the top performer.  
4. **Model Evaluation:** Measured the model's performance using robust metrics.

## 

## **Key Results**

* **Best Performing Model:** **AdaBoost Classifier**.  
* **Overall Accuracy:** The final model achieved an accuracy of **86.93%** in predicting mental health conditions.

## 

## **Advanced Evaluation & Future Features**

We implemented advanced features to give a clearer, more detailed view of the model's performance beyond simple accuracy. We plan to integrate these plots into a web dashboard later:

* **ROC Curve (Receiver Operating Characteristic):** Shows the model's ability to distinguish between individuals with and without a predicted condition.  
* **Precision-Recall Curve:** Provides detailed insight into the trade-off between the model's correct positive predictions and its ability to find all relevant cases.  
* **Feature Importance Plot:** Clearly visualizes which demographic or social factors are most heavily weighted by the model when making a prediction.

## 

## **How to Run Locally**

1. **Clone the project:**  
   git clone \[repository-link-here\]

2. **Install requirements:**  
   pip install \-r requirements.txt

3. **Run the script:**  
   python main.py

   *Follow the on-screen console instructions for input and results.*

## **Conclusion**

This model is a strong foundation for predicting mental health conditions. Future steps involve turning this core Python logic into a **Full Stack web application** for wider accessibility and practical use.