import streamlit as st
st.set_page_config(page_title="Student Performance Predictor", layout="centered")

import pandas as pd
import joblib
import matplotlib.pyplot as plt
import analytics
from database import create_table, insert_record
import sqlite3

create_table()

# ----------- SIDEBAR NAVIGATION -----------
page = st.sidebar.selectbox("Select Page", ["Prediction", "Analytics Dashboard"])

# Load models
features = joblib.load("feature_columns.pkl")
reg_model = joblib.load("regression_model.pkl")
pass_model = joblib.load("pass_fail_model.pkl")
grade_model = joblib.load("grade_model.pkl")


# -------------------- 🧠 PREDICTION PAGE ----------------------
if page == "Prediction":

    st.title("🎓 Student Performance Prediction System")
    st.write("Enter student details to predict academic performance.")

    # ---------- SINGLE STUDENT INPUT ----------
    study_hours = st.slider("Study Hours per Day", 1, 10, 5)
    attendance = st.slider("Attendance Percentage", 50, 100, 75)
    previous_score = st.slider("Previous Exam Score", 40, 90, 60)
    assignments = st.slider("Assignments Completed", 1, 10, 5)
    sleep_hours = st.slider("Sleep Hours per Day", 4, 8, 6)

    st.divider()

    # ---------- BULK UPLOAD ----------
    st.subheader("📂 Bulk Student Prediction (Upload CSV/Excel)")
    uploaded_file = st.file_uploader("Upload CSV or Excel File", type=["csv", "xlsx"])

    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith(".csv"):
                bulk_df = pd.read_csv(uploaded_file)
            else:
                bulk_df = pd.read_excel(uploaded_file, engine="openpyxl")
        except:
            st.error("Excel support requires 'openpyxl'. Install using: pip install openpyxl")
            st.stop()

        st.write("Preview of Uploaded Data:")
        st.dataframe(bulk_df.head())

        required_cols = ["study_hours", "attendance", "previous_score", "assignments", "sleep_hours"]

        if all(col in bulk_df.columns for col in required_cols):
            bulk_df["predicted_score"] = reg_model.predict(bulk_df[required_cols])
            bulk_df["result"] = ["PASS" if p == 1 else "FAIL" for p in pass_model.predict(bulk_df[required_cols])]
            bulk_df["grade"] = grade_model.predict(bulk_df[required_cols])

            st.success("✅ Predictions completed for all students!")
            st.dataframe(bulk_df)

            for _, row in bulk_df.iterrows():
                insert_record((row["study_hours"], row["attendance"], row["previous_score"],
                               row["assignments"], row["sleep_hours"],
                               round(row["predicted_score"], 2), row["result"], row["grade"]))

            st.download_button("⬇ Download Prediction Results",
                               bulk_df.to_csv(index=False).encode("utf-8"),
                               "bulk_student_predictions.csv", "text/csv")
        else:
            st.error("File must contain: study_hours, attendance, previous_score, assignments, sleep_hours")

    st.divider()

    # ---------- SINGLE STUDENT PREDICTION ----------
    if st.button("Predict Performance"):

        new_data = pd.DataFrame({
            "study_hours": [study_hours],
            "attendance": [attendance],
            "previous_score": [previous_score],
            "assignments": [assignments],
            "sleep_hours": [sleep_hours]
        })

        pred_score = reg_model.predict(new_data)[0]
        pred_pass = pass_model.predict(new_data)[0]
        pred_grade = grade_model.predict(new_data)[0]
        pass_prob = pass_model.predict_proba(new_data)[0][1]

        st.subheader("📊 Prediction Results")
        st.metric("Final Score (Predicted)", f"{pred_score:.2f}")
        st.metric("Pass Probability", f"{pass_prob*100:.1f}%")

        if pred_pass == 1:
            st.success("Result: PASS ✅")
        else:
            st.error("Result: FAIL ❌")

        st.info(f"Predicted Grade: {pred_grade}")

        insert_record((study_hours, attendance, previous_score, assignments,
                       sleep_hours, round(pred_score, 2),
                       "PASS" if pred_pass == 1 else "FAIL", pred_grade))

        # ---------------- AI EARLY WARNING (AFTER CLICK) ----------------
        st.subheader("🧠 Academic Risk Analysis")

        risk_score = 0
        risk_messages = []

        if study_hours < 3:
            risk_score += 2
            risk_messages.append("Very low study time")
        if attendance < 65:
            risk_score += 2
            risk_messages.append("Poor attendance")
        if previous_score < 50:
            risk_score += 2
            risk_messages.append("Weak previous performance")
        if assignments < 4:
            risk_score += 1
            risk_messages.append("Low assignment completion")
        if sleep_hours < 5:
            risk_score += 1
            risk_messages.append("Insufficient sleep")

        risk_percent = min(risk_score * 15, 100)

        if pred_score < 35 or pass_prob < 0.6 or risk_score >= 6:
            st.error("🚨 HIGH RISK: Student is likely to fail without immediate improvement.")
        elif pred_score < 50 or risk_score >= 3:
            st.warning("⚠️ MODERATE RISK: Student needs better study habits.")
        else:
            st.success("✅ LOW RISK: Student is on a good track.")

        if risk_messages:
            st.info("🔎 Risk Factors: " + ", ".join(risk_messages))

        st.progress(risk_percent)
        st.caption(f"Risk Level: {risk_percent}%")

        # Suggestions
        st.subheader("💡 AI Suggestions for Improvement")
        if study_hours < 3:
            st.write("📘 Increase daily study time to 4–5 hours")
        if attendance < 75:
            st.write("🏫 Attend more classes regularly")
        if previous_score < 60:
            st.write("📝 Revise weak subjects and practice more")
        if assignments < 6:
            st.write("📂 Complete assignments on time")
        if sleep_hours < 6:
            st.write("😴 Maintain at least 6–7 hours of sleep")

        # Feature Importance
        if hasattr(grade_model, "feature_importances_"):
            st.subheader("🎁 Feature Importance")
            fig, ax = plt.subplots()
            ax.barh(new_data.columns, grade_model.feature_importances_)
            st.pyplot(fig)


# ----------------- 📊 ANALYTICS DASHBOARD --------------------
elif page == "Analytics Dashboard":

    st.title("📊 Student Performance Analytics Dashboard")
    df = analytics.load_data()

    if st.button("🗑 Reset All Student Data"):
        conn = sqlite3.connect("students.db")
        conn.execute("DELETE FROM records")
        conn.commit()
        conn.close()
        st.success("All student records deleted!")
        st.rerun()

    elif df.empty:
        st.warning("No data available yet.")
    else:
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Students Analysed", len(df))
        col2.metric("Average Predicted Score", f"{df['predicted_score'].mean():.2f}")
        col3.metric("Pass Percentage", f"{(df['result'].value_counts(normalize=True).get('PASS',0)*100):.1f}%")

        st.divider()

        # Grade Distribution
        st.subheader("🎓 Grade Distribution")
        grade_order = ["A+", "A", "B", "C", "P", "F"]
        grade_counts = df["grade"].value_counts().reindex(grade_order, fill_value=0)

        fig, ax = plt.subplots()
        ax.bar(grade_counts.index, grade_counts.values)
        for i, v in enumerate(grade_counts.values):
            ax.text(i, v + 0.1, str(v), ha='center', fontweight='bold')
        st.pyplot(fig)

        # Pass/Fail Pie Chart
        st.subheader("✅ Pass vs Fail Percentage")
        pass_fail_counts = df["result"].value_counts()

        fig2, ax2 = plt.subplots()
        ax2.pie(pass_fail_counts.values,
                labels=pass_fail_counts.index,
                autopct='%1.1f%%',
                startangle=90)
        ax2.axis('equal')
        st.pyplot(fig2)

        # Score Distribution
        st.subheader("📈 Predicted Score Distribution")
        fig3, ax3 = plt.subplots()
        ax3.hist(df["predicted_score"], bins=10, edgecolor='black')
        ax3.set_title("Distribution of Predicted Student Scores")
        ax3.set_xlabel("Predicted Exam Score")
        ax3.set_ylabel("Number of Students")
        ax3.axvline(x=30, linestyle='--')
        ax3.text(31, ax3.get_ylim()[1]*0.9, "Risk Zone (<30)", rotation=90, verticalalignment='top')
        st.pyplot(fig3)

        # Risk Students Table
        st.subheader("⚠️ Students At Academic Risk (Score < 30)")
        st.dataframe(df[df["predicted_score"] < 30])
