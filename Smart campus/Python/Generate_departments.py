import pandas as pd

departments = [
    {
        "Department_ID": 101,
        "Department_Name": "Computer Science",
        "HOD": "Dr. Amit Sharma",
        "Building": "Block A"
    },
    {
        "Department_ID": 102,
        "Department_Name": "Mechanical",
        "HOD": "Dr. Neha Verma",
        "Building": "Block B"
    },
    {
        "Department_ID": 103,
        "Department_Name": "Civil",
        "HOD": "Dr. Rajesh Singh",
        "Building": "Block C"
    },
    {
        "Department_ID": 104,
        "Department_Name": "Electrical",
        "HOD": "Dr. Pooja Gupta",
        "Building": "Block D"
    },
    {
        "Department_ID": 105,
        "Department_Name": "Electronics",
        "HOD": "Dr. Vikas Kumar",
        "Building": "Block E"
    },
    {
        "Department_ID": 106,
        "Department_Name": "Information Technology",
        "HOD": "Dr. Anjali Mehta",
        "Building": "Block F"
    },
    {
        "Department_ID": 107,
        "Department_Name": "MBA",
        "HOD": "Dr. Rakesh Jain",
        "Building": "Block G"
    },
    {
        "Department_ID": 108,
        "Department_Name": "MCA",
        "HOD": "Dr. Priya Saxena",
        "Building": "Block H"
    }
]

# Convert list to DataFrame
df = pd.DataFrame(departments)

# Save to Excel
df.to_excel("../Dataset/Departments.xlsx", index=False)

print("Departments dataset created successfully!")