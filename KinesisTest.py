import boto3
import json
import uuid
import random
from datetime import datetime, timedelta 
import time

kinesis = boto3.client('kinesis', region_name='ca-central-1')

stream_name = 'fraud-detection-stream'

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
        "status": random.choice(["approved", "declined",])
    }

while True:
    # Generating Random Data
    dataGenerated = generate_transaction()
    # Putting Kinesis stream
    try:
        response = kinesis.put_record(
            StreamName=stream_name,
            Data=json.dumps(dataGenerated),
            PartitionKey=str(dataGenerated['user_id'])
        )
    except:
        print("Error")
    print(response)
    print(f"Sent: {dataGenerated}")
    time.sleep(0.5)
    break 