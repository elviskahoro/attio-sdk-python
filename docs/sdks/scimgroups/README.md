# SCIMGroups

## Overview

SCIM groups represent Attio teams managed through the SCIM provisioning protocol.

### Available Operations

* [get_scim_v2_groups](#get_scim_v2_groups) - List SCIM groups
* [post_scim_v2_groups](#post_scim_v2_groups) - Create SCIM group
* [get_scim_v2_groups_workspace_team_id_](#get_scim_v2_groups_workspace_team_id_) - Get SCIM group
* [patch_scim_v2_groups_workspace_team_id_](#patch_scim_v2_groups_workspace_team_id_) - Patch SCIM group
* [put_scim_v2_groups_workspace_team_id_](#put_scim_v2_groups_workspace_team_id_) - Update SCIM group
* [delete_scim_v2_groups_workspace_team_id_](#delete_scim_v2_groups_workspace_team_id_) - Delete SCIM group

## get_scim_v2_groups

Lists SCIM groups for the workspace.

Required scopes: `user_management:read`.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_/scim/v2/Groups" method="get" path="/scim/v2/Groups" -->
```python
from attio import SDK


with SDK(
    oauth2="<YOUR_OAUTH2_HERE>",
) as sdk:

    res = sdk.scim_groups.get_scim_v2_groups()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetScimV2GroupsResponse](../../models/getscimv2groupsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## post_scim_v2_groups

Creates a SCIM group for the workspace.

Required scopes: `user_management:read-write`.

### Example Usage

<!-- UsageSnippet language="python" operationID="post_/scim/v2/Groups" method="post" path="/scim/v2/Groups" -->
```python
from attio import SDK


with SDK(
    oauth2="<YOUR_OAUTH2_HERE>",
) as sdk:

    res = sdk.scim_groups.post_scim_v2_groups()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PostScimV2GroupsResponse](../../models/postscimv2groupsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## get_scim_v2_groups_workspace_team_id_

Gets a SCIM group by ID.

Required scopes: `user_management:read`.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_/scim/v2/Groups/{workspace_team_id}" method="get" path="/scim/v2/Groups/{workspace_team_id}" -->
```python
from attio import SDK


with SDK(
    oauth2="<YOUR_OAUTH2_HERE>",
) as sdk:

    res = sdk.scim_groups.get_scim_v2_groups_workspace_team_id_(workspace_team_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workspace_team_id`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The ID of the SCIM group to retrieve.                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetScimV2GroupsWorkspaceTeamIDResponse](../../models/getscimv2groupsworkspaceteamidresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## patch_scim_v2_groups_workspace_team_id_

Patches a SCIM group in the workspace.

Required scopes: `user_management:read-write`.

### Example Usage

<!-- UsageSnippet language="python" operationID="patch_/scim/v2/Groups/{workspace_team_id}" method="patch" path="/scim/v2/Groups/{workspace_team_id}" -->
```python
from attio import SDK


with SDK(
    oauth2="<YOUR_OAUTH2_HERE>",
) as sdk:

    res = sdk.scim_groups.patch_scim_v2_groups_workspace_team_id_(workspace_team_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workspace_team_id`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The ID of the SCIM group to update.                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PatchScimV2GroupsWorkspaceTeamIDResponse](../../models/patchscimv2groupsworkspaceteamidresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## put_scim_v2_groups_workspace_team_id_

Updates a SCIM group in the workspace.

Required scopes: `user_management:read-write`.

### Example Usage

<!-- UsageSnippet language="python" operationID="put_/scim/v2/Groups/{workspace_team_id}" method="put" path="/scim/v2/Groups/{workspace_team_id}" -->
```python
from attio import SDK


with SDK(
    oauth2="<YOUR_OAUTH2_HERE>",
) as sdk:

    res = sdk.scim_groups.put_scim_v2_groups_workspace_team_id_(workspace_team_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workspace_team_id`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The ID of the SCIM group to replace.                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PutScimV2GroupsWorkspaceTeamIDResponse](../../models/putscimv2groupsworkspaceteamidresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## delete_scim_v2_groups_workspace_team_id_

Deletes a SCIM group from the workspace.

Required scopes: `user_management:read-write`.

### Example Usage

<!-- UsageSnippet language="python" operationID="delete_/scim/v2/Groups/{workspace_team_id}" method="delete" path="/scim/v2/Groups/{workspace_team_id}" -->
```python
from attio import SDK


with SDK(
    oauth2="<YOUR_OAUTH2_HERE>",
) as sdk:

    res = sdk.scim_groups.delete_scim_v2_groups_workspace_team_id_(workspace_team_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workspace_team_id`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The ID of the SCIM group to delete.                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteScimV2GroupsWorkspaceTeamIDResponse](../../models/deletescimv2groupsworkspaceteamidresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |