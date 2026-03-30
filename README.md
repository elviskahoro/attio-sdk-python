# Attio Python SDK

<div align="left">
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


<br /><br />

Type-safe Python client for the [Attio API](https://developers.attio.com/), with support for sync and async usage.

<!-- Start Summary [summary] -->
## Summary

- Install in seconds with `pip install attio`.
- Authenticate with your OAuth2 bearer token.
- Use one SDK for both sync and async requests.
- Start with quick examples, then use the full operation docs linked below.

<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [Attio Python SDK](#attio-python-sdk)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication)
  * [Common Workflows](#common-workflows)
  * [Full API Reference](#full-api-reference)
  * [File uploads](#file-uploads)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
  * [Troubleshooting](#troubleshooting)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

The easiest way to install the SDK is:

```bash
pip install attio
```

You can also install with `uv` or `poetry`:

```bash
uv add attio
poetry add attio
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and `uvx`:

```shell
uvx --from attio python
```

Or as a standalone script without creating a project:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "attio",
# ]
# ///

from attio import SDK

sdk = SDK(
    oauth2="<YOUR_OAUTH2_HERE>",
)

# Rest of script here...
```

Run it with:

```bash
uv run script.py
```
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

The SDK ships with typed request/response models and works well with common Python tooling (`pyright`, `mypy`, Pylance, PyCharm).
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Quickstart (sync)

```python
from attio import SDK

with SDK(
    oauth2="<YOUR_OAUTH2_HERE>",
) as sdk:
    # Verify auth and token scopes
    identity = sdk.meta.get_v2_self()
    print(identity)

    # First API call: list objects in your workspace
    objects = sdk.objects.get_v2_objects()
    print(objects)
```

### Quickstart (async)

```python
import asyncio
from attio import SDK


async def main():

    async with SDK(
        oauth2="<YOUR_OAUTH2_HERE>",
    ) as sdk:
        identity = await sdk.meta.get_v2_self_async()
        print(identity)

        objects = await sdk.objects.get_v2_objects_async()
        print(objects)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

This SDK supports the following security scheme globally:

| Name     | Type   | Scheme       |
| -------- | ------ | ------------ |
| `oauth2` | oauth2 | OAuth2 token |

Pass your OAuth2 bearer token when creating the client:
```python
from attio import SDK


with SDK(
    oauth2="<YOUR_OAUTH2_HERE>",
) as sdk:
    res = sdk.meta.get_v2_self()
    print(res)
```

Using an environment variable is recommended:

```python
import os
from attio import SDK

with SDK(oauth2=os.environ["ATTIO_OAUTH2_TOKEN"]) as sdk:
    res = sdk.meta.get_v2_self()
    print(res)
```
<!-- End Authentication [security] -->

## Common Workflows

### List objects

```python
from attio import SDK

with SDK(oauth2="<YOUR_OAUTH2_HERE>") as sdk:
    res = sdk.objects.get_v2_objects()
    print(res)
```

### Create a record (people)

```python
from attio import SDK

with SDK(oauth2="<YOUR_OAUTH2_HERE>") as sdk:
    res = sdk.records.post_v2_objects_object_records(
        object="people",
        data={
            "values": {
                "<ATTRIBUTE_SLUG_OR_ID>": ["Ada Lovelace"],
            },
        },
    )
    print(res)
```

### Query records (people)

```python
from attio import SDK

with SDK(oauth2="<YOUR_OAUTH2_HERE>") as sdk:
    res = sdk.records.post_v2_objects_object_records_query(
        object="people",
        limit=25,
        offset=0,
    )
    print(res)
```

<!-- Start Available Resources and Operations [operations] -->
## Full API Reference

<details open>
<summary>Available resources and methods</summary>

### [Attributes](docs/sdks/attributes/README.md)

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

### [CallRecordings](docs/sdks/callrecordings/README.md)

* [get_v2_meetings_meeting_id_call_recordings](docs/sdks/callrecordings/README.md#get_v2_meetings_meeting_id_call_recordings) - List call recordings
* [post_v2_meetings_meeting_id_call_recordings](docs/sdks/callrecordings/README.md#post_v2_meetings_meeting_id_call_recordings) - Create call recording
* [get_v2_meetings_meeting_id_call_recordings_call_recording_id_](docs/sdks/callrecordings/README.md#get_v2_meetings_meeting_id_call_recordings_call_recording_id_) - Get call recording
* [delete_v2_meetings_meeting_id_call_recordings_call_recording_id_](docs/sdks/callrecordings/README.md#delete_v2_meetings_meeting_id_call_recordings_call_recording_id_) - Delete call recording

### [Comments](docs/sdks/comments/README.md)

* [post_v2_comments](docs/sdks/comments/README.md#post_v2_comments) - Create a comment
* [get_v2_comments_comment_id_](docs/sdks/comments/README.md#get_v2_comments_comment_id_) - Get a comment
* [delete_v2_comments_comment_id_](docs/sdks/comments/README.md#delete_v2_comments_comment_id_) - Delete a comment

### [Entries](docs/sdks/entries/README.md)

* [post_v2_lists_list_entries_query](docs/sdks/entries/README.md#post_v2_lists_list_entries_query) - List entries
* [post_v2_lists_list_entries](docs/sdks/entries/README.md#post_v2_lists_list_entries) - Create an entry (add record to list)
* [put_v2_lists_list_entries](docs/sdks/entries/README.md#put_v2_lists_list_entries) - Assert a list entry by parent
* [get_v2_lists_list_entries_entry_id_](docs/sdks/entries/README.md#get_v2_lists_list_entries_entry_id_) - Get a list entry
* [patch_v2_lists_list_entries_entry_id_](docs/sdks/entries/README.md#patch_v2_lists_list_entries_entry_id_) - Update a list entry (append multiselect values)
* [put_v2_lists_list_entries_entry_id_](docs/sdks/entries/README.md#put_v2_lists_list_entries_entry_id_) - Update a list entry (overwrite multiselect values)
* [delete_v2_lists_list_entries_entry_id_](docs/sdks/entries/README.md#delete_v2_lists_list_entries_entry_id_) - Delete a list entry
* [get_v2_lists_list_entries_entry_id_attributes_attribute_values](docs/sdks/entries/README.md#get_v2_lists_list_entries_entry_id_attributes_attribute_values) - List attribute values for a list entry

### [Files](docs/sdks/files/README.md)

* [get_v2_files](docs/sdks/files/README.md#get_v2_files) - List files
* [post_v2_files](docs/sdks/files/README.md#post_v2_files) - Create a folder
* [post_v2_files_upload](docs/sdks/files/README.md#post_v2_files_upload) - Upload a file
* [get_v2_files_file_id_](docs/sdks/files/README.md#get_v2_files_file_id_) - Get a file
* [delete_v2_files_file_id_](docs/sdks/files/README.md#delete_v2_files_file_id_) - Delete a file
* [get_v2_files_file_id_download](docs/sdks/files/README.md#get_v2_files_file_id_download) - Download a file

### [Lists](docs/sdks/lists/README.md)

* [get_v2_lists](docs/sdks/lists/README.md#get_v2_lists) - List all lists
* [post_v2_lists](docs/sdks/lists/README.md#post_v2_lists) - Create a list
* [get_v2_lists_list_](docs/sdks/lists/README.md#get_v2_lists_list_) - Get a list
* [patch_v2_lists_list_](docs/sdks/lists/README.md#patch_v2_lists_list_) - Update a list
* [get_v2_lists_list_views](docs/sdks/lists/README.md#get_v2_lists_list_views) - List views for list

### [Meetings](docs/sdks/meetings/README.md)

* [get_v2_meetings](docs/sdks/meetings/README.md#get_v2_meetings) - List meetings
* [post_v2_meetings](docs/sdks/meetings/README.md#post_v2_meetings) - Find or create a meeting
* [get_v2_meetings_meeting_id_](docs/sdks/meetings/README.md#get_v2_meetings_meeting_id_) - Get a meeting

### [Meta](docs/sdks/metasdk/README.md)

* [get_v2_self](docs/sdks/metasdk/README.md#get_v2_self) - Identify

### [Notes](docs/sdks/notes/README.md)

* [get_v2_notes](docs/sdks/notes/README.md#get_v2_notes) - List notes
* [post_v2_notes](docs/sdks/notes/README.md#post_v2_notes) - Create a note
* [get_v2_notes_note_id_](docs/sdks/notes/README.md#get_v2_notes_note_id_) - Get a note
* [delete_v2_notes_note_id_](docs/sdks/notes/README.md#delete_v2_notes_note_id_) - Delete a note

### [Objects](docs/sdks/objects/README.md)

* [get_v2_objects](docs/sdks/objects/README.md#get_v2_objects) - List objects
* [post_v2_objects](docs/sdks/objects/README.md#post_v2_objects) - Create an object
* [get_v2_objects_object_](docs/sdks/objects/README.md#get_v2_objects_object_) - Get an object
* [patch_v2_objects_object_](docs/sdks/objects/README.md#patch_v2_objects_object_) - Update an object
* [get_v2_objects_object_views](docs/sdks/objects/README.md#get_v2_objects_object_views) - List views for object

### [Records](docs/sdks/records/README.md)

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

### [SCIMGroups](docs/sdks/scimgroups/README.md)

* [get_scim_v2_groups](docs/sdks/scimgroups/README.md#get_scim_v2_groups) - List SCIM groups
* [post_scim_v2_groups](docs/sdks/scimgroups/README.md#post_scim_v2_groups) - Create SCIM group
* [patch_scim_v2_groups_workspace_team_id_](docs/sdks/scimgroups/README.md#patch_scim_v2_groups_workspace_team_id_) - Patch SCIM group

### [SCIMSchemas](docs/sdks/scimschemas/README.md)

* [get_scim_v2_schemas](docs/sdks/scimschemas/README.md#get_scim_v2_schemas) - List SCIM schemas

### [SCIMUsers](docs/sdks/scimusers/README.md)

* [get_scim_v2_users](docs/sdks/scimusers/README.md#get_scim_v2_users) - List SCIM users
* [post_scim_v2_users](docs/sdks/scimusers/README.md#post_scim_v2_users) - Create SCIM user
* [patch_scim_v2_users_user_id_](docs/sdks/scimusers/README.md#patch_scim_v2_users_user_id_) - Patch SCIM user
* [put_scim_v2_users_user_id_](docs/sdks/scimusers/README.md#put_scim_v2_users_user_id_) - Update SCIM user

### [Tasks](docs/sdks/tasks/README.md)

* [get_v2_tasks](docs/sdks/tasks/README.md#get_v2_tasks) - List tasks
* [post_v2_tasks](docs/sdks/tasks/README.md#post_v2_tasks) - Create a task
* [get_v2_tasks_task_id_](docs/sdks/tasks/README.md#get_v2_tasks_task_id_) - Get a task
* [patch_v2_tasks_task_id_](docs/sdks/tasks/README.md#patch_v2_tasks_task_id_) - Update a task
* [delete_v2_tasks_task_id_](docs/sdks/tasks/README.md#delete_v2_tasks_task_id_) - Delete a task

### [Threads](docs/sdks/threads/README.md)

* [get_v2_threads](docs/sdks/threads/README.md#get_v2_threads) - List threads
* [get_v2_threads_thread_id_](docs/sdks/threads/README.md#get_v2_threads_thread_id_) - Get a thread

### [Transcripts](docs/sdks/transcripts/README.md)

* [get_v2_meetings_meeting_id_call_recordings_call_recording_id_transcript](docs/sdks/transcripts/README.md#get_v2_meetings_meeting_id_call_recordings_call_recording_id_transcript) - Get call transcript

### [Webhooks](docs/sdks/webhooks/README.md)

* [get_v2_webhooks](docs/sdks/webhooks/README.md#get_v2_webhooks) - List webhooks
* [post_v2_webhooks](docs/sdks/webhooks/README.md#post_v2_webhooks) - Create a webhook
* [get_v2_webhooks_webhook_id_](docs/sdks/webhooks/README.md#get_v2_webhooks_webhook_id_) - Get a webhook
* [patch_v2_webhooks_webhook_id_](docs/sdks/webhooks/README.md#patch_v2_webhooks_webhook_id_) - Update a webhook
* [delete_v2_webhooks_webhook_id_](docs/sdks/webhooks/README.md#delete_v2_webhooks_webhook_id_) - Delete a webhook

### [WorkspaceMembers](docs/sdks/workspacemembers/README.md)

* [get_v2_workspace_members](docs/sdks/workspacemembers/README.md#get_v2_workspace_members) - List workspace members
* [get_v2_workspace_members_workspace_member_id_](docs/sdks/workspacemembers/README.md#get_v2_workspace_members_workspace_member_id_) - Get a workspace member

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start File uploads [file-upload] -->
## File uploads

Use file streams for uploads to avoid loading large files fully into memory.

```python
from attio import SDK

with SDK(
    oauth2="<YOUR_OAUTH2_HERE>",
) as sdk:
    with open("example.file", "rb") as f:
        res = sdk.files.post_v2_files_upload(
            file={"file_name": "example.file", "content": f},
            object="people",
            record_id="bf071e1f-6035-429d-b874-d83ea64ea13b",
            parent_folder_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )
        print(res)
```
<!-- End File uploads [file-upload] -->

<!-- Start Retries [retries] -->
## Retries

You can configure retries per request or globally for the entire SDK.

Per request:
```python
from attio import SDK
from attio.utils import BackoffStrategy, RetryConfig


with SDK(
    oauth2="<YOUR_OAUTH2_HERE>",
) as sdk:
    res = sdk.objects.get_v2_objects(
        retries=RetryConfig(
            "backoff",
            BackoffStrategy(1, 50, 1.1, 100),
            False,
        )
    )
    print(res)
```

Global default:

```python
from attio import SDK
from attio.utils import BackoffStrategy, RetryConfig


with SDK(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    oauth2="<YOUR_OAUTH2_HERE>",
) as sdk:
    res = sdk.objects.get_v2_objects()
    print(res)
```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

The SDK raises `errors.SDKError` for API-level failures (4XX/5XX). Catch this type for most cases.

```python
from attio import SDK, errors

with SDK(oauth2="<YOUR_OAUTH2_HERE>") as sdk:
    try:
        res = sdk.objects.get_v2_objects()
        print(res)
    except errors.SDKError as err:
        print(err.status_code)
        print(err.message)
        print(err.body)
```

When needed, handle specific typed errors for an operation (for example conflict/not-found errors). See each operation page in [Full API Reference](#full-api-reference) for its exact error types.
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

Override the default API base URL per client:
```python
from attio import SDK

with SDK(
    server_url="https://api.attio.com",
    oauth2="<YOUR_OAUTH2_HERE>",
) as sdk:
    res = sdk.objects.get_v2_objects()
    print(res)
```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The SDK uses [httpx](https://www.python-httpx.org/) under the hood. You can pass your own configured client to control timeouts, headers, proxies, or transport behavior.

Sync example:
```python
from attio import SDK
import httpx

client = httpx.Client(
    timeout=20.0,
    headers={"x-custom-header": "some-value"},
)

sdk = SDK(
    oauth2="<YOUR_OAUTH2_HERE>",
    client=client,
)
```

Async example:

```python
from attio import SDK
import httpx

async_client = httpx.AsyncClient(timeout=20.0)
sdk = SDK(
    oauth2="<YOUR_OAUTH2_HERE>",
    async_client=async_client,
)
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

## Troubleshooting

### 401 or 403 responses

- Confirm the OAuth2 token is valid and not expired.
- Confirm the token includes the scopes required by the endpoint (scope requirements are listed in each operation doc).
- Verify you are sending the token through `SDK(oauth2=...)`.

### Validation errors on create/update

- Attribute keys and value shapes must match your Attio workspace schema.
- Check the operation docs for the exact request model and examples.
- Start from a simple payload, then add fields incrementally.

### Async usage issues

- Use async methods (ending in `_async`) inside `async with SDK(...)`.
- Do not mix sync and async clients in the same call path.

<!-- Placeholder for Future Speakeasy SDK Sections -->
