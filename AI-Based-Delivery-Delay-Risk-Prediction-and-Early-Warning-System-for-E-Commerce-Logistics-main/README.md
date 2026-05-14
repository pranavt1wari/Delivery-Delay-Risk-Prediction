# AI-Based Delivery Delay Risk Prediction and Early Warning System for E-Commerce Logistics

## Overview
This project focuses on predicting delivery delay risks in e-commerce logistics using Machine Learning.  
The system generates a realistic logistics dataset, preprocesses and engineers meaningful features, and trains predictive models to classify deliveries into different risk categories.

The goal is to help logistics companies identify risky deliveries early and improve operational efficiency through proactive decision-making.

---

## Problem Statement
E-commerce logistics companies often face delivery delays due to:
- High order volume
- Traffic congestion
- Weather conditions
- Warehouse processing inefficiencies
- Courier workload
- Historical delay patterns

This project builds an AI-based early warning system capable of predicting whether a delivery will be:
- **On-Time**
- **At Risk**
- **Delayed**

---

## Project Workflow

### 1. Synthetic Dataset Generation
A realistic logistics dataset was generated containing:
- Order volume
- Warehouse processing time
- Shipment distance
- Courier load percentage
- Traffic level
- Weather severity
- Past delay rate

A weighted delivery risk score was calculated using domain-inspired logic and controlled stochastic noise.

---

### 2. Data Preprocessing & Feature Engineering

#### Conventional Preprocessing
- Missing value checks
- Label encoding
- Feature scaling using `StandardScaler`
- Train-test split

#### Unconventional Feature Engineering
- Severity Index  
  Combines traffic and weather impact.

- Warehouse Efficiency  
  Measures shipment distance per warehouse processing hour.

- Log Transformations  
  Applied to reduce skewness in numerical features.

- Distance Categorization  
  Distance values converted into:
  - Short
  - Medium
  - Long

- One-Hot Encoding for categorical features

---

## Machine Learning Models Used

### Logistic Regression
Used as a baseline classification model.

### Random Forest Classifier
Selected as the final model due to:
- Better handling of non-linear relationships
- Improved classification performance
- Better understanding of complex logistics patterns

### Additional Models Explored
- LightGBM
- Gradient Boosting
- Artificial Neural Networks (ANN)

---

## Technologies Used

### Programming Language
- Python

### Libraries
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- LightGBM

### Environment
- Google Colab
- Jupyter Notebook

---

## Project Structure

```bash
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 1_data_generation.ipynb
│   ├── 2_preprocessing.ipynb
│   └── 3_modeling.ipynb
│
├── outputs/
│   ├── plots/
│   └── models/
│
└── README.md
```

---

## Key Features
- Synthetic logistics dataset generation
- Delivery risk scoring mechanism
- Advanced feature engineering
- Multi-class classification
- Early warning system for delayed deliveries
- Model comparison and evaluation

---

## Model Evaluation
Models were evaluated using:
- Accuracy Score
- Classification Report
- Confusion Matrix

Random Forest achieved the best overall performance after removing target leakage and handling complex feature interactions effectively.

---

## Future Improvements
- Real-time delivery tracking integration
- Live traffic and weather APIs
- Deep Learning models
- Dashboard visualization
- Explainable AI for prediction interpretation
- Deployment using Flask or FastAPI

---

## Applications
- E-commerce logistics optimization
- Supply chain analytics
- Delivery risk management
- Courier workload balancing
- Smart warehouse systems

---

## Conclusion
This project demonstrates how AI and Machine Learning can improve logistics decision-making by identifying risky deliveries before delays occur. The system can support smarter routing, resource allocation, and proactive customer service in modern e-commerce operations.
