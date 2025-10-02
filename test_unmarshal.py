"""Test script to reproduce the unmarshalling error with example.json"""

import sys
sys.path.insert(0, '/Users/elvis/Documents/elviskahoro/attio-sdk-python/src')

import json
from attio import models
from attio.utils.unmarshal_json_response import unmarshal_json_response

# Read the test.json file
with open("test.json", "r") as f:
    response_json = json.load(f)

print("Testing unmarshalling of test.json...")
print(f"Response keys: {response_json.keys()}")
print()

try:
    # Try to unmarshal the full response (it expects {data: record_object})
    # The POST endpoint returns a single record object wrapped in {data: {...}}
    # Extract just one record for testing
    single_record_response = {"data": response_json["data"][0]}

    # Create a mock response object
    from unittest.mock import Mock

    mock_response = Mock()
    mock_response.text = json.dumps(single_record_response)
    mock_response.headers = {'content-type': 'application/json'}

    result = unmarshal_json_response(
        models.PostV2ObjectsObjectRecordsResponse,
        mock_response
    )
    print("✓ Unmarshalling successful!")
    print(f"Result type: {type(result)}")
    print(f"Result data type: {type(result.data)}")
    print(f"Record ID: {result.data.id}")
except Exception as e:
    print(f"✗ Unmarshalling failed with error:")
    print(f"Error type: {type(e).__name__}")
    print()
    # Print full error for debugging
    print(str(e))
