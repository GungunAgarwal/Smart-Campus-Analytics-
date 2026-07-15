import pandas as pd
import numpy as np
from faker import Faker
from pathlib import Path
from datetime import timedelta

fake = Faker("en_IN")

# Project path
BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = BASE_DIR / "Dataset"

attendance = []

for i in range(20000):

    student_id = np.random.randint(1001, 1501)     # Students IDs
    course_id = np.random.randint(3001, 3101)      # Course IDs

    attendance_date = fake.date_between(
        start_date="-180d",
        end_date="today"
    )

    status = np.random.choice(
        ["Present", "Absent"],
        p=[0.88, 0.12]
    )

    attendance.append({
        "Attendance_ID": 50001 + i,
        "Student_ID": student_id,
        "Course_ID": course_id,
        "Attendance_Date": attendance_date,
        "Status": status
    })

df = pd.DataFrame(attendance)

df.to_excel(DATASET_DIR / "Attendance.xlsx", index=False)

print("Attendance dataset created successfully!")