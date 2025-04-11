# Add Attachment to Table

**Description**: Adds an attachment to a ServiceNow table using the provided file name, table name, and system ID.

## Endpoint

- **URL:** `api/now/attachment/file`
- **Method:** `POST`
## Inputs

| Name | Type | Description | Required |
|------|------|-------------|----------|
| attachments | array | File to be uploaded | Yes |
| parameters | object |  | No |
| headers | object |  | No |
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

| Name | Type |
|------|------|
| status_code | number |
| reason | string |
| json_body | object |
## Response Headers

| Header | Type |
|--------|------|
| Server-Timing | string |
| Content-Encoding | string |
| X-Is-Logged-In | string |
| X-Transaction-ID | string |
| Location | string |
| X-Content-Type-Options | string |
| Pragma | string |
| Cache-Control | string |
| Expires | string |
| Content-Type | string |
| Transfer-Encoding | string |
| Date | string |
| Keep-Alive | string |
| Connection | string |
| Server | string |
| Set-Cookie | string |
| Strict-Transport-Security | string |