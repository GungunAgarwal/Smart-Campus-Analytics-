import pandas as pd
import numpy as np
from faker import Faker
from pathlib import Path

fake = Faker("en_IN")

# Project Path
BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = BASE_DIR / "Dataset"

categories = [
    "WiFi Issue",
    "Laptop Problem",
    "Projector Issue",
    "Software Installation",
    "Printer Issue",
    "Email Access",
    "Password Reset",
    "Computer Not Working",
    "Network Issue",
    "Lab Equipment"
]

priorities = [
    "Low",
    "Medium",
    "High"
]

statuses = [
    "Open",
    "In Progress",
    "Resolved",
    "Closed"
]

tickets = []

for i in range(1000):

    created_date = fake.date_between(
        start_date="-365d",
        end_date="today"
    )

    status = np.random.choice(
        statuses,
        p=[0.20, 0.25, 0.40, 0.15]
    )

    if status in ["Resolved", "Closed"]:
        resolved_date = fake.date_between(
            start_date=created_date,
            end_date="today"
        )
    else:
        resolved_date = ""

    tickets.append({
        "Ticket_ID": 8001 + i,
        "Student_ID": np.random.randint(1001, 1501),
        "Category": np.random.choice(categories),
        "Priority": np.random.choice(
            priorities,
            p=[0.40, 0.40, 0.20]
        ),
        "Status": status,
        "Created_Date": created_date,
        "Resolved_Date": resolved_date
    })

df = pd.DataFrame(tickets)

df.to_excel(DATASET_DIR / "IT_Tickets.xlsx", index=False)

print("IT Tickets dataset created successfully!")