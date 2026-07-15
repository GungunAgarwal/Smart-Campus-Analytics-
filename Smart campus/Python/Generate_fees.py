import pandas as pd
import numpy as np
from faker import Faker
from pathlib import Path

fake = Faker("en_IN")

# Project Path
BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = BASE_DIR / "Dataset"

fees = []

payment_modes = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Cash"
]

for i in range(500):

    status = np.random.choice(
        ["Paid", "Pending"],
        p=[0.85, 0.15]
    )

    if status == "Paid":
        payment_date = fake.date_between(
            start_date="-365d",
            end_date="today"
        )
    else:
        payment_date = ""

    fees.append({
        "Payment_ID": 6001 + i,
        "Student_ID": np.random.randint(1001, 1501),
        "Amount": np.random.choice(
            [25000, 30000, 35000, 40000, 45000, 50000]
        ),
        "Payment_Date": payment_date,
        "Status": status,
        "Payment_Mode": np.random.choice(payment_modes)
    })

df = pd.DataFrame(fees)

df.to_excel(DATASET_DIR / "Fees.xlsx", index=False)

print("Fees dataset created successfully!")