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
X = df[features]

# ------------- REGRESSION MODEL ------------------
y_reg = df["final_score"]

X_train, X_test, y_train, y_test = train_test_split(X, y_reg, test_size=0.2, random_state=42)

reg_model = LinearRegression()
reg_model.fit(X_train, y_train)

pred_reg = reg_model.predict(X_test)
print("📈 Regression MAE:", mean_absolute_error(y_test, pred_reg))
print("📈 Regression RMSE:", np.sqrt(mean_squared_error(y_test, pred_reg)))
print("📈 Regression R2:", r2_score(y_test, pred_reg))

joblib.dump(reg_model, "regression_model.pkl")


# ------------- PASS/FAIL MODEL ----------------
y_pass = df["result"]

X_train, X_test, y_train, y_test = train_test_split(X, y_pass, test_size=0.2, random_state=42)

pass_model = Pipeline([
    ('scaler', StandardScaler()), # It scales (standardizes) the features.
    ('classifier', LogisticRegression()) # after standardized each feature apply them
])

pass_model.fit(X_train, y_train)
pred_pass = pass_model.predict(X_test)

print("\n🎯 Pass/Fail Accuracy:", accuracy_score(y_test, pred_pass))
# print(classification_report(y_test, pred_pass))
joblib.dump(pass_model, "pass_fail_model.pkl")


# ------------- GRADE MODEL -------------------
y_grade = df["grade"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y_grade, test_size=0.2, random_state=42, stratify=y_grade
)

grade_model = RandomForestClassifier(
    n_estimators=600,
    max_depth=10,
    min_samples_split=5,
    class_weight="balanced",
    random_state=42
)
grade_model.fit(X_train, y_train)

pred_grade = grade_model.predict(X_test)

print("\n🏆 Grade Model Accuracy:", accuracy_score(y_test, pred_grade))
# print(classification_report(y_test, pred_grade))

joblib.dump(grade_model, "grade_model.pkl")

print("\n✅ All models trained and saved successfully!")
