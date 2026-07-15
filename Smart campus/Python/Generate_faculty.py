import pandas as pd
import numpy as np
from faker import Faker

fake = Faker("en_IN")

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

designations = [
    "Assistant Professor",
    "Associate Professor",
    "Professor"
]

faculty = []

for i in range(50):
    dept_id = np.random.choice(list(department_data.keys()))

    faculty.append({
        "Faculty_ID": 2001 + i,
        "Faculty_Name": fake.name(),
        "Department_ID": dept_id,
        "Department_Name": department_data[dept_id],
        "Designation": np.random.choice(designations),
        "Experience_Years": np.random.randint(1, 31),
        "Email": fake.email(),
        "Phone_Number": fake.phone_number()
    })

df = pd.DataFrame(faculty)

df.to_excel("../Dataset/Faculty.xlsx", index=False)

print("Faculty dataset created successfully!")