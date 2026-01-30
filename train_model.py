import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error,r2_score,mean_squared_error, accuracy_score, classification_report
from student_performance import generate_dataset

# Generate dataset
df = generate_dataset()

features = ["study_hours", "attendance", "previous_score", "assignments", "sleep_hours"]
joblib.dump(features, "feature_columns.pkl")
X = df[features]

# ------------- REGRESSION MODEL ------------------
y_reg = df["final_score"]
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X, y_reg, test_size=0.2, random_state=42)

reg_model = LinearRegression()
reg_model.fit(X_train_reg, y_train_reg)
pred_reg = reg_model.predict(X_test_reg)

print("📈 Regression MAE:", mean_absolute_error(y_test_reg, pred_reg))
print("📈 Regression RMSE:", np.sqrt(mean_squared_error(y_test_reg, pred_reg)))
print("📈 Regression R2:", r2_score(y_test_reg, pred_reg))

joblib.dump(reg_model, "regression_model.pkl")


# ------------- PASS/FAIL MODEL ----------------
y_passfail = df["result"]

X_train_pf, X_test_pf, y_train_pf, y_test_pf = train_test_split(X, y_passfail, test_size=0.2, random_state=42)

pf_model = Pipeline([
    ('scaler', StandardScaler()), # It scales (standardizes) the features.
    ('classifier', LogisticRegression()) # after standardized each feature apply them
])

pf_model.fit(X_train_pf, y_train_pf)
pred_pf = pf_model.predict(X_test_pf)

print("🎯 Pass/Fail Accuracy:", accuracy_score(y_test_pf, pred_pf))
# print(classification_report(y_test, pred_pass))
joblib.dump(pf_model, "pass_fail_model.pkl")


# ------------- GRADE MODEL -------------------
y_grade = df["grade"]

X_train_gr, X_test_gr, y_train_gr, y_test_gr = train_test_split(X, y_grade, test_size=0.2, random_state=42)


grade_model = RandomForestClassifier(
    n_estimators=300,
    max_depth=10,
    min_samples_split=5,
    class_weight="balanced",
    random_state=42
)
grade_model.fit(X_train_gr, y_train_gr)
pred_grade = grade_model.predict(X_test_gr)

print("🏆 Grade Model Accuracy:", accuracy_score(y_test_gr, pred_grade))
# print(classification_report(y_test, pred_grade))

joblib.dump(grade_model, "grade_model.pkl")


print("\n📊 MODEL PERFORMANCE SUMMARY")
print(f"Regression R2 Score: {r2_score(y_test_reg, pred_reg):.2f}")
print(f"Pass/Fail Accuracy: {accuracy_score(y_test_pf, pred_pf):.2f}")
print(f"Grade Model Accuracy: {accuracy_score(y_test_gr, pred_grade):.2f}")

print("\n✅ All models trained and saved successfully!")
