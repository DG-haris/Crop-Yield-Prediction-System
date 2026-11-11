# 🌾 Crop Yield Prediction System

A Machine Learning-based web application that predicts agricultural crop yield using soil conditions, weather information, crop details, and farming inputs.

## 📌 Project Overview

The Crop Yield Prediction System uses a **Gradient Boosting Regressor** to estimate crop yield in tonnes per hectare (t/ha).

The application allows users to enter agricultural and environmental parameters through an interactive Streamlit interface and receive an estimated crop yield.

## 🚀 Features

- Crop yield prediction using Machine Learning.
- Interactive Streamlit web application.
- Input validation through numerical input ranges.
- 15 input features covering soil, weather, crops, and agricultural practices.
- Real-time prediction output.
- Input summary displayed after prediction.
- Model performance metrics displayed in the sidebar.

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Joblib
- Streamlit
- Machine Learning

## 🤖 Machine Learning Model

**Algorithm:** Gradient Boosting Regressor

**Prediction Target:** Crop Yield (tonnes/hectare)

### Input Features

1. Soil pH
2. Soil Moisture
3. Average Temperature
4. Total Rainfall
5. Fertilizer Amount
6. Pesticide Usage
7. Sunlight Hours
8. Nitrogen Content
9. Phosphorus Content
10. Potassium Content
11. Irrigation Frequency
12. Crop Type
13. Region
14. Season
15. Harvest Month

## 📊 Model Performance

The model was evaluated using field-grouped validation to reduce data leakage between training and validation data.

| Evaluation Metric | Result |
|---|---:|
| R² Score | 0.686 |
| MAE | 0.516 t/ha |
| RMSE | 0.641 t/ha |

## 📂 Project Structure

```text
Crop-Yield-Prediction-System/
│
├── app.py
├── crop_yield_model.pkl
├── requirements.txt
├── README.md
├── .gitignore
│
└── screenshots/
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project directory

```bash
cd Crop-Yield-Prediction-System
```

### 3. Create a virtual environment (optional)

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your web browser.

## 🎯 Project Objective

The objective of this project is to demonstrate how Machine Learning can be applied to agricultural data to estimate crop yield based on multiple environmental and farming-related factors.

## 👨‍💻 Author

Developed as a Machine Learning and Data Science portfolio project.

---

⭐ If you find this project interesting, consider giving it a star!