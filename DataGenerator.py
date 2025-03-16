import uuid
import random
from datetime import datetime, timedelta 
import pandas as pd

locations = ["California, USA", "New York, USA", "Texas, USA", "Ontario, Canada", "London, UK"]
device_types = ["mobile", "desktop", "tablet"]
card_types = ["credit", "debit", "prepaid"]

def generate_transaction():
    return {
        "transaction_id": f"T{uuid.uuid4().hex[:6].upper()}",
        "user_id": f"U{random.randint(10000, 99999)}",
        "timestamp": (datetime.utcnow() - timedelta(minutes=random.randint(1, 10000))).isoformat() + "Z",
        "amount": round(random.uniform(10, 1000), 2),
        "device_type": random.choice(device_types),
        "location": random.choice(locations),
        "is_vpn": random.choice([True, False]),
        "card_type": random.choice(card_types),
        "status": random.choice(["approved", "declined"]),
        # For 10%  Fraud Data 
        "is_fraud": random.choices([0, 1],weights=[90, 10])[0]
    }


noOfRows = 10000
dataFrame = pd.DataFrame()
for i in range(noOfRows):
    data = pd.DataFrame([generate_transaction()])
    dataFrame = pd.concat([dataFrame,data],ignore_index=True)

dataFrame.to_csv("D:/SSense/data.csv")
    