# Meetings

## Overview

Meetings are events synced from your calendar, added manually or added from third-party integrations.

### Available Operations

* [get_v2_meetings](#get_v2_meetings) - List meetings
* [post_v2_meetings](#post_v2_meetings) - Find or create a meeting
* [get_v2_meetings_meeting_id_](#get_v2_meetings_meeting_id_) - Get a meeting

## get_v2_meetings

Lists all meetings in the workspace using a deterministic sort order.

This endpoint is in beta. We will aim to avoid breaking changes, but small updates may be made as we roll out to more users.

Required scopes: `meeting:read`, `record_permission:read`.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_/v2/meetings" method="get" path="/v2/meetings" -->
```python
from attio import SDK


with SDK(
    oauth2="<YOUR_OAUTH2_HERE>",
) as sdk:

    res = sdk.meetings.get_v2_meetings(limit=50, participants="", sort="start_asc", timezone="UTC")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             | Example                                                                 |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `limit`                                                                 | *Optional[int]*                                                         | :heavy_minus_sign:                                                      | N/A                                                                     | 50                                                                      |
| `cursor`                                                                | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | N/A                                                                     |                                                                         |
| `linked_object`                                                         | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | N/A                                                                     |                                                                         |
| `linked_record_id`                                                      | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | N/A                                                                     |                                                                         |
| `participants`                                                          | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | N/A                                                                     |                                                                         |
| `sort`                                                                  | [Optional[models.GetV2MeetingsSort]](../../models/getv2meetingssort.md) | :heavy_minus_sign:                                                      | The order in which to sort the meetings. Defaults to start_asc.         |                                                                         |
| `ends_from`                                                             | *OptionalNullable[str]*                                                 | :heavy_minus_sign:                                                      | N/A                                                                     |                                                                         |
| `starts_before`                                                         | *OptionalNullable[str]*                                                 | :heavy_minus_sign:                                                      | N/A                                                                     |                                                                         |
| `timezone`                                                              | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | N/A                                                                     |                                                                         |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |                                                                         |

### Response

**[models.GetV2MeetingsResponse](../../models/getv2meetingsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## post_v2_meetings

Finds an existing meeting or creates a new one if it doesn't yet exist. [Please see here](/rest-api/guides/syncing-meetings) for a full guide on syncing meetings to Attio.

This endpoint is in alpha and may be subject to breaking changes as we gather feedback.

Required scopes: `meeting:read-write`, `record_permission:read`.

### Example Usage

<!-- UsageSnippet language="python" operationID="post_/v2/meetings" method="post" path="/v2/meetings" -->
```python
from attio import SDK
from attio.utils import parse_datetime


with SDK(
    oauth2="<YOUR_OAUTH2_HERE>",
) as sdk:

    res = sdk.meetings.post_v2_meetings(data={
        "title": "Onboarding Session",
        "description": "Getting you up to speed with the platform and answering any questions you have.",
        "start": {
            "date_": "2027-11-27",
        },
        "end": {
            "datetime_": parse_datetime("2027-11-27T15:00:00Z"),
            "timezone": "America/New_York",
        },
        "is_all_day": False,
        "participants": [],
        "linked_records": [
            {
                "object": "people",
                "record_id": "891dcbfc-9141-415d-9b2a-2238a6cc012d",
            },
        ],
        "external_ref": "external_meeting_12345",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `data`                                                              | [models.PostV2MeetingsData](../../models/postv2meetingsdata.md)     | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PostV2MeetingsResponse](../../models/postv2meetingsresponse.md)**

### Errors

| Error Type                               | Status Code                              | Content Type                             |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| errors.PostV2MeetingsValidationTypeError | 400                                      | application/json                         |
| errors.SDKDefaultError                   | 4XX, 5XX                                 | \*/\*                                    |

## get_v2_meetings_meeting_id_

Get a single meeting by ID.

This endpoint is in beta. We will aim to avoid breaking changes, but small updates may be made as we roll out to more users.

Required scopes: `meeting:read`, `record_permission:read`.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_/v2/meetings/{meeting_id}" method="get" path="/v2/meetings/{meeting_id}" -->
```python
from attio import SDK


with SDK(
    oauth2="<YOUR_OAUTH2_HERE>",
) as sdk:

    res = sdk.meetings.get_v2_meetings_meeting_id_(meeting_id="cb59ab17-ad15-460c-a126-0715617c0853")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `meeting_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | cb59ab17-ad15-460c-a126-0715617c0853                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetV2MeetingsMeetingIDResponse](../../models/getv2meetingsmeetingidresponse.md)**

### Errors

| Error Type                                 | Status Code                                | Content Type                               |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| errors.GetV2MeetingsMeetingIDNotFoundError | 404                                        | application/json                           |
| errors.SDKDefaultError                     | 4XX, 5XX                                   | \*/\*                                      |