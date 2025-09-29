# Objects
(*objects*)

## Overview

Objects are the core data models inside of Attio. They contain standard objects, such as [people](/rest-api/endpoint-reference/standard-objects/people/list-person-records), [companies](/rest-api/endpoint-reference/standard-objects/companies/list-company-records) or [deals](/docs/standard-objects-deals), and custom objects that are specific to your use-case. See our [objects and lists guide](/docs/objects-and-lists) for more information.

### Available Operations

* [get_v2_objects](#get_v2_objects) - List objects
* [post_v2_objects](#post_v2_objects) - Create an object
* [get_v2_objects_object_](#get_v2_objects_object_) - Get an object
* [patch_v2_objects_object_](#patch_v2_objects_object_) - Update an object

## get_v2_objects

Lists all system-defined and user-defined objects in your workspace.

Required scopes: `object_configuration:read`.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_/v2/objects" method="get" path="/v2/objects" -->
```python
from attio import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as a_client:

    res = a_client.objects.get_v2_objects()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetV2ObjectsResponse](../../models/getv2objectsresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.AttioDefaultError | 4XX, 5XX                 | \*/\*                    |

## post_v2_objects

Creates a new custom object in your workspace.

Required scopes: `object_configuration:read-write`.

### Example Usage

<!-- UsageSnippet language="python" operationID="post_/v2/objects" method="post" path="/v2/objects" -->
```python
from attio import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as a_client:

    res = a_client.objects.post_v2_objects(data={
        "api_slug": "people",
        "singular_noun": "Person",
        "plural_noun": "People",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `data`                                                              | [models.PostV2ObjectsData](../../models/postv2objectsdata.md)       | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PostV2ObjectsResponse](../../models/postv2objectsresponse.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| errors.PostV2ObjectsSlugConflictError | 409                                   | application/json                      |
| errors.AttioDefaultError              | 4XX, 5XX                              | \*/\*                                 |

## get_v2_objects_object_

Gets a single object by its `object_id` or slug.

Required scopes: `object_configuration:read`.

### Example Usage

<!-- UsageSnippet language="python" operationID="get_/v2/objects/{object}" method="get" path="/v2/objects/{object}" -->
```python
from attio import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as a_client:

    res = a_client.objects.get_v2_objects_object_(object="people")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `object`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | people                                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetV2ObjectsObjectResponse](../../models/getv2objectsobjectresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.GetV2ObjectsObjectNotFoundError | 404                                    | application/json                       |
| errors.AttioDefaultError               | 4XX, 5XX                               | \*/\*                                  |

## patch_v2_objects_object_

Updates a single object. The object to be updated is identified by its `object_id`.

Required scopes: `object_configuration:read-write`.

### Example Usage

<!-- UsageSnippet language="python" operationID="patch_/v2/objects/{object}" method="patch" path="/v2/objects/{object}" -->
```python
from attio import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as a_client:

    res = a_client.objects.patch_v2_objects_object_(object="people", data={
        "api_slug": "people",
        "singular_noun": "Person",
        "plural_noun": "People",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 | Example                                                                     |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `object`                                                                    | *str*                                                                       | :heavy_check_mark:                                                          | N/A                                                                         | people                                                                      |
| `data`                                                                      | [models.PatchV2ObjectsObjectData](../../models/patchv2objectsobjectdata.md) | :heavy_check_mark:                                                          | N/A                                                                         |                                                                             |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |                                                                             |

### Response

**[models.PatchV2ObjectsObjectResponse](../../models/patchv2objectsobjectresponse.md)**

### Errors

| Error Type                                     | Status Code                                    | Content Type                                   |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| errors.PatchV2ObjectsObjectValidationTypeError | 400                                            | application/json                               |
| errors.PatchV2ObjectsObjectNotFoundError       | 404                                            | application/json                               |
| errors.PatchV2ObjectsObjectSlugConflictError   | 409                                            | application/json                               |
| errors.AttioDefaultError                       | 4XX, 5XX                                       | \*/\*                                          |