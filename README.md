<p align="center">
  <img src="https://img.icons8.com/external-flaticons-lineal-color-flat-icons/512/external-student-back-to-school-flaticons-lineal-color-flat-icons.png" width="18%" alt="Student AI Banner"/>
</p>

<h1 align="center">🎓 AI-Based Student Performance Prediction and Early Warning System using ML</h1>

<p align="center">
  <b>An End-to-End Machine Learning Web Application for Predicting Student Academic Outcomes 📊</b><br>
  Predict <b>Final Score</b>, <b>Pass/Fail Result</b>, <b>Grade</b>, and detect <b>Academic Risk Levels</b> using AI models trained on academic & lifestyle data.
</p>

<h3 align="center">🧠 Machine Learning Models Used</h3>
<p align="center">
  <img src="https://img.shields.io/badge/Linear%20Regression-Score%20Prediction-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Logistic%20Regression-Pass%2FFail-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Random%20Forest-Grade%20Prediction-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Scikit--Learn-ML%20Library-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Streamlit-Web%20App-ff4b4b?style=for-the-badge" />
  <img src="https://img.shields.io/badge/SQLite-Database-lightgrey?style=for-the-badge" />
</p>

---

## 📌 Project Overview

The **AI-Based Student Performance Prediction and Early Warning System** is an intelligent education analytics platform built using **Machine Learning + Streamlit**.

This system helps educators and institutions:

✅ Predict **Final Exam Scores**  
✅ Determine **Pass or Fail Status**  
✅ Classify **Student Grades**  
✅ Detect **Students at Academic Risk**  
✅ Provide **AI-Based Improvement Suggestions**

It acts as an **Early Warning System** to identify struggling students before final exams.

---

## ✨ Key Features

### 🎯 Student Performance Prediction

Predicts:

- 📈 Final Score (Regression Model)  
- ✅ PASS / ❌ FAIL (Binary Classification)  
- 🏆 Grade (A+, A, B, C, P, F)

### 🧠 Academic Early Warning System

After prediction, the system analyzes student behavior and detects risk factors:

| Risk Factor | Impact |
|-------------|--------|
| Low study hours | High academic risk |
| Poor attendance | Performance decline |
| Weak previous scores | Learning gaps |
| Fewer assignments | Low engagement |
| Insufficient sleep | Reduced concentration |

Students are classified as:

🚨 **High Risk**  
⚠️ **Moderate Risk**  
✅ **Low Risk**

### 💡 AI-Based Suggestions

The system automatically provides improvement tips like:

- Increase daily study hours  
- Improve class attendance  
- Revise weak subjects  
- Complete assignments regularly  
- Maintain healthy sleep habits  

### 📂 Bulk Student Prediction

Upload a **CSV or Excel file** containing multiple student records to:

✔ Predict performance for all students  
✔ Store results in the database  
✔ Download prediction report  

### 📊 Analytics Dashboard

The dashboard provides visual insights:

📈 Grade Distribution  
🥧 Pass vs Fail Ratio  
📉 Predicted Score Distribution  
⚠️ List of At-Risk Students  

All prediction data is stored in an **SQLite database**.

---

## 📊 Input Features Used

| Feature | Description |
|---------|-------------|
| 📚 Study Hours | Hours studied per day |
| 🏫 Attendance | Attendance percentage |
| 📝 Previous Score | Previous exam marks |
| 📂 Assignments | Number of assignments completed |
| 😴 Sleep Hours | Average sleep per day |

---

## 🧠 Machine Learning Models

| Model | Purpose |
|------|---------|
| **Linear Regression** | Predict Final Score |
| **Logistic Regression (with StandardScaler)** | Predict Pass/Fail |
| **Random Forest Classifier** | Predict Student Grade |

All models are trained using **Scikit-learn** and saved with **Joblib**.

---

## 🧰 Tech Stack Used

| Technology | Purpose |
|------------|---------|
| Python 🐍 | Core Programming |
| Pandas & NumPy | Data Processing |
| Scikit-learn | Machine Learning |
| Joblib | Model Saving |
| Streamlit | Web App Interface |
| Matplotlib | Data Visualization |
| SQLite | Data Storage |

---

## 🗂️ Project Structure

```bash
AI_Student_Performance_System/
│
├── app.py                    # Streamlit Web Application
├── train_model.py            # Model training script
├── student_performance.py    # Dataset generation
├── analytics.py              # Dashboard data loader
├── database.py               # SQLite database operations
├── prediction.py             # Console-based prediction
│
├── regression_model.pkl      # Saved regression model (generated)
├── pass_fail_model.pkl       # Saved pass/fail model (generated)
├── grade_model.pkl           # Saved grade model (generated)
├── feature_columns.pkl       # Feature list (generated)
│
├── students.db               # SQLite database (auto-created)
└── README.md                 # Project documentation
```

---

## ⚙️ How to Run the Project

### 1️⃣ Install Dependencies

```bash
pip install pandas numpy scikit-learn joblib streamlit matplotlib openpyxl
```

### 2️⃣ Train the Machine Learning Models

```bash
python train_model.py
```

✔ Generates dataset  
✔ Trains ML models  
✔ Saves `.pkl` model files  

### 3️⃣ Run the Streamlit Web Application

```bash
streamlit run app.py
```

Your browser will open with the **Student Performance Prediction System** 🎉

---

## 📈 Example Prediction Output

```
Final Score (Predicted): 84.63
Pass Probability: 88.4%
Result: PASS
Grade: A
Risk Level: MODERATE
```

---

## 🎯 Project Objective

This project shows how **Artificial Intelligence in Education** can:

📌 Identify academically at-risk students early  
📌 Predict student outcomes before final exams  
📌 Help teachers take preventive actions  
📌 Enable data-driven academic decision-making  

---

## 🚀 Future Improvements

- 🌍 Deploy the web app online  
- 📊 Add advanced performance analytics  
- 🧠 Train on real educational datasets  
- 🤖 Integrate Deep Learning models  
- 📧 Send alerts for high-risk students  

---

## 👨‍💻 Author

**Nikhil Kumar**  
AI & Machine Learning Enthusiast 🚀  

---

<h3 align="center">🌟 If you like this project, give it a ⭐ on GitHub and support the journey!</h3>
