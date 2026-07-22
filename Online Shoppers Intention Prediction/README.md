# Online Shoppers Intention Prediction

## Overview
This project predicts whether an online shopper will make a purchase based on session-level browsing behavior. It combines model training, evaluation, and a Flask web app for real-time predictions and dashboard-style insights.

## Problem Statement
E-commerce sites collect a lot of browsing data, but not every visit turns into a purchase. The goal of this project is to use session behavior to predict purchase intent and support better business decisions.

## Dataset
- **Dataset Name:** Online Shoppers Purchasing Intention Dataset
- **Source:** Kaggle
- **Dataset Link:** [Online Shoppers Intention](https://www.kaggle.com/datasets/henrysue/online-shoppers-intention)
- **Records:** 12,330 sessions
- **Features:** 18 columns including the target variable
- **Target Variable:** `Revenue`
  - `True` or `Yes` means a purchase happened.
  - `False` or `No` means no purchase happened.

The dataset contains session-level e-commerce behavior such as page visits, time spent on pages, bounce rate, exit rate, page value, traffic source, visitor type, and weekend activity. The UCI version of the dataset is described as 10 numerical and 8 categorical attributes, with `Revenue` used as the class label. [web:25]

## Why This Dataset Works Well
This dataset is a good fit for purchase prediction because it contains direct behavioral signals linked to conversion, such as product page activity, page value, and exit behavior. The target is binary, so it works naturally for classification models.

## Data Preprocessing
The project uses the following preprocessing steps:
- Duplicate sessions are removed.
- Missing values are handled with median imputation for numeric fields and mode imputation for categorical fields.
- Categorical values are encoded with label encoders.
- Numeric features are scaled with `StandardScaler`.
- Train/test split is stratified so the target distribution stays balanced across splits.

## Project Workflow
1. Load the dataset from the `Dataset` folder.
2. Clean and validate the data.
3. Encode categorical columns.
4. Scale numeric features.
5. Train multiple deep learning models.
6. Evaluate model performance.
7. Save trained models and preprocessing files.
8. Build a Flask app for inference and dashboard views.
9. Add security settings for safer deployment.

## Models Implemented
### MLP
Used as a baseline model for tabular classification.

### Deep Neural Network
A deeper feedforward model used as the main production model in the web app.

### LSTM
Used to learn sequential-style patterns from session data.

### GRU
Used as a lighter recurrent alternative to LSTM.

## Model Assets
This folder contains the notebook, trained models, and preprocessing files needed for training and inference.

### Files Included
- Jupyter Notebook implementation
- Trained deep learning models
- Feature scaler
- Label encoders
- Target encoder

These files are kept because the Flask app needs them for real-time inference and dashboard results.

## Performance Summary
| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|-------|----------|-----------|--------|----------|---------|
| MLP | 0.8895 | 0.7248 | 0.5876 | 0.6481 | 0.8672 |
| Deep Neural Network | 0.8965 | 0.7658 | 0.6521 | 0.7037 | 0.8952 |
| LSTM | 0.8931 | 0.7412 | 0.6124 | 0.6708 | 0.8823 |
| GRU | 0.8947 | 0.7521 | 0.6287 | 0.6849 | 0.8891 |

The Deep Neural Network performs best overall, especially on F1 score and ROC-AUC.

## Visualizations
All plots are combined into one PDF report inside the `Images` folder. Each figure is explained below.

### 1. Training History
Shows how the model learned across epochs. It helps check whether training converged properly and whether overfitting appeared.

### 2. Model Comparison
Compares all trained models across metrics like accuracy, precision, recall, F1 score, and ROC-AUC.

### 3. Confusion Matrices
Shows correct and incorrect predictions for purchase and non-purchase sessions.

### 4. ROC Curves
Shows how well each model separates the two classes.

### 5. Feature Importance
Highlights the most useful behavioral signals for prediction.

### 6. Data Distribution
Shows the spread of the dataset features and target class behavior.

## Web Application
The project includes a Flask web application for prediction and analysis.

### Goal
A deployable Flask app for real-time purchase intent prediction using the deep feedforward neural network.

### Model Used in the App
The web app uses the Deep Neural Network model for production inference. The other models were trained for comparison.

### Pages
#### Home Page
Introduces the project and routes users to the prediction and dashboard sections.

#### Prediction Page
Accepts session values and returns:
- Purchase intent prediction
- Confidence score
- Short explanation
- Key factors behind the result

#### Dashboard Page
Shows:
- Dataset statistics
- Purchase vs non-purchase ratio
- Top correlated features
- Model comparison metrics

### Web App Demo
A demo video is included in the `Web App` folder and shows:
- Landing page
- Prediction workflow
- Real-time inference
- Analytics dashboard
- Model comparison

## Security Improvements
The Flask app includes production-oriented security fixes.

### Applied Fixes
- `PREFERRED_URL_SCHEME = "https"`
- `SESSION_COOKIE_SECURE = True`
- `SESSION_COOKIE_HTTPONLY = True`
- `SESSION_COOKIE_SAMESITE = "Lax"`
- Flask-Talisman for HTTPS enforcement and security headers
- Content Security Policy for safer script and style loading

These settings help address the GitHub Advanced Security warnings and make the app safer for deployment.

## Repository Structure
```text
Online Shoppers Intention Prediction/
├── Dataset/
│   └── online_shoppers_intention.csv
├── Images/
│   ├── model_visualizations.pdf
│   └── webapp_screenshot.png
├── Model/
│   ├── online_shoppers_intention_prediction.ipynb
│   ├── 01_mlp_model.h5
│   ├── 02_lstm_model.h5
│   ├── 03_gru_model.h5
│   ├── 04_deep_network_model.h5
│   ├── feature_scaler.pkl
│   ├── label_encoders.pkl
│   └── target_encoder.pkl
├── Web App/
│   ├── app.py
│   ├── static/
│   ├── templates/
│   └── web_app.mp4
├── requirements.txt
└── README.md
```

## Installation
```bash
git clone <repository-url>
cd "Online Shoppers Intention Prediction"
pip install -r requirements.txt
```

## Run the Web App
```bash
cd "Web App"
python app.py
```

Then open the local server in your browser.

## Future Improvements
- Handle class imbalance more explicitly.
- Add SHAP-based explainability.
- Improve dashboard interactivity.
- Add API endpoints for integration.
- Deploy the app to a production host.

## Author
**Somapuram Uday**

- GitHub: [udaycodespace](https://github.com/udaycodespace)
- LinkedIn: [Somapuram Uday](https://www.linkedin.com/in/somapuram-uday)