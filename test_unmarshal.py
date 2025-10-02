"""Test script to reproduce the unmarshalling error with timestamp attribute type

This script tests the unmarshalling of a query response containing a 'timestamp' attribute.
The installed package (v0.0.18) has a bug where PostV2ObjectsObjectRecordsQueryValueTimestamp.value
is defined as a date type instead of str, causing validation errors.

Toggle USE_INSTALLED_PACKAGE to compare:
- True: Uses pip-installed package (reproduces the error)
- False: Uses local source (should work correctly)
"""

import sys
# Toggle this to test installed package vs local source
USE_INSTALLED_PACKAGE = True

if not USE_INSTALLED_PACKAGE:
    sys.path.insert(0, '/Users/elvis/Documents/elviskahoro/attio-sdk-python/src')

import json
from attio import models
from attio.utils.unmarshal_json_response import unmarshal_json_response

# Read the test.json file
with open("test.json", "r") as f:
    response_json = json.load(f)

print(f"Testing with {'INSTALLED' if USE_INSTALLED_PACKAGE else 'LOCAL SOURCE'} package")
print("Testing unmarshalling of test.json with timestamp attribute...")
print(f"Response keys: {response_json.keys()}")
print()

print("=" * 80)
print("TEST 1: Query response with timestamp attribute")
print("=" * 80)
try:
    # Try to unmarshal as a query response (which is where the error occurs)
    # The query endpoint returns multiple records in {data: [...]}

    # Create a mock response object
    from unittest.mock import Mock

    mock_response = Mock()
    mock_response.text = json.dumps(response_json)  # Use the full response with array
    mock_response.headers = {'content-type': 'application/json'}

    result = unmarshal_json_response(
        models.PostV2ObjectsObjectRecordsQueryResponse,  # Use Query response model
        mock_response
    )
    print("✓ Unmarshalling successful!")
    print(f"Result type: {type(result)}")
    print(f"Result data type: {type(result.data)}")
    print(f"Number of records: {len(result.data)}")
except Exception as e:
    print(f"✗ Unmarshalling failed with error:")
    print(f"Error type: {type(e).__name__}")
    print()
    # Print full error for debugging
    print(str(e))

print()
print("=" * 80)
print("TEST 2: Error response with uniqueness_conflict code")
print("=" * 80)

# Test the uniqueness_conflict error response
error_response = {
    "status_code": 400,
    "type": "invalid_request_error",
    "code": "uniqueness_conflict",
    "message": 'The value "{\\"email_address\\":\\"bethleham.a@gmail.com\\"}" provided for attribute with ID "b8bfd231-5bd9-4092-9d39-dbf3f0e6e0d9" conflicts with one already in the system.'
}

try:
    from attio.errors.post_v2_objects_object_recordsop import PostV2ObjectsObjectRecordsValueNotFoundErrorData

    mock_error_response = Mock()
    mock_error_response.text = json.dumps(error_response)
    mock_error_response.headers = {'content-type': 'application/json'}
    mock_error_response.status_code = 400

    # Try to unmarshal as an error response using the ValueNotFoundError model
    # This should fail because it only accepts code: "value_not_found"
    result = unmarshal_json_response(
        PostV2ObjectsObjectRecordsValueNotFoundErrorData,
        mock_error_response
    )
    print("✓ Error response unmarshalling successful!")
    print(f"Result: {result}")
except Exception as e:
    print(f"✗ Error response unmarshalling failed:")
    print(f"Error type: {type(e).__name__}")
    print()
    print(str(e)[:500])  # Limit output
