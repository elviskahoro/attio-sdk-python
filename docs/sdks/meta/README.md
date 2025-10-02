# Meta
(*meta*)

## Overview

Meta endpoints are used to get information about the API token.

### Available Operations

* [get_v2_self](#get_v2_self) - Identify

## get_v2_self

Identify the current access token, the workspace it is linked to, and any permissions it has.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_/v2/self" method="get" path="/v2/self" -->
```python
from attio import SDK


with SDK(
    oauth2="<YOUR_OAUTH2_HERE>",
) as sdk:

    res = sdk.meta.get_v2_self()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetV2SelfResponse](../../models/getv2selfresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |