"""Generate synthetic customer records for an authorized DLP test."""
import json
from pathlib import Path

records = [
    {
        "user_id": f"TEST-{i:04d}",
        "name": f"Test Customer {i:02d}",
        "email": f"customer{i:02d}@example.com",
        "department": "Finance" if i % 2 else "Human Resources",
        "customer_note": (
            "Confidential customer account review. The customer requested "
            "a copy of their billing history and an update to their contact details. "
            "Access to this customer record is restricted to the assigned account team."
        ),
    }
    for i in range(1, 21)
]
payload = {
    "test_id": "cisco-sse-semantic-20261007",
    "synthetic": True,
    "description": "Entirely fictional customer records for an authorized DLP test.",
    "users": records,
}
path = Path(__file__).with_name("synthetic_users.json")
path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(path.read_text(encoding="utf-8"))
