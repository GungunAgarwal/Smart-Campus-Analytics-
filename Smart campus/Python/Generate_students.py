import pandas as pd
import numpy as np
from faker import Faker

fake = Faker() 

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

courses = [
    "B.Tech",
    "M.Tech",
    "MBA",
    "BBA"
]

hostel_status = [
    "Yes",
    "No"
]

genders = [
    "Male",
    "Female"
]



students = []

for i in range(500):
    dept_id = np.random.randint(101, 109)
    student = {
        "Student_ID": 1001 + i,
        "Student_Name": fake.name(),
        "Gender": np.random.choice(genders),
        "Age": np.random.randint(18, 25),
        "Department_ID": dept_id,
        "Department_Name": department_data[dept_id],
        "Course": np.random.choice(courses),
        "Semester": np.random.randint(1, 9),
        "Admission_Year": np.random.randint(2021, 2026),
        "Hostel_Status": np.random.choice(hostel_status),
        "Email": fake.email(),
        "Phone_Number": fake.phone_number()
    }
    
    students.append(student)
    
    df = pd.DataFrame(students)
    
    df.to_excel("Dataset/Students.xlsx", index=False) 
       
    print("Student dataset created successfully!")
