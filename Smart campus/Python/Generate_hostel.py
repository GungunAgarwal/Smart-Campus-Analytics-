import pandas as pd
import numpy as np
from faker import Faker
from pathlib import Path

fake = Faker("en_IN")

# Project Path
BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = BASE_DIR / "Dataset"

hostels = [
    "A Block Hostel",
    "B Block Hostel",
    "C Block Hostel",
    "Girls Hostel 1",
    "Girls Hostel 2"
]

fee_status = [
    "Paid",
    "Pending"
]

hostel_data = []

for i in range(500):

    hostel_data.append({
        "Hostel_ID": 7001 + i,
        "Student_ID": np.random.randint(1001, 1501),
        "Hostel_Name": np.random.choice(hostels),
        "Room_No": np.random.randint(101, 501),
        "Floor": np.random.randint(1, 6),
        "Fee_Status": np.random.choice(
            fee_status,
            p=[0.90, 0.10]
        )
    })

df = pd.DataFrame(hostel_data)

df.to_excel(DATASET_DIR / "Hostel.xlsx", index=False)

print("Hostel dataset created successfully!")