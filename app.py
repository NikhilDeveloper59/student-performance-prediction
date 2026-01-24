import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt


# Load models
reg_model = joblib.load("regression_model.pkl")
pass_model = joblib.load("pass_fail_model.pkl")
grade_model = joblib.load("grade_model.pkl")

st.set_page_config(page_title="Student Performance Predictor", layout="centered")

st.title("🎓 Student Performance Prediction System")
st.write("Enter student details to predict academic performance.")

# ---------------- USER INPUT ----------------
study_hours = st.slider("Study Hours per Day", 1, 10, 5)
attendance = st.slider("Attendance Percentage", 50, 100, 75)
previous_score = st.slider("Previous Exam Score", 40, 90, 60)
assignments = st.slider("Assignments Completed", 1, 10, 5)
sleep_hours = st.slider("Sleep Hours per Day", 4, 8, 6)

if st.button("Predict Performance"):

    new_data = pd.DataFrame({
        "study_hours": [study_hours],
        "attendance": [attendance],
        "previous_score": [previous_score],
        "assignments": [assignments],
        "sleep_hours": [sleep_hours]
    })

    # ---------------- PREDICTIONS ----------------
    pred_score = reg_model.predict(new_data)[0]
    pred_pass = pass_model.predict(new_data)[0]
    pred_grade = grade_model.predict(new_data)[0]

    st.subheader("📊 Prediction Results")
    st.metric("Final Score (Predicted)", f"{pred_score:.2f}")

    if pred_pass == 1:
        st.success("Result: PASS ✅")
    else:
        st.error("Result: FAIL ❌")

    st.info(f"Predicted Grade: {pred_grade}")

    # ---------------- FEATURE IMPORTANCE ----------------
    st.subheader("📌 Feature Importance for Grade Prediction")

    importances = grade_model.feature_importances_
    feature_names = new_data.columns

    fig, ax = plt.subplots()
    ax.barh(feature_names, importances)
    ax.set_xlabel("Importance Score")
    ax.set_title("Feature Importance")
    st.pyplot(fig)

    # ---------------- DOWNLOAD REPORT ----------------
    st.subheader("📄 Download Prediction Report")

    report_df = pd.DataFrame({
        "Study Hours": [study_hours],
        "Attendance %": [attendance],
        "Previous Score": [previous_score],
        "Assignments Completed": [assignments],
        "Sleep Hours": [sleep_hours],
        "Predicted Final Score": [round(pred_score, 2)],
        "Pass/Fail": ["PASS" if pred_pass == 1 else "FAIL"],
        "Predicted Grade": [pred_grade]
    })

    csv = report_df.to_csv(index=False).encode('utf-8')

    st.download_button(
        label="⬇ Download Report as CSV",
        data=csv,
        file_name="student_prediction_report.csv",
        mime="text/csv"
    )
