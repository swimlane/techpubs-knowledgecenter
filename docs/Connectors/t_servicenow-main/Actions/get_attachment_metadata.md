# Get Attachment Metadata

**Description**: Retrieve metadata for attachments in ServiceNow, with the ability to filter results using 'sysparm_query'.

## Endpoint

- **URL:** `api/now/attachment`
- **Method:** `GET`
## Inputs

- **parameters** (object)
  - **sysparm_query** (string) – Required: Encoded query. Queries for the Attachment API are relative to the Attachments [sys_attachment] table.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Server-Timing": "sem_wait;dur=0, sesh_wait;dur=0",
      "Content-Encoding": "gzip",
      "X-Is-Logged-In": "true",
      "X-Transaction-ID": "09ee25ec974f",
      "X-Total-Count": "2",
      "X-Content-Type-Options": "nosniff",
      "Pragma": "no-store,no-cache",
      "Cache-Control": "no-cache,no-store,must-revalidate,max-age=-1",
      "Expires": "0",
      "Content-Type": "application/json;charset=UTF-8",
      "Transfer-Encoding": "chunked",
      "Date": "Sat, 05 Nov 2022 16:24:03 GMT",
      "Keep-Alive": "timeout=20",
      "Connection": "keep-alive",
      "Server": "ServiceNow",
      "Set-Cookie": "glide_user=; Max-Age=0; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/; HttpOnly; SameSite=None; Secure, glide_user_session=; Max-Age=0; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/; HttpOnly; SameSite=None; Secure, glide_user_route=glide.f6d1c4085a807931391acf9b7192b09e; Max-Age=2147483647; Expires=Thu, 23-Nov-2090 19:38:10 GMT; Path=/; HttpOnly; SameSite=None; Secure, glide_session_store=4DEEE160978F111084D57E121153AF4C; Max-Age=1800; Expires=Sat, 05-Nov-2022 16:54:03 GMT; Path=/; HttpOnly; SameSite=None; Secure",
      "Strict-Transport-Security": "max-age=63072000; includeSubDomains"
    },
    "reason": "OK",
    "json_body": {
      "result": [
        {
          "size_bytes": "5881",
          "file_name": "test",
          "sys_mod_count": "1",
          "average_image_color": "",
          "image_width": "",
          "sys_updated_on": "2022-11-05 00:53:44",
          "sys_tags": "",
          "table_name": "incident",
          "sys_id": "41f9dad09783111084d57e121153af94",
          "image_height": "",
          "sys_updated_by": "system",
          "download_link": "https://dev130168.service-now.com/api/now/attachment/41f9dad09783111084d57e121153af94/file",
          "content_type": "application/json",
          "sys_created_on": "2022-11-05 00:53:43",
          "size_compressed": "4343",
          "compressed": "true",
          "state": "available",
          "table_sys_id": "1c741bd70b2322007518478d83673af3",
          "chunk_size_bytes": "700000",
          "hash": "8671fa6613cd1c6e82c0e1d6b940ae0771d1d8b3f56019f8274ed501407ffc2a",
          "sys_created_by": "admin"
        },
        {
          "size_bytes": "5896",
          "file_name": "test",
          "sys_mod_count": "1",
          "average_image_color": "",
          "image_width": "",
          "sys_updated_on": "2022-11-05 00:53:07",
          "sys_tags": "",
          "table_name": "incident",
          "sys_id": "d4d91e549783111084d57e121153afe3",
          "image_height": "",
          "sys_updated_by": "system",
          "download_link": "https://dev130168.service-now.com/api/now/attachment/d4d91e549783111084d57e121153afe3/file",
          "content_type": "application/json",
          "sys_created_on": "2022-11-05 00:53:06",
          "size_compressed": "4358",
          "compressed": "true",
          "state": "available",
          "table_sys_id": "1c741bd70b2322007518478d83673af3",
          "chunk_size_bytes": "700000",
          "hash": "11164d45817f810e70d5f84051523ef0cb12818774fc742d31cfaa158ebe747c",
          "sys_created_by": "admin"
        }
      ]
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **result** (array)
## Response Headers

| Header | Type |
|--------|------|
| Server-Timing | string |
| Content-Encoding | string |
| X-Is-Logged-In | string |
| X-Transaction-ID | string |
| X-Total-Count | string |
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