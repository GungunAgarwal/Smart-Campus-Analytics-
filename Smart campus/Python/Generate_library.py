import pandas as pd
import numpy as np
from faker import Faker
from pathlib import Path
from datetime import timedelta

fake = Faker("en_IN")

# Project Path
BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = BASE_DIR / "Dataset"

books = [
    "Python Programming",
    "Data Structures",
    "Database Management Systems",
    "Operating Systems",
    "Computer Networks",
    "Artificial Intelligence",
    "Machine Learning",
    "Cloud Computing",
    "Cyber Security",
    "Software Engineering",
    "Digital Electronics",
    "Engineering Mathematics",
    "Thermodynamics",
    "Fluid Mechanics",
    "Microprocessors",
    "Electrical Machines",
    "Structural Analysis",
    "Marketing Management",
    "Financial Accounting",
    "Business Analytics"
]

library = []

for i in range(5000):

    issue_date = fake.date_between(
        start_date="-365d",
        end_date="today"
    )

    return_date = issue_date + timedelta(
        days=np.random.randint(5, 31)
    )

    fine = np.random.choice(
        [0, 0, 0, 10, 20, 50, 100],
        p=[0.50, 0.15, 0.10, 0.10, 0.07, 0.05, 0.03]
    )

    library.append({
        "Issue_ID": 9001 + i,
        "Student_ID": np.random.randint(1001, 1501),
        "Book_Name": np.random.choice(books),
        "Issue_Date": issue_date,
        "Return_Date": return_date,
        "Fine": fine
    })

df = pd.DataFrame(library)

df.to_excel(DATASET_DIR / "Library.xlsx", index=False)

print("Library dataset created successfully!")