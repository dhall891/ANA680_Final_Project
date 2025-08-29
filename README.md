\# Heart Disease Prediction – Final Project (ANA680)



\## Overview

This project demonstrates the full machine learning lifecycle, from model development to deployment using modern MLOps tools. The goal is to predict \*\*heart disease\*\* based on patient health metrics using the UCI Cleveland dataset.



The project covers:

1\. Problem definition \& dataset

2\. Data exploration \& preprocessing

3\. Model training \& evaluation

4\. Local deployment with Flask

5\. Containerization with Docker

6\. CI/CD pipeline deployment to Heroku

7\. Model retraining in AWS SageMaker Studio Lab

8\. Deployment with Kubernetes



---



\## Dataset

\- Source: UCI Cleveland Heart Disease Dataset  

\- Format: `heart\_cleveland\_upload.xlsx`  

\- Rows: 297  

\- Columns: 14 (13 features + 1 target column `condition`)  

\- Target:  

&nbsp; - `0` → No Heart Disease  

&nbsp; - `1` → Heart Disease  



---



\## Data Exploration \& Preprocessing

\- No missing values found  

\- Balanced dataset: ~160 negative cases, ~137 positive cases  

\- StandardScaler used for feature normalization  

\- Train/test split: 80/20 stratified  



---



\## Model Training

\- Algorithms tested: Logistic Regression, Random Forest  

\- \*\*Best model: Logistic Regression\*\*  

\- Performance metrics (on test set):  

&nbsp; - Accuracy: ~0.87  

&nbsp; - Precision: ~0.89  

&nbsp; - Recall: ~0.81  

&nbsp; - F1 Score: ~0.85  



Artifacts saved:

\- `model.pkl` (trained Logistic Regression model)  

\- `scaler.pkl` (StandardScaler for input features)  



---



\## Local Deployment (Flask)

\- File: `app.py`  

\- HTML form (`templates/index.html`) accepts patient input  

\- Returns text prediction: `"Heart Disease"` or `"No Heart Disease"`  

\- Run locally:  

&nbsp; ```bash

&nbsp; python app.py



