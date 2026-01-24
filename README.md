<p align="center">
  <img src="https://img.icons8.com/external-flaticons-lineal-color-flat-icons/512/external-student-back-to-school-flaticons-lineal-color-flat-icons.png" width="18%" alt="Student AI Banner"/>
</p>

<h1 align="center">🎓 Student Performance Prediction System</h1>

<p align="center">
  <b>An End-to-End Machine Learning Project for Predicting Student Outcomes 📊</b><br>
  Predict <b>Final Score</b>, <b>Pass/Fail Result</b>, and <b>Grade</b> using AI models trained on academic & lifestyle data.
</p>

<h3 align="center">🧩 Machine Learning Models Used</h3>
<p align="center">
  <img src="https://img.shields.io/badge/Linear%20Regression-Score%20Prediction-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Logistic%20Regression-Pass%2FFail-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Random%20Forest-Grade%20Prediction-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Scikit--Learn-ML%20Library-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Python-Programming-yellow?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Joblib-Model%20Saving-purple?style=for-the-badge" />
</p>

---

## 📌 Project Overview

This system uses **Machine Learning** to analyze student study patterns and predict:

✅ Final Exam Score (Regression)  
✅ Pass or Fail Status (Binary Classification)  
✅ Final Grade — A / B / C / D (Multi-Class Classification)  

It demonstrates how AI can support **education analytics** and **student performance monitoring**.

---

## ✨ Features

### 📊 Score Prediction
Predicts the **numerical final exam score** using **Linear Regression**.

### 🎯 Pass / Fail Detection
Determines whether a student will **PASS or FAIL** using **Logistic Regression**.

### 🏆 Grade Classification
Assigns a **Grade (A/B/C/D)** using a **Random Forest Classifier**.

### 💾 Model Persistence
All trained models are saved as `.pkl` files and reused without retraining.

### 🖥️ Prediction Interfaces
✔ Console-based prediction  
✔ Streamlit Web App interface  

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

## 🧠 Tech Stack Used

| Technology | Purpose |
|------------|---------|
| Python 🐍 | Core Programming |
| Pandas | Data Handling |
| NumPy | Numerical Operations |
| Scikit-learn | ML Model Training |
| Joblib | Model Saving & Loading |
| Streamlit | Web App Interface |

---

## 🗂️ Project Structure

Student_Performance_Prediction/
│
├── student_performance.py
├── train_model.py
├── prediction.py
├── app.py                  # Streamlit Web App
├── regression_model.pkl
├── pass_fail_model.pkl
├── grade_model.pkl
└── README.md

---

<h2>⚙️ How to Run the Project</h2>

<h3>1️⃣ Install Dependencies</h3>

<pre>pip install pandas numpy scikit-learn joblib streamlit</pre>

<h3>2️⃣ Train the Models</h3>

<pre>python train_model.py</pre>

<ul>
  <li>✔ Generates dataset</li>
  <li>✔ Trains all models</li>
  <li>✔ Saves <code>.pkl</code> files</li>
</ul>

<h3>3️⃣ Run Console Prediction</h3>

<pre>python prediction.py</pre>

<h3>4️⃣ Run Web App (Recommended)</h3>

<pre>streamlit run app.py</pre>

---

<h2>📈 Example Output</h2>

<pre>
Final Score (Predicted): 90.77
Result: PASS
Grade: A
</pre>

---

<h2>🎯 Project Objective</h2>

<p>This project demonstrates how <b>Machine Learning</b> can be applied in the education domain to:</p>

<ul>
  <li>📌 Identify at-risk students</li>
  <li>📌 Predict academic performance</li>
  <li>📌 Help educators make data-driven decisions</li>
</ul>

---

<h2>🏆 Future Improvements</h2>

<ul>
  <li>🚀 Add visualization dashboard</li>
  <li>🌐 Deploy the web app online</li>
  <li>🧾 Use real-world student datasets</li>
  <li>📊 Add deep learning models</li>
</ul>

---

<h2>👨‍💻 Author</h2>

<p><b>Nikhil Kumar</b><br>
Machine Learning Enthusiast 🚀</p>

---

<h3 align="center">⭐ If you like this project, give it a star on GitHub!</h3>

```bash

