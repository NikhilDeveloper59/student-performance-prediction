<<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Segoe+UI&size=34&duration=4500&pause=1000&color=2E86C1&center=true&vCenter=true&repeat=false&width=1200&lines=AI-Based+Student+Performance+Prediction+and+Early+Warning+System+using+ML" alt="Typing Title" />
</p>
>

<p align="center">
  <img src="https://img.icons8.com/external-flaticons-lineal-color-flat-icons/512/external-student-back-to-school-flaticons-lineal-color-flat-icons.png" width="18%" alt="Student AI Banner"/>
</p>

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

- 📈 Final Score Prediction  
- ✅ PASS / ❌ FAIL Detection  
- 🏆 Grade Classification (A+, A, B, C, P, F)

### 🧠 Academic Early Warning System

| Risk Factor | Impact |
|-------------|--------|
| Low study hours | High academic risk |
| Poor attendance | Performance decline |
| Weak previous scores | Learning gaps |
| Fewer assignments | Low engagement |
| Insufficient sleep | Reduced concentration |

Students are categorized into:

🚨 **High Risk**  
⚠️ **Moderate Risk**  
✅ **Low Risk**

### 💡 AI-Based Suggestions

The system provides personalized tips like:

- Increase daily study hours  
- Improve attendance  
- Revise weak subjects  
- Complete assignments on time  
- Maintain healthy sleep habits  

### 📂 Bulk Student Prediction

Upload a **CSV or Excel file** to:

✔ Predict performance for multiple students  
✔ Store results in database  
✔ Download prediction report  

### 📊 Analytics Dashboard

Visual insights include:

📈 Grade Distribution  
🥧 Pass vs Fail Ratio  
📉 Score Distribution  
⚠️ At-Risk Students List  

All data is stored in **SQLite**.

---

## 📊 Input Features Used

| Feature | Description |
|---------|-------------|
| 📚 Study Hours | Hours studied per day |
| 🏫 Attendance | Attendance percentage |
| 📝 Previous Score | Previous exam marks |
| 📂 Assignments | Assignments completed |
| 😴 Sleep Hours | Average sleep per day |

---

## 🧠 Machine Learning Models

| Model | Purpose |
|------|---------|
| **Linear Regression** | Final Score Prediction |
| **Logistic Regression + StandardScaler** | Pass/Fail Prediction |
| **Random Forest Classifier** | Grade Classification |

Models are trained using **Scikit-learn** and saved using **Joblib**.

---

## 🧰 Tech Stack Used

| Technology | Purpose |
|------------|---------|
| Python 🐍 | Core Programming |
| Pandas & NumPy | Data Processing |
| Scikit-learn | Machine Learning |
| Joblib | Model Saving |
| Streamlit | Web App Interface |
| Matplotlib | Visualization |
| SQLite | Database |

---

## 🗂️ Project Structure

```bash
AI_Student_Performance_System/
│
├── app.py
├── train_model.py
├── student_performance.py
├── analytics.py
├── database.py
├── prediction.py
│
├── regression_model.pkl
├── pass_fail_model.pkl
├── grade_model.pkl
├── feature_columns.pkl
│
├── students.db
└── README.md
```

---

## ⚙️ How to Run the Project

### 1️⃣ Install Dependencies

```bash
pip install pandas numpy scikit-learn joblib streamlit matplotlib openpyxl
```

### 2️⃣ Train the Models

```bash
python train_model.py
```

### 3️⃣ Run the Web App

```bash
streamlit run app.py
```

---

## 📈 Example Output

```
Final Score (Predicted): 84.63
Pass Probability: 88.4%
Result: PASS
Grade: A
Risk Level: MODERATE
```

---

## 🎯 Project Objective

This project demonstrates how **AI in Education** can:

📌 Identify at-risk students early  
📌 Predict academic outcomes  
📌 Support data-driven teaching decisions  

---

## 🚀 Future Improvements

- Deploy the app online  
- Add advanced analytics  
- Use real-world datasets  
- Add Deep Learning models  
- Automated alerts for high-risk students  

---

## 👨‍💻 Author

**Nikhil Kumar**  
AI & Machine Learning Enthusiast 🚀  

---

<h3 align="center">🌟 If you like this project, give it a ⭐ on GitHub!</h3>
