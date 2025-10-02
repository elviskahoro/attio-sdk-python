"""Test script to reproduce the unmarshalling error with example.json"""

import json
from attio.models import post_v2_objects_object_recordsop as models
from attio.utils.serializers import unmarshal_json

# Read the example.json file
with open("example.json", "r") as f:
    response_json = json.load(f)

# Extract the data array (the API returns {data: [record]})
# But the model expects just the record object
record_data = response_json["data"][0]

print("Testing unmarshalling of example.json...")
print(f"Record data keys: {record_data.keys()}")
print()

try:
    # Try to unmarshal the record data
    result = unmarshal_json(
        json.dumps(record_data),
        models.PostV2ObjectsObjectRecordsDataResponse
    )
    print("✓ Unmarshalling successful!")
    print(f"Result type: {type(result)}")
    print(f"Record ID: {result.id}")
except Exception as e:
    print(f"✗ Unmarshalling failed with error:")
    print(f"Error type: {type(e).__name__}")
    print()
    # Print full error for debugging
    print(str(e))
