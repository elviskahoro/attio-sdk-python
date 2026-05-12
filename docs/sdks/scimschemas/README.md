# SCIMSchemas

## Overview

SCIM schemas describe the resource types supported by the SCIM service provider.

### Available Operations

* [get_scim_v2_schemas](#get_scim_v2_schemas) - List SCIM schemas

## get_scim_v2_schemas

Lists the SCIM schemas supported by this service provider.

Required scopes: `user_management:read`.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_/scim/v2/Schemas" method="get" path="/scim/v2/Schemas" -->
```python
from attio import SDK


with SDK(
    oauth2="<YOUR_OAUTH2_HERE>",
) as sdk:

    res = sdk.scim_schemas.get_scim_v2_schemas()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetScimV2SchemasResponse](../../models/getscimv2schemasresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |