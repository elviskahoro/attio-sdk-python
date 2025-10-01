# Threads
(*threads*)

## Overview

Threads are groups of [comments](/rest-api/endpoint-reference/comments/get-a-comment) on either a record or entry.

### Available Operations

* [get_v2_threads](#get_v2_threads) - List threads
* [get_v2_threads_thread_id_](#get_v2_threads_thread_id_) - Get a thread

## get_v2_threads

List threads of comments on a record or list entry.

To view threads on records, you will need the `object_configuration:read` and `record_permission:read` scopes.

To view threads on list entries, you will need the `list_configuration:read` and `list_entry:read` scopes.

Required scopes: `comment:read`.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_/v2/threads" method="get" path="/v2/threads" -->
```python
from attio import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as a_client:

    res = a_client.threads.get_v2_threads(record_id="891dcbfc-9141-415d-9b2a-2238a6cc012d", object="people", entry_id="2e6e29ea-c4e0-4f44-842d-78a891f8c156", list_id="33ebdbe9-e529-47c9-b894-0ba25e9c15c0", limit=10, offset=5)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `record_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | 891dcbfc-9141-415d-9b2a-2238a6cc012d                                |
| `object`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | people                                                              |
| `entry_id`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | 2e6e29ea-c4e0-4f44-842d-78a891f8c156                                |
| `list_id`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | 33ebdbe9-e529-47c9-b894-0ba25e9c15c0                                |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | 10                                                                  |
| `offset`                                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | 5                                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetV2ThreadsResponse](../../models/getv2threadsresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.AttioDefaultError | 4XX, 5XX                 | \*/\*                    |

## get_v2_threads_thread_id_

Get all comments in a thread.

To view threads on records, you will need the `object_configuration:read` and `record_permission:read` scopes.

To view threads on list entries, you will need the `list_configuration:read` and `list_entry:read` scopes.

Required scopes: `comment:read`.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_/v2/threads/{thread_id}" method="get" path="/v2/threads/{thread_id}" -->
```python
from attio import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as a_client:

    res = a_client.threads.get_v2_threads_thread_id_(thread_id="a649e4d9-435c-43fb-83ba-847b4876f27a")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `thread_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | a649e4d9-435c-43fb-83ba-847b4876f27a                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetV2ThreadsThreadIDResponse](../../models/getv2threadsthreadidresponse.md)**

### Errors

| Error Type                               | Status Code                              | Content Type                             |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| errors.GetV2ThreadsThreadIDNotFoundError | 404                                      | application/json                         |
| errors.AttioDefaultError                 | 4XX, 5XX                                 | \*/\*                                    |