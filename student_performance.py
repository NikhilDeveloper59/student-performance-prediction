import pandas as pd
import numpy as np

def generate_dataset(rows=1000):
    np.random.seed(42)

    data = {
        "study_hours": np.random.randint(1, 11, rows),
        "attendance": np.random.randint(50, 101, rows),
        "previous_score": np.random.randint(40, 91, rows),
        "assignments": np.random.randint(1, 11, rows),
        "sleep_hours": np.random.randint(4, 9, rows),
    }

    df = pd.DataFrame(data)
    
    # Create Final Score (Regression Target)
    df["final_score"] = (
        df["study_hours"] * 5 +
        df["attendance"] * 0.2 +
        df["previous_score"] * 0.3 +
        df["assignments"] * 2 -
        df["sleep_hours"] * 1.5 +
        np.random.normal(0, 4, rows)
    ).clip(0, 100)

    # Pass / Fail (Binary Classification)
    PASS_MARK = 30  # Standard pass limit
    df["result"] = df["final_score"].apply(lambda x: 1 if x >= PASS_MARK else 0)


    # Grade (Multi-class Classification)
    def get_grade(score):
        if score >= 90:
            return "A+"
        elif score >= 80:
            return "A"
        elif score >= 60:
            return "B"
        elif score >= 40:
            return "C"
        elif score >= 30:
            return "P"   # Pass class
        else:
            return "F"   # Fail


    df["grade"] = df["final_score"].apply(get_grade)

    return df
