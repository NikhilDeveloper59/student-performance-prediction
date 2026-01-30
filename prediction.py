import pandas as pd
import joblib

# Load models
reg_model = joblib.load("regression_model.pkl")
pass_model = joblib.load("pass_fail_model.pkl")
grade_model = joblib.load("grade_model.pkl")

print("✅ All models loaded successfully!")

print("\n🔮 Enter Student Details")

study_hours = float(input("Study hours per day (1-10): "))
attendance = float(input("Attendance percentage (50-100): "))
previous_score = float(input("Previous exam score (40-90): "))
assignments = float(input("Assignments completed (1-10): "))
sleep_hours = float(input("Sleep hours per day (4-8): "))

new_data = pd.DataFrame({
    "study_hours": [study_hours],
    "attendance": [attendance],
    "previous_score": [previous_score],
    "assignments": [assignments],
    "sleep_hours": [sleep_hours]
})

# Predictions
pred_score = reg_model.predict(new_data)[0]
pred_pass = pass_model.predict(new_data)[0]
pred_grade = grade_model.predict(new_data)[0]

print("\n📊 STUDENT PERFORMANCE PREDICTION")
print("Final Score (Predicted):", round(pred_score, 2))
print("Result:", "PASS ✅" if pred_pass == 1 else "FAIL ❌")
print("Grade:", pred_grade)

print("\n🎗🎀Performance 🎀")

if pred_score < 40:
    print("⚠️ Student is at RISK of failing.")

if study_hours < 3:
    print("📘 Suggestion: Increase study hours.")

if attendance < 70:
    print("🏫 Suggestion: Improve attendance.")

if sleep_hours < 5:
    print("😴 Suggestion: Get proper sleep for better focus.")
