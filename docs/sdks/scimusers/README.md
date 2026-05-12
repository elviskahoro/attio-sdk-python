# SCIMUsers

## Overview

SCIM users represent workspace members managed through the SCIM provisioning protocol.

### Available Operations

* [get_scim_v2_users](#get_scim_v2_users) - List SCIM users
* [post_scim_v2_users](#post_scim_v2_users) - Create SCIM user
* [get_scim_v2_users_user_id_](#get_scim_v2_users_user_id_) - Get SCIM user
* [patch_scim_v2_users_user_id_](#patch_scim_v2_users_user_id_) - Patch SCIM user
* [put_scim_v2_users_user_id_](#put_scim_v2_users_user_id_) - Update SCIM user
* [delete_scim_v2_users_user_id_](#delete_scim_v2_users_user_id_) - Delete SCIM user

## get_scim_v2_users

Lists SCIM users for the workspace.

Required scopes: `user_management:read`.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_/scim/v2/Users" method="get" path="/scim/v2/Users" -->
```python
from attio import SDK


with SDK(
    oauth2="<YOUR_OAUTH2_HERE>",
) as sdk:

    res = sdk.scim_users.get_scim_v2_users()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetScimV2UsersResponse](../../models/getscimv2usersresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## post_scim_v2_users

Creates a SCIM user in the workspace.

Required scopes: `user_management:read-write`.

### Example Usage

<!-- UsageSnippet language="python" operationID="post_/scim/v2/Users" method="post" path="/scim/v2/Users" -->
```python
from attio import SDK


with SDK(
    oauth2="<YOUR_OAUTH2_HERE>",
) as sdk:

    res = sdk.scim_users.post_scim_v2_users()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PostScimV2UsersResponse](../../models/postscimv2usersresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## get_scim_v2_users_user_id_

Gets a SCIM user by ID.

Required scopes: `user_management:read`.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_/scim/v2/Users/{user_id}" method="get" path="/scim/v2/Users/{user_id}" -->
```python
from attio import SDK


with SDK(
    oauth2="<YOUR_OAUTH2_HERE>",
) as sdk:

    res = sdk.scim_users.get_scim_v2_users_user_id_(user_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The ID of the SCIM user to retrieve.                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetScimV2UsersUserIDResponse](../../models/getscimv2usersuseridresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## patch_scim_v2_users_user_id_

Patches a SCIM user in the workspace.

Required scopes: `user_management:read-write`.

### Example Usage

<!-- UsageSnippet language="python" operationID="patch_/scim/v2/Users/{user_id}" method="patch" path="/scim/v2/Users/{user_id}" -->
```python
from attio import SDK


with SDK(
    oauth2="<YOUR_OAUTH2_HERE>",
) as sdk:

    res = sdk.scim_users.patch_scim_v2_users_user_id_(user_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The ID of the SCIM user to update.                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PatchScimV2UsersUserIDResponse](../../models/patchscimv2usersuseridresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## put_scim_v2_users_user_id_

Updates a SCIM user in the workspace.

Required scopes: `user_management:read-write`.

### Example Usage

<!-- UsageSnippet language="python" operationID="put_/scim/v2/Users/{user_id}" method="put" path="/scim/v2/Users/{user_id}" -->
```python
from attio import SDK


with SDK(
    oauth2="<YOUR_OAUTH2_HERE>",
) as sdk:

    res = sdk.scim_users.put_scim_v2_users_user_id_(user_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The ID of the SCIM user to replace.                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PutScimV2UsersUserIDResponse](../../models/putscimv2usersuseridresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## delete_scim_v2_users_user_id_

Deletes a SCIM user from the workspace.

Required scopes: `user_management:read-write`.

### Example Usage

<!-- UsageSnippet language="python" operationID="delete_/scim/v2/Users/{user_id}" method="delete" path="/scim/v2/Users/{user_id}" -->
```python
from attio import SDK


with SDK(
    oauth2="<YOUR_OAUTH2_HERE>",
) as sdk:

    res = sdk.scim_users.delete_scim_v2_users_user_id_(user_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The ID of the SCIM user to delete.                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteScimV2UsersUserIDResponse](../../models/deletescimv2usersuseridresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |