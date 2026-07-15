import pandas as pd
import numpy as np
from pathlib import Path

# Project Path
BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = BASE_DIR / "Dataset"

# Department Mapping
department_data = {
    101: "Computer Science",
    102: "Mechanical",
    103: "Civil",
    104: "Electrical",
    105: "Electronics",
    106: "Information Technology",
    107: "MBA",
    108: "MCA"
}

courses = []

course_names = [
    "Programming in Python",
    "Database Management Systems",
    "Data Structures",
    "Operating Systems",
    "Computer Networks",
    "Software Engineering",
    "Machine Learning",
    "Artificial Intelligence",
    "Cloud Computing",
    "Cyber Security",
    "Thermodynamics",
    "Fluid Mechanics",
    "Engineering Mathematics",
    "Digital Electronics",
    "Electrical Machines",
    "Microprocessors",
    "Structural Analysis",
    "Surveying",
    "Marketing Management",
    "Financial Accounting"
]

for i in range(100):

    dept_id = np.random.choice(list(department_data.keys()))

    courses.append({
        "Course_ID": 3001 + i,
        "Course_Name": np.random.choice(course_names),
        "Department_ID": dept_id,
        "Department_Name": department_data[dept_id],
        "Semester": np.random.randint(1, 9),
        "Credits": np.random.choice([2, 3, 4]),
        "Faculty_ID": np.random.randint(2001, 2051)
    })

df = pd.DataFrame(courses)

df.to_excel(DATASET_DIR / "Courses.xlsx", index=False)

print("Courses dataset created successfully!")