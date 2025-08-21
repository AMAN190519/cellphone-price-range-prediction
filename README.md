# 📱 Cellphone Price Prediction

This project was completed in *Jupyter Notebook*. It covers data cleaning, EDA (visualization), skewness correction, outlier treatment, scaling, feature engineering, and machine learning model training & evaluation.  
(Notebook: cellphone_price_prediction.ipynb)

---

## 📌 Overview
Predict cellphone price ranges (categories) from technical specifications using Python.  
The project demonstrates a full ML pipeline from data inspection to model evaluation and basic improvement ideas.

---

## 🔧 Technologies / Libraries
- Python (>=3.8)  
- numpy, pandas  
- matplotlib, seaborn (visualization: histograms, boxplots, scatter, heatmap)  
- scipy (statistical functions)  
- scikit-learn (models & preprocessing)  
- jupyter

---

## 📂 Files in this repository
- cellphone-price-range-prediction.ipynb — Main Jupyter Notebook (full code, plots, explanations).  
- requirements.txt — Required Python packages.
- Readme.md
- .gitignore 
   
  

---

## 🧭 Project Workflow
1. *Data Cleaning*
   - Checked and handled missing values.  
   - Removed duplicates.  
   - Encoded - No Encoding was needed as all the columns were numerical.

2. *Exploratory Data Analysis (EDA)*
   - Histograms for distributions (skewness check).  
   - Boxplots for outlier detection.  
   - bar graphs for important features.

3. *Skewness Treatment*
   - Applied transformations to reduce skewness where needed:  
     - Log Transform (np.log1p)  
     - Square Root Transform (np.sqrt)  
     - Cube Root Transform (np.cbrt)  

4. *Outlier Treatment*
   - Detected outliers using the IQR method.  
   - Applied *Winsorization (capping)* instead of dropping extreme values.

5. *Feature Scaling*
   - Standardization using StandardScaler.  

6. *Model Training*
   - Logistic Regression  
   - XGBoost  
   - Random Forest Classifier  

7. *Model Evaluation*
   - Accuracy score, Confusion Matrix, Classification Report (precision/recall/f1).  
   - Feature importance and model comparison chart.

---

## 📊 Results (example)
- *Random Forest Accuracy:* ~89%  
- *Logistic Regression Accuracy:* ~95%  
- *XGBoost:* ~93%  

---

## 🚀 How to Run

```bash
# 1. Clone the repository
git clone https://github.com/AMAN190519/cellphone-price-range-prediction.git
cd cellphone-price-range-prediction

# 2. (Optional but recommended) create & activate virtual environment
python -m venv .venv

# On Windows (PowerShell):
.venv\Scripts\Activate.ps1
# or (cmd):
.venv\Scripts\activate

# On macOS / Linux:
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start Jupyter Notebook
jupyter notebook

# 5. In browser, open:
# -> cellphone-price-range-predictio.ipynb
