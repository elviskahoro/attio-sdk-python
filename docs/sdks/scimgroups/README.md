# SCIMGroups

## Overview

SCIM groups represent Attio teams managed through the SCIM provisioning protocol.

### Available Operations

* [get_scim_v2_groups](#get_scim_v2_groups) - List SCIM groups
* [post_scim_v2_groups](#post_scim_v2_groups) - Create SCIM group
* [patch_scim_v2_groups_workspace_team_id_](#patch_scim_v2_groups_workspace_team_id_) - Patch SCIM group

## get_scim_v2_groups

Lists SCIM groups for the workspace.

Required scopes: `scim_management:read`.

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

Required scopes: `scim_management:read-write`.

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

## patch_scim_v2_groups_workspace_team_id_

Patches a SCIM group in the workspace.

Required scopes: `scim_management:read-write`.

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