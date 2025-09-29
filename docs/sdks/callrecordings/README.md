# CallRecordings
(*call_recordings*)

## Overview

Call recordings store video, audio, transcript and speaker information for calls. They are linked to meetings.

### Available Operations

* [get_v2_meetings_meeting_id_call_recordings](#get_v2_meetings_meeting_id_call_recordings) - List call recordings
* [get_v2_meetings_meeting_id_call_recordings_call_recording_id_](#get_v2_meetings_meeting_id_call_recordings_call_recording_id_) - Get call recording

## get_v2_meetings_meeting_id_call_recordings

List all call recordings for a meeting.

This endpoint is in beta. We will aim to avoid breaking changes, but small updates may be made as we roll out to more users.

Required scopes: `meeting:read`, `call_recording:read`.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_/v2/meetings/{meeting_id}/call_recordings" method="get" path="/v2/meetings/{meeting_id}/call_recordings" -->
```python
from attio import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as a_client:

    res = a_client.call_recordings.get_v2_meetings_meeting_id_call_recordings(meeting_id="cb59ab17-ad15-460c-a126-0715617c0853", limit=50, cursor="eyJkZXNjcmlwdGlvbiI6ICJ0aGlzIGlzIGEgY3Vyc29yIn0=.eM56CGbqZ6G1NHiJchTIkH4vKDr")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  | Example                                                                      |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `meeting_id`                                                                 | *str*                                                                        | :heavy_check_mark:                                                           | N/A                                                                          | cb59ab17-ad15-460c-a126-0715617c0853                                         |
| `limit`                                                                      | *Optional[int]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          | 50                                                                           |
| `cursor`                                                                     | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          | eyJkZXNjcmlwdGlvbiI6ICJ0aGlzIGlzIGEgY3Vyc29yIn0=.eM56CGbqZ6G1NHiJchTIkH4vKDr |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |                                                                              |

### Response

**[models.GetV2MeetingsMeetingIDCallRecordingsResponse](../../models/getv2meetingsmeetingidcallrecordingsresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.AttioDefaultError | 4XX, 5XX                 | \*/\*                    |

## get_v2_meetings_meeting_id_call_recordings_call_recording_id_

Get a single call recording by ID.

This endpoint is in beta. We will aim to avoid breaking changes, but small updates may be made as we roll out to more users.

Required scopes: `meeting:read`, `call_recording:read`.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_/v2/meetings/{meeting_id}/call_recordings/{call_recording_id}" method="get" path="/v2/meetings/{meeting_id}/call_recordings/{call_recording_id}" -->
```python
from attio import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as a_client:

    res = a_client.call_recordings.get_v2_meetings_meeting_id_call_recordings_call_recording_id_(meeting_id="cb59ab17-ad15-460c-a126-0715617c0853", call_recording_id="e8f2a3b7-9b4d-4c5e-8a1f-3d7b2c5e8f9a")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `meeting_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | cb59ab17-ad15-460c-a126-0715617c0853                                |
| `call_recording_id`                                                 | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | e8f2a3b7-9b4d-4c5e-8a1f-3d7b2c5e8f9a                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetV2MeetingsMeetingIDCallRecordingsCallRecordingIDResponse](../../models/getv2meetingsmeetingidcallrecordingscallrecordingidresponse.md)**

### Errors

| Error Type                                                              | Status Code                                                             | Content Type                                                            |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| errors.GetV2MeetingsMeetingIDCallRecordingsCallRecordingIDNotFoundError | 404                                                                     | application/json                                                        |
| errors.AttioDefaultError                                                | 4XX, 5XX                                                                | \*/\*                                                                   |