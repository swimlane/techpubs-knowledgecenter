# Add Attachment to Table

**Description**: Adds an attachment to a ServiceNow table using the provided file name, table name, and system ID.

## Endpoint

- **URL:** `api/now/attachment/file`
- **Method:** `POST`
## Inputs

- **attachments** (array) – Required: File to be uploaded
  - **file_name** (string) – Required: Name or label.
  - **file** (string) – Required: Text string.
- **parameters** (object): Structured object with nested properties.
  - **encryption_context** (string): Sys_id of an encryption context record. Specify this parameter to allow only users with the specified encryption context to access the attachment.
  - **file_name** (string) – Required: Name or label.
  - **table_name** (string) – Required: Name or label.
  - **table_sys_id** (string) – Required: Sys_id of the record in the table specified in table_name that you want to attach the file to.
- **headers** (object): Structured object with nested properties.
  - **Content-Type** (string) – Required: Type of the resource or value.
## Output

### Example

```json
[
  {
    "status_code": 201,
    "response_headers": {
      "Server-Timing": "sem_wait;dur=0, sesh_wait;dur=0",
      "Content-Encoding": "gzip",
      "X-Is-Logged-In": "true",
      "X-Transaction-ID": "89f9d2509783",
      "Location": "https://dev130168.service-now.com/api/now/attachment/41f9dad09783111084d57e121153af94/file",
      "X-Content-Type-Options": "nosniff",
      "Pragma": "no-store,no-cache",
      "Cache-Control": "no-cache,no-store,must-revalidate,max-age=-1",
      "Expires": "0",
      "Content-Type": "application/json;charset=UTF-8",
      "Transfer-Encoding": "chunked",
      "Date": "Sat, 05 Nov 2022 00:53:43 GMT",
      "Keep-Alive": "timeout=20",
      "Connection": "keep-alive",
      "Server": "ServiceNow",
      "Set-Cookie": "glide_user=; Max-Age=0; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/; HttpOnly; SameSite=None; Secure, glide_user_session=; Max-Age=0; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/; HttpOnly; SameSite=None; Secure, glide_user_route=glide.f6d1c4085a807931391acf9b7192b09e; Max-Age=2147483647; Expires=Thu, 23-Nov-2090 04:07:50 GMT; Path=/; HttpOnly; SameSite=None; Secure, glide_session_store=09F91ADC9743111084D57E121153AFDE; Max-Age=1800; Expires=Sat, 05-Nov-2022 01:23:43 GMT; Path=/; HttpOnly; SameSite=None; Secure",
      "Strict-Transport-Security": "max-age=63072000; includeSubDomains"
    },
    "reason": "Created",
    "json_body": {
      "result": {
        "size_bytes": "5881",
        "file_name": "test",
        "sys_mod_count": "0",
        "average_image_color": "",
        "image_width": "",
        "sys_updated_on": "2022-11-05 00:53:43",
        "sys_tags": "",
        "table_name": "incident",
        "sys_id": "41f9dad09783111084d57e121153af94",
        "image_height": "",
        "sys_updated_by": "admin",
        "download_link": "https://dev130168.service-now.com/api/now/attachment/41f9dad09783111084d57e121153af94/file",
        "content_type": "application/json",
        "sys_created_on": "2022-11-05 00:53:43",
        "size_compressed": "4343",
        "compressed": "true",
        "state": "pending",
        "table_sys_id": "1c741bd70b2322007518478d83673af3",
        "chunk_size_bytes": "700000",
        "hash": "8671fa6613cd1c6e82c0e1d6b940ae0771d1d8b3f56019f8274ed501407ffc2a",
        "sys_created_by": "admin"
      }
    }
  }
]
```
### Output Parameters

- **status_code** (number): Status value or code.
- **reason** (string): Text string.
- **json_body** (object): Structured object with nested properties.
  - **result** (object): Structured object with nested properties.
    - **size_bytes** (string): Size in bytes or appropriate unit.
    - **file_name** (string): Name or label.
    - **sys_mod_count** (string): Number of occurrences or items.
    - **average_image_color** (string): Text string.
    - **image_width** (string): Unique identifier.
    - **sys_updated_on** (string): Timestamp in ISO 8601 format.
    - **sys_tags** (string): Text string.
    - **table_name** (string): Name or label.
    - **sys_id** (string): Unique identifier.
    - **image_height** (string): Text string.
    - **sys_updated_by** (string): Timestamp in ISO 8601 format.
    - **download_link** (string): Text string.
    - **content_type** (string): Type of the resource or value.
    - **sys_created_on** (string): Text string.
    - **size_compressed** (string): Size in bytes or appropriate unit.
    - **compressed** (string): Text string.
    - **state** (string): Text string.
    - **table_sys_id** (string): Unique identifier.
    - **chunk_size_bytes** (string): Size in bytes or appropriate unit.
    - **hash** (string): Hash value for data integrity.
    - **sys_created_by** (string): Text string.
## Response Headers

| Header | Type | Description |
|--------|------|-------------|
| Server-Timing | string | Text string. |
| Content-Encoding | string | Text string. |
| X-Is-Logged-In | string | Text string. |
| X-Transaction-ID | string | Unique identifier. |
| Location | string | Text string. |
| X-Content-Type-Options | string | Type of the resource or value. |
| Pragma | string | Text string. |
| Cache-Control | string | Text string. |
| Expires | string | Text string. |
| Content-Type | string | Type of the resource or value. |
| Transfer-Encoding | string | Text string. |
| Date | string | Timestamp in ISO 8601 format. |
| Keep-Alive | string | Text string. |
| Connection | string | Text string. |
| Server | string | Text string. |
| Set-Cookie | string | Text string. |
| Strict-Transport-Security | string | Text string. |