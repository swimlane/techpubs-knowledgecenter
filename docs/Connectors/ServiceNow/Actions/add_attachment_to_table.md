# Add Attachment to Table

**Description**: Adds an attachment to a ServiceNow table using the provided file name, table name, and system ID.

## Endpoint

- **URL:** `api/now/attachment/file`
- **Method:** `POST`
## Inputs

- **attachments** (array) – Required: File to be uploaded
  - **file_name** (string) – Required: Auto-generated description for `file_name`. Please update manually if needed.
  - **file** (string) – Required: Auto-generated description for `file`. Please update manually if needed.
- **parameters** (object): Auto-generated description for `parameters`. Please update manually if needed.
  - **encryption_context** (string): Sys_id of an encryption context record. Specify this parameter to allow only users with the specified encryption context to access the attachment.
  - **file_name** (string) – Required: Auto-generated description for `file_name`. Please update manually if needed.
  - **table_name** (string) – Required: Auto-generated description for `table_name`. Please update manually if needed.
  - **table_sys_id** (string) – Required: Sys_id of the record in the table specified in table_name that you want to attach the file to.
- **headers** (object): Auto-generated description for `headers`. Please update manually if needed.
  - **Content-Type** (string) – Required: Auto-generated description for `Content-Type`. Please update manually if needed.
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

- **status_code** (number): Auto-generated description for `status_code`. Please update manually if needed.
- **reason** (string): Auto-generated description for `reason`. Please update manually if needed.
- **json_body** (object): Auto-generated description for `json_body`. Please update manually if needed.
  - **result** (object): Auto-generated description for `result`. Please update manually if needed.
    - **size_bytes** (string): Auto-generated description for `size_bytes`. Please update manually if needed.
    - **file_name** (string): Auto-generated description for `file_name`. Please update manually if needed.
    - **sys_mod_count** (string): Auto-generated description for `sys_mod_count`. Please update manually if needed.
    - **average_image_color** (string): Auto-generated description for `average_image_color`. Please update manually if needed.
    - **image_width** (string): Auto-generated description for `image_width`. Please update manually if needed.
    - **sys_updated_on** (string): Auto-generated description for `sys_updated_on`. Please update manually if needed.
    - **sys_tags** (string): Auto-generated description for `sys_tags`. Please update manually if needed.
    - **table_name** (string): Auto-generated description for `table_name`. Please update manually if needed.
    - **sys_id** (string): Auto-generated description for `sys_id`. Please update manually if needed.
    - **image_height** (string): Auto-generated description for `image_height`. Please update manually if needed.
    - **sys_updated_by** (string): Auto-generated description for `sys_updated_by`. Please update manually if needed.
    - **download_link** (string): Auto-generated description for `download_link`. Please update manually if needed.
    - **content_type** (string): Auto-generated description for `content_type`. Please update manually if needed.
    - **sys_created_on** (string): Auto-generated description for `sys_created_on`. Please update manually if needed.
    - **size_compressed** (string): Auto-generated description for `size_compressed`. Please update manually if needed.
    - **compressed** (string): Auto-generated description for `compressed`. Please update manually if needed.
    - **state** (string): Auto-generated description for `state`. Please update manually if needed.
    - **table_sys_id** (string): Auto-generated description for `table_sys_id`. Please update manually if needed.
    - **chunk_size_bytes** (string): Auto-generated description for `chunk_size_bytes`. Please update manually if needed.
    - **hash** (string): Auto-generated description for `hash`. Please update manually if needed.
    - **sys_created_by** (string): Auto-generated description for `sys_created_by`. Please update manually if needed.
## Response Headers

| Header | Type | Description |
|--------|------|-------------|
| Server-Timing | string | Auto-generated description for `Server-Timing`. Please update manually if needed. |
| Content-Encoding | string | Auto-generated description for `Content-Encoding`. Please update manually if needed. |
| X-Is-Logged-In | string | Auto-generated description for `X-Is-Logged-In`. Please update manually if needed. |
| X-Transaction-ID | string | Auto-generated description for `X-Transaction-ID`. Please update manually if needed. |
| Location | string | Auto-generated description for `Location`. Please update manually if needed. |
| X-Content-Type-Options | string | Auto-generated description for `X-Content-Type-Options`. Please update manually if needed. |
| Pragma | string | Auto-generated description for `Pragma`. Please update manually if needed. |
| Cache-Control | string | Auto-generated description for `Cache-Control`. Please update manually if needed. |
| Expires | string | Auto-generated description for `Expires`. Please update manually if needed. |
| Content-Type | string | Auto-generated description for `Content-Type`. Please update manually if needed. |
| Transfer-Encoding | string | Auto-generated description for `Transfer-Encoding`. Please update manually if needed. |
| Date | string | Auto-generated description for `Date`. Please update manually if needed. |
| Keep-Alive | string | Auto-generated description for `Keep-Alive`. Please update manually if needed. |
| Connection | string | Auto-generated description for `Connection`. Please update manually if needed. |
| Server | string | Auto-generated description for `Server`. Please update manually if needed. |
| Set-Cookie | string | Auto-generated description for `Set-Cookie`. Please update manually if needed. |
| Strict-Transport-Security | string | Auto-generated description for `Strict-Transport-Security`. Please update manually if needed. |