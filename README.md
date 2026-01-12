# 🌧️ Rain Prediction Machine Learning Project

## 📌 Project Description
This project predicts whether it will rain tomorrow using historical weather data.
It is a complete end-to-end Machine Learning classification project built using Python and Scikit-Learn.

---

## 🧾 Dataset
The dataset contains weather-related features such as:
- Temperature
- Rainfall
- Sunshine
- Wind Speed
- Humidity
- Pressure
- Cloud Cover

### Files Used:
- `weather.csv` – Raw dataset
- `cleandata.csv` – Cleaned dataset after handling missing values
- `encodeddata.csv` – Encoded dataset for model training

---

## ⚙️ Project Workflow
1. Data Cleaning (handling missing values)
2. Feature Selection
3. Label Encoding (`RainToday`, `RainTomorrow`)
4. Train-Test Split
5. Model Training using Logistic Regression
6. Model Evaluation (Accuracy Score & Confusion Matrix)

---

## 🤖 Machine Learning Model
- Algorithm: **Logistic Regression**
- Type: **Binary Classification**
- Library: `scikit-learn`

---

## ▶️ How to Run the Project

### Step 1: Install Dependencies
```bash
pip install pandas scikit-learn
step 2: Run Data Cleaning
python cleandata.py

Step 3: Run Encoding
python encoding.py

Step 4: Train Model
python modeltrain.py
