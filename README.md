# openapi

Developer-friendly & type-safe Python SDK specifically catered to leverage *openapi* API.

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=openapi&utm_campaign=python"><img src="https://www.speakeasy.com/assets/badges/built-by-speakeasy.svg" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


<br /><br />
> [!IMPORTANT]
> This SDK is not yet ready for production use. To complete setup please follow the steps outlined in your [workspace](https://app.speakeasy.com/org/elviskahoro/attio). Delete this section before > publishing to a package manager.

<!-- Start Summary [summary] -->
## Summary


<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [openapi](#openapi)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!TIP]
> To finish publishing your SDK to PyPI you must [run your first generation action](https://www.speakeasy.com/docs/github-setup#step-by-step-guide).


> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add git+<UNSET>.git
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install git+<UNSET>.git
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add git+<UNSET>.git
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from attio python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "attio",
# ]
# ///

from attio import SDK

sdk = SDK(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from attio import SDK


with SDK(
    oauth2="<YOUR_OAUTH2_HERE>",
) as sdk:

    res = sdk.objects.get_v2_objects()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from attio import SDK

async def main():

    async with SDK(
        oauth2="<YOUR_OAUTH2_HERE>",
    ) as sdk:

        res = await sdk.objects.get_v2_objects_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name     | Type   | Scheme       |
| -------- | ------ | ------------ |
| `oauth2` | oauth2 | OAuth2 token |

To authenticate with the API the `oauth2` parameter must be set when initializing the SDK client instance. For example:
```python
from attio import SDK


with SDK(
    oauth2="<YOUR_OAUTH2_HERE>",
) as sdk:

    res = sdk.objects.get_v2_objects()

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [attributes](docs/sdks/attributes/README.md)

* [get_v2_target_identifier_attributes](docs/sdks/attributes/README.md#get_v2_target_identifier_attributes) - List attributes
* [post_v2_target_identifier_attributes](docs/sdks/attributes/README.md#post_v2_target_identifier_attributes) - Create an attribute
* [get_v2_target_identifier_attributes_attribute_](docs/sdks/attributes/README.md#get_v2_target_identifier_attributes_attribute_) - Get an attribute
* [patch_v2_target_identifier_attributes_attribute_](docs/sdks/attributes/README.md#patch_v2_target_identifier_attributes_attribute_) - Update an attribute
* [get_v2_target_identifier_attributes_attribute_options](docs/sdks/attributes/README.md#get_v2_target_identifier_attributes_attribute_options) - List select options
* [post_v2_target_identifier_attributes_attribute_options](docs/sdks/attributes/README.md#post_v2_target_identifier_attributes_attribute_options) - Create a select option
* [patch_v2_target_identifier_attributes_attribute_options_option_](docs/sdks/attributes/README.md#patch_v2_target_identifier_attributes_attribute_options_option_) - Update a select option
* [get_v2_target_identifier_attributes_attribute_statuses](docs/sdks/attributes/README.md#get_v2_target_identifier_attributes_attribute_statuses) - List statuses
* [post_v2_target_identifier_attributes_attribute_statuses](docs/sdks/attributes/README.md#post_v2_target_identifier_attributes_attribute_statuses) - Create a status
* [patch_v2_target_identifier_attributes_attribute_statuses_status_](docs/sdks/attributes/README.md#patch_v2_target_identifier_attributes_attribute_statuses_status_) - Update a status

### [call_recordings](docs/sdks/callrecordings/README.md)

* [get_v2_meetings_meeting_id_call_recordings](docs/sdks/callrecordings/README.md#get_v2_meetings_meeting_id_call_recordings) - List call recordings
* [get_v2_meetings_meeting_id_call_recordings_call_recording_id_](docs/sdks/callrecordings/README.md#get_v2_meetings_meeting_id_call_recordings_call_recording_id_) - Get call recording

### [comments](docs/sdks/comments/README.md)

* [post_v2_comments](docs/sdks/comments/README.md#post_v2_comments) - Create a comment
* [get_v2_comments_comment_id_](docs/sdks/comments/README.md#get_v2_comments_comment_id_) - Get a comment
* [delete_v2_comments_comment_id_](docs/sdks/comments/README.md#delete_v2_comments_comment_id_) - Delete a comment

### [entries](docs/sdks/entries/README.md)

* [post_v2_lists_list_entries_query](docs/sdks/entries/README.md#post_v2_lists_list_entries_query) - List entries
* [post_v2_lists_list_entries](docs/sdks/entries/README.md#post_v2_lists_list_entries) - Create an entry (add record to list)
* [put_v2_lists_list_entries](docs/sdks/entries/README.md#put_v2_lists_list_entries) - Assert a list entry by parent
* [get_v2_lists_list_entries_entry_id_](docs/sdks/entries/README.md#get_v2_lists_list_entries_entry_id_) - Get a list entry
* [patch_v2_lists_list_entries_entry_id_](docs/sdks/entries/README.md#patch_v2_lists_list_entries_entry_id_) - Update a list entry (append multiselect values)
* [put_v2_lists_list_entries_entry_id_](docs/sdks/entries/README.md#put_v2_lists_list_entries_entry_id_) - Update a list entry (overwrite multiselect values)
* [delete_v2_lists_list_entries_entry_id_](docs/sdks/entries/README.md#delete_v2_lists_list_entries_entry_id_) - Delete a list entry
* [get_v2_lists_list_entries_entry_id_attributes_attribute_values](docs/sdks/entries/README.md#get_v2_lists_list_entries_entry_id_attributes_attribute_values) - List attribute values for a list entry

### [lists](docs/sdks/lists/README.md)

* [get_v2_lists](docs/sdks/lists/README.md#get_v2_lists) - List all lists
* [post_v2_lists](docs/sdks/lists/README.md#post_v2_lists) - Create a list
* [get_v2_lists_list_](docs/sdks/lists/README.md#get_v2_lists_list_) - Get a list
* [patch_v2_lists_list_](docs/sdks/lists/README.md#patch_v2_lists_list_) - Update a list

### [meetings](docs/sdks/meetings/README.md)

* [get_v2_meetings](docs/sdks/meetings/README.md#get_v2_meetings) - List meetings
* [get_v2_meetings_meeting_id_](docs/sdks/meetings/README.md#get_v2_meetings_meeting_id_) - Get a meeting

### [meta](docs/sdks/meta/README.md)

* [get_v2_self](docs/sdks/meta/README.md#get_v2_self) - Identify

### [notes](docs/sdks/notes/README.md)

* [get_v2_notes](docs/sdks/notes/README.md#get_v2_notes) - List notes
* [post_v2_notes](docs/sdks/notes/README.md#post_v2_notes) - Create a note
* [get_v2_notes_note_id_](docs/sdks/notes/README.md#get_v2_notes_note_id_) - Get a note
* [delete_v2_notes_note_id_](docs/sdks/notes/README.md#delete_v2_notes_note_id_) - Delete a note

### [objects](docs/sdks/objects/README.md)

* [get_v2_objects](docs/sdks/objects/README.md#get_v2_objects) - List objects
* [post_v2_objects](docs/sdks/objects/README.md#post_v2_objects) - Create an object
* [get_v2_objects_object_](docs/sdks/objects/README.md#get_v2_objects_object_) - Get an object
* [patch_v2_objects_object_](docs/sdks/objects/README.md#patch_v2_objects_object_) - Update an object

### [records](docs/sdks/records/README.md)

* [post_v2_objects_object_records_query](docs/sdks/records/README.md#post_v2_objects_object_records_query) - List records
* [post_v2_objects_object_records](docs/sdks/records/README.md#post_v2_objects_object_records) - Create a record
* [put_v2_objects_object_records](docs/sdks/records/README.md#put_v2_objects_object_records) - Assert a record
* [get_v2_objects_object_records_record_id_](docs/sdks/records/README.md#get_v2_objects_object_records_record_id_) - Get a record
* [patch_v2_objects_object_records_record_id_](docs/sdks/records/README.md#patch_v2_objects_object_records_record_id_) - Update a record (append multiselect values)
* [put_v2_objects_object_records_record_id_](docs/sdks/records/README.md#put_v2_objects_object_records_record_id_) - Update a record (overwrite multiselect values)
* [delete_v2_objects_object_records_record_id_](docs/sdks/records/README.md#delete_v2_objects_object_records_record_id_) - Delete a record
* [get_v2_objects_object_records_record_id_attributes_attribute_values](docs/sdks/records/README.md#get_v2_objects_object_records_record_id_attributes_attribute_values) - List record attribute values
* [get_v2_objects_object_records_record_id_entries](docs/sdks/records/README.md#get_v2_objects_object_records_record_id_entries) - List record entries
* [post_v2_objects_records_search](docs/sdks/records/README.md#post_v2_objects_records_search) - Search records


### [tasks](docs/sdks/tasks/README.md)

* [get_v2_tasks](docs/sdks/tasks/README.md#get_v2_tasks) - List tasks
* [post_v2_tasks](docs/sdks/tasks/README.md#post_v2_tasks) - Create a task
* [get_v2_tasks_task_id_](docs/sdks/tasks/README.md#get_v2_tasks_task_id_) - Get a task
* [patch_v2_tasks_task_id_](docs/sdks/tasks/README.md#patch_v2_tasks_task_id_) - Update a task
* [delete_v2_tasks_task_id_](docs/sdks/tasks/README.md#delete_v2_tasks_task_id_) - Delete a task

### [threads](docs/sdks/threads/README.md)

* [get_v2_threads](docs/sdks/threads/README.md#get_v2_threads) - List threads
* [get_v2_threads_thread_id_](docs/sdks/threads/README.md#get_v2_threads_thread_id_) - Get a thread

### [transcripts](docs/sdks/transcripts/README.md)

* [get_v2_meetings_meeting_id_call_recordings_call_recording_id_transcript](docs/sdks/transcripts/README.md#get_v2_meetings_meeting_id_call_recordings_call_recording_id_transcript) - Get call transcript

### [webhooks](docs/sdks/webhooks/README.md)

* [get_v2_webhooks](docs/sdks/webhooks/README.md#get_v2_webhooks) - List webhooks
* [post_v2_webhooks](docs/sdks/webhooks/README.md#post_v2_webhooks) - Create a webhook
* [get_v2_webhooks_webhook_id_](docs/sdks/webhooks/README.md#get_v2_webhooks_webhook_id_) - Get a webhook
* [patch_v2_webhooks_webhook_id_](docs/sdks/webhooks/README.md#patch_v2_webhooks_webhook_id_) - Update a webhook
* [delete_v2_webhooks_webhook_id_](docs/sdks/webhooks/README.md#delete_v2_webhooks_webhook_id_) - Delete a webhook

### [workspace_members](docs/sdks/workspacemembers/README.md)

* [get_v2_workspace_members](docs/sdks/workspacemembers/README.md#get_v2_workspace_members) - List workspace members
* [get_v2_workspace_members_workspace_member_id_](docs/sdks/workspacemembers/README.md#get_v2_workspace_members_workspace_member_id_) - Get a workspace member

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from attio import SDK
from attio.utils import BackoffStrategy, RetryConfig


with SDK(
    oauth2="<YOUR_OAUTH2_HERE>",
) as sdk:

    res = sdk.objects.get_v2_objects(,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from attio import SDK
from attio.utils import BackoffStrategy, RetryConfig


with SDK(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    oauth2="<YOUR_OAUTH2_HERE>",
) as sdk:

    res = sdk.objects.get_v2_objects()

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`SDKError`](./src/attio/errors/sdkerror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](#error-classes). |

### Example
```python
from attio import SDK, errors


with SDK(
    oauth2="<YOUR_OAUTH2_HERE>",
) as sdk:
    res = None
    try:

        res = sdk.objects.post_v2_objects(data={
            "api_slug": "people",
            "singular_noun": "Person",
            "plural_noun": "People",
        })

        # Handle response
        print(res)


    except errors.SDKError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, errors.PostV2ObjectsSlugConflictError):
            print(e.data.status_code)  # float
            print(e.data.type)  # models.PostV2ObjectsType
            print(e.data.code)  # models.PostV2ObjectsCode
            print(e.data.message)  # str
```

### Error Classes
**Primary error:**
* [`SDKError`](./src/attio/errors/sdkerror.py): The base class for HTTP error responses.

<details><summary>Less common errors (85)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`SDKError`](./src/attio/errors/sdkerror.py)**:
* [`PatchV2ObjectsObjectValidationTypeError`](./src/attio/errors/patchv2objectsobjectvalidationtypeerror.py): Bad Request. Status code `400`. Applicable to 1 of 63 methods.*
* [`PostV2TargetIdentifierAttributesValidationTypeError`](./src/attio/errors/postv2targetidentifierattributesvalidationtypeerror.py): Bad Request. Status code `400`. Applicable to 1 of 63 methods.*
* [`SystemEditUnauthorizedError`](./src/attio/errors/systemeditunauthorizederror.py): Bad Request. Status code `400`. Applicable to 1 of 63 methods.*
* [`PostV2TargetIdentifierAttributesAttributeOptionsValidationTypeError`](./src/attio/errors/postv2targetidentifierattributesattributeoptionsvalidationtypeerror.py): Bad Request. Status code `400`. Applicable to 1 of 63 methods.*
* [`PatchV2TargetIdentifierAttributesAttributeOptionsOptionValueNotFoundError`](./src/attio/errors/patchv2targetidentifierattributesattributeoptionsoptionvaluenotfounderror.py): Bad Request. Status code `400`. Applicable to 1 of 63 methods.*
* [`PostV2TargetIdentifierAttributesAttributeStatusesValidationTypeError`](./src/attio/errors/postv2targetidentifierattributesattributestatusesvalidationtypeerror.py): Bad Request. Status code `400`. Applicable to 1 of 63 methods.*
* [`PatchV2TargetIdentifierAttributesAttributeStatusesStatusValueNotFoundError`](./src/attio/errors/patchv2targetidentifierattributesattributestatusesstatusvaluenotfounderror.py): Bad Request. Status code `400`. Applicable to 1 of 63 methods.*
* [`FilterError`](./src/attio/errors/filtererror.py): Bad Request. Status code `400`. Applicable to 1 of 63 methods.*
* [`PostV2ObjectsObjectRecordsValueNotFoundError`](./src/attio/errors/postv2objectsobjectrecordsvaluenotfounderror.py): Bad Request. Status code `400`. Applicable to 1 of 63 methods.*
* [`PutV2ObjectsObjectRecordsValueNotFoundError`](./src/attio/errors/putv2objectsobjectrecordsvaluenotfounderror.py): Bad Request. Status code `400`. Applicable to 1 of 63 methods.*
* [`PatchV2ObjectsObjectRecordsRecordIDMissingValueError`](./src/attio/errors/patchv2objectsobjectrecordsrecordidmissingvalueerror.py): Bad Request. Status code `400`. Applicable to 1 of 63 methods.*
* [`PutV2ObjectsObjectRecordsRecordIDMissingValueError`](./src/attio/errors/putv2objectsobjectrecordsrecordidmissingvalueerror.py): Bad Request. Status code `400`. Applicable to 1 of 63 methods.*
* [`GetV2ObjectsObjectRecordsRecordIDAttributesAttributeValuesValidationTypeError`](./src/attio/errors/getv2objectsobjectrecordsrecordidattributesattributevaluesvalidationtypeerror.py): Bad Request. Status code `400`. Applicable to 1 of 63 methods.*
* [`PostV2ObjectsRecordsSearchValueNotFoundError`](./src/attio/errors/postv2objectsrecordssearchvaluenotfounderror.py): Bad Request. Status code `400`. Applicable to 1 of 63 methods.*
* [`PostV2ListsValueNotFoundError`](./src/attio/errors/postv2listsvaluenotfounderror.py): Bad Request. Status code `400`. Applicable to 1 of 63 methods.*
* [`PatchV2ListsListValueNotFoundError`](./src/attio/errors/patchv2listslistvaluenotfounderror.py): Bad Request. Status code `400`. Applicable to 1 of 63 methods.*
* [`PostV2ListsListEntriesValueNotFoundError`](./src/attio/errors/postv2listslistentriesvaluenotfounderror.py): Bad Request. Status code `400`. Applicable to 1 of 63 methods.*
* [`MultipleMatchResultsError`](./src/attio/errors/multiplematchresultserror.py): Bad Request. Status code `400`. Applicable to 1 of 63 methods.*
* [`PatchV2ListsListEntriesEntryIDImmutableValueError`](./src/attio/errors/patchv2listslistentriesentryidimmutablevalueerror.py): Bad Request. Status code `400`. Applicable to 1 of 63 methods.*
* [`PutV2ListsListEntriesEntryIDImmutableValueError`](./src/attio/errors/putv2listslistentriesentryidimmutablevalueerror.py): Bad Request. Status code `400`. Applicable to 1 of 63 methods.*
* [`PostV2TasksValidationTypeError`](./src/attio/errors/postv2tasksvalidationtypeerror.py): Bad Request. Status code `400`. Applicable to 1 of 63 methods.*
* [`PatchV2TasksTaskIDValidationTypeError`](./src/attio/errors/patchv2taskstaskidvalidationtypeerror.py): Bad Request. Status code `400`. Applicable to 1 of 63 methods.*
* [`PostV2CommentsValueNotFoundError`](./src/attio/errors/postv2commentsvaluenotfounderror.py): Bad Request. Status code `400`. Applicable to 1 of 63 methods.*
* [`PostV2WebhooksValidationTypeError`](./src/attio/errors/postv2webhooksvalidationtypeerror.py): Bad Request. Status code `400`. Applicable to 1 of 63 methods.*
* [`BillingError`](./src/attio/errors/billingerror.py): Forbidden. Status code `403`. Applicable to 1 of 63 methods.*
* [`GetV2ObjectsObjectNotFoundError`](./src/attio/errors/getv2objectsobjectnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`PatchV2ObjectsObjectNotFoundError`](./src/attio/errors/patchv2objectsobjectnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`PostV2TargetIdentifierAttributesNotFoundError`](./src/attio/errors/postv2targetidentifierattributesnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`GetV2TargetIdentifierAttributesAttributeNotFoundError`](./src/attio/errors/getv2targetidentifierattributesattributenotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`PatchV2TargetIdentifierAttributesAttributeNotFoundError`](./src/attio/errors/patchv2targetidentifierattributesattributenotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`GetV2TargetIdentifierAttributesAttributeOptionsNotFoundError`](./src/attio/errors/getv2targetidentifierattributesattributeoptionsnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`PostV2TargetIdentifierAttributesAttributeOptionsNotFoundError`](./src/attio/errors/postv2targetidentifierattributesattributeoptionsnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`PatchV2TargetIdentifierAttributesAttributeOptionsOptionNotFoundError`](./src/attio/errors/patchv2targetidentifierattributesattributeoptionsoptionnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`GetV2TargetIdentifierAttributesAttributeStatusesNotFoundError`](./src/attio/errors/getv2targetidentifierattributesattributestatusesnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`PostV2TargetIdentifierAttributesAttributeStatusesNotFoundError`](./src/attio/errors/postv2targetidentifierattributesattributestatusesnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`PatchV2TargetIdentifierAttributesAttributeStatusesStatusNotFoundError`](./src/attio/errors/patchv2targetidentifierattributesattributestatusesstatusnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`PostV2ObjectsObjectRecordsQueryNotFoundError`](./src/attio/errors/postv2objectsobjectrecordsquerynotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`PostV2ObjectsObjectRecordsNotFoundError`](./src/attio/errors/postv2objectsobjectrecordsnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`PutV2ObjectsObjectRecordsNotFoundError`](./src/attio/errors/putv2objectsobjectrecordsnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`GetV2ObjectsObjectRecordsRecordIDNotFoundError`](./src/attio/errors/getv2objectsobjectrecordsrecordidnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`PatchV2ObjectsObjectRecordsRecordIDNotFoundError`](./src/attio/errors/patchv2objectsobjectrecordsrecordidnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`PutV2ObjectsObjectRecordsRecordIDNotFoundError`](./src/attio/errors/putv2objectsobjectrecordsrecordidnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`DeleteV2ObjectsObjectRecordsRecordIDNotFoundError`](./src/attio/errors/deletev2objectsobjectrecordsrecordidnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`GetV2ObjectsObjectRecordsRecordIDAttributesAttributeValuesNotFoundError`](./src/attio/errors/getv2objectsobjectrecordsrecordidattributesattributevaluesnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`PostV2ListsNotFoundError`](./src/attio/errors/postv2listsnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`GetV2ListsListNotFoundError`](./src/attio/errors/getv2listslistnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`PatchV2ListsListNotFoundError`](./src/attio/errors/patchv2listslistnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`PostV2ListsListEntriesQueryNotFoundError`](./src/attio/errors/postv2listslistentriesquerynotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`PostV2ListsListEntriesNotFoundError`](./src/attio/errors/postv2listslistentriesnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`PutV2ListsListEntriesNotFoundError`](./src/attio/errors/putv2listslistentriesnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`GetV2ListsListEntriesEntryIDNotFoundError`](./src/attio/errors/getv2listslistentriesentryidnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`PatchV2ListsListEntriesEntryIDNotFoundError`](./src/attio/errors/patchv2listslistentriesentryidnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`PutV2ListsListEntriesEntryIDNotFoundError`](./src/attio/errors/putv2listslistentriesentryidnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`DeleteV2ListsListEntriesEntryIDNotFoundError`](./src/attio/errors/deletev2listslistentriesentryidnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`GetV2ListsListEntriesEntryIDAttributesAttributeValuesNotFoundError`](./src/attio/errors/getv2listslistentriesentryidattributesattributevaluesnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`GetV2WorkspaceMembersWorkspaceMemberIDNotFoundError`](./src/attio/errors/getv2workspacemembersworkspacememberidnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`GetV2NotesNotFoundError`](./src/attio/errors/getv2notesnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`PostV2NotesNotFoundError`](./src/attio/errors/postv2notesnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`GetV2NotesNoteIDNotFoundError`](./src/attio/errors/getv2notesnoteidnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`DeleteV2NotesNoteIDNotFoundError`](./src/attio/errors/deletev2notesnoteidnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`PostV2TasksNotFoundError`](./src/attio/errors/postv2tasksnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`GetV2TasksTaskIDNotFoundError`](./src/attio/errors/getv2taskstaskidnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`PatchV2TasksTaskIDNotFoundError`](./src/attio/errors/patchv2taskstaskidnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`DeleteV2TasksTaskIDNotFoundError`](./src/attio/errors/deletev2taskstaskidnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`GetV2ThreadsThreadIDNotFoundError`](./src/attio/errors/getv2threadsthreadidnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`GetV2CommentsCommentIDNotFoundError`](./src/attio/errors/getv2commentscommentidnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`DeleteV2CommentsCommentIDNotFoundError`](./src/attio/errors/deletev2commentscommentidnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`GetV2MeetingsMeetingIDNotFoundError`](./src/attio/errors/getv2meetingsmeetingidnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`GetV2MeetingsMeetingIDCallRecordingsCallRecordingIDNotFoundError`](./src/attio/errors/getv2meetingsmeetingidcallrecordingscallrecordingidnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`GetV2WebhooksWebhookIDNotFoundError`](./src/attio/errors/getv2webhookswebhookidnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`PatchV2WebhooksWebhookIDNotFoundError`](./src/attio/errors/patchv2webhookswebhookidnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`DeleteV2WebhooksWebhookIDNotFoundError`](./src/attio/errors/deletev2webhookswebhookidnotfounderror.py): Not Found. Status code `404`. Applicable to 1 of 63 methods.*
* [`PostV2ObjectsSlugConflictError`](./src/attio/errors/postv2objectsslugconflicterror.py): Conflict. Status code `409`. Applicable to 1 of 63 methods.*
* [`PatchV2ObjectsObjectSlugConflictError`](./src/attio/errors/patchv2objectsobjectslugconflicterror.py): Conflict. Status code `409`. Applicable to 1 of 63 methods.*
* [`PostV2TargetIdentifierAttributesSlugConflictError`](./src/attio/errors/postv2targetidentifierattributesslugconflicterror.py): Conflict. Status code `409`. Applicable to 1 of 63 methods.*
* [`PostV2TargetIdentifierAttributesAttributeOptionsSlugConflictError`](./src/attio/errors/postv2targetidentifierattributesattributeoptionsslugconflicterror.py): Conflict. Status code `409`. Applicable to 1 of 63 methods.*
* [`PatchV2TargetIdentifierAttributesAttributeOptionsOptionSlugConflictError`](./src/attio/errors/patchv2targetidentifierattributesattributeoptionsoptionslugconflicterror.py): Conflict. Status code `409`. Applicable to 1 of 63 methods.*
* [`PostV2TargetIdentifierAttributesAttributeStatusesSlugConflictError`](./src/attio/errors/postv2targetidentifierattributesattributestatusesslugconflicterror.py): Conflict. Status code `409`. Applicable to 1 of 63 methods.*
* [`PatchV2TargetIdentifierAttributesAttributeStatusesStatusSlugConflictError`](./src/attio/errors/patchv2targetidentifierattributesattributestatusesstatusslugconflicterror.py): Conflict. Status code `409`. Applicable to 1 of 63 methods.*
* [`PostV2ListsSlugConflictError`](./src/attio/errors/postv2listsslugconflicterror.py): Conflict. Status code `409`. Applicable to 1 of 63 methods.*
* [`ResponseValidationError`](./src/attio/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

\* Check [the method documentation](#available-resources-and-operations) to see if the error is applicable.
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from attio import SDK


with SDK(
    server_url="https://api.attio.com",
    oauth2="<YOUR_OAUTH2_HERE>",
) as sdk:

    res = sdk.objects.get_v2_objects()

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from attio import SDK
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = SDK(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from attio import SDK
from attio.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = SDK(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `SDK` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from attio import SDK
def main():

    with SDK(
        oauth2="<YOUR_OAUTH2_HERE>",
    ) as sdk:
        # Rest of application here...


# Or when using async:
async def amain():

    async with SDK(
        oauth2="<YOUR_OAUTH2_HERE>",
    ) as sdk:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from attio import SDK
import logging

logging.basicConfig(level=logging.DEBUG)
s = SDK(debug_logger=logging.getLogger("attio"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=openapi&utm_campaign=python)
