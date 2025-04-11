# Get Attachment Metadata

**Description**: Retrieve metadata for attachments in ServiceNow, with the ability to filter results using 'sysparm_query'.

## Endpoint

- **URL:** `api/now/attachment`
- **Method:** `GET`
## Inputs

| Name | Type | Description | Required |
|------|------|-------------|----------|
| parameters | object |  | No |
## Output

### Example

```json
- json_body:
    result:
    - average_image_color: ''
      chunk_size_bytes: '700000'
      compressed: 'true'
      content_type: application/json
      download_link: https://dev130168.service-now.com/api/now/attachment/41f9dad09783111084d57e121153af94/file
      file_name: test
      hash: 8671fa6613cd1c6e82c0e1d6b940ae0771d1d8b3f56019f8274ed501407ffc2a
      image_height: ''
      image_width: ''
      size_bytes: '5881'
      size_compressed: '4343'
      state: available
      sys_created_by: admin
      sys_created_on: '2022-11-05 00:53:43'
      sys_id: 41f9dad09783111084d57e121153af94
      sys_mod_count: '1'
      sys_tags: ''
      sys_updated_by: system
      sys_updated_on: '2022-11-05 00:53:44'
      table_name: incident
      table_sys_id: 1c741bd70b2322007518478d83673af3
    - average_image_color: ''
      chunk_size_bytes: '700000'
      compressed: 'true'
      content_type: application/json
      download_link: https://dev130168.service-now.com/api/now/attachment/d4d91e549783111084d57e121153afe3/file
      file_name: test
      hash: 11164d45817f810e70d5f84051523ef0cb12818774fc742d31cfaa158ebe747c
      image_height: ''
      image_width: ''
      size_bytes: '5896'
      size_compressed: '4358'
      state: available
      sys_created_by: admin
      sys_created_on: '2022-11-05 00:53:06'
      sys_id: d4d91e549783111084d57e121153afe3
      sys_mod_count: '1'
      sys_tags: ''
      sys_updated_by: system
      sys_updated_on: '2022-11-05 00:53:07'
      table_name: incident
      table_sys_id: 1c741bd70b2322007518478d83673af3
  reason: OK
  response_headers:
    Cache-Control: no-cache,no-store,must-revalidate,max-age=-1
    Connection: keep-alive
    Content-Encoding: gzip
    Content-Type: application/json;charset=UTF-8
    Date: Sat, 05 Nov 2022 16:24:03 GMT
    Expires: '0'
    Keep-Alive: timeout=20
    Pragma: no-store,no-cache
    Server: ServiceNow
    Server-Timing: sem_wait;dur=0, sesh_wait;dur=0
    Set-Cookie: glide_user=; Max-Age=0; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/;
      HttpOnly; SameSite=None; Secure, glide_user_session=; Max-Age=0; Expires=Thu,
      01-Jan-1970 00:00:10 GMT; Path=/; HttpOnly; SameSite=None; Secure, glide_user_route=glide.f6d1c4085a807931391acf9b7192b09e;
      Max-Age=2147483647; Expires=Thu, 23-Nov-2090 19:38:10 GMT; Path=/; HttpOnly;
      SameSite=None; Secure, glide_session_store=4DEEE160978F111084D57E121153AF4C;
      Max-Age=1800; Expires=Sat, 05-Nov-2022 16:54:03 GMT; Path=/; HttpOnly; SameSite=None;
      Secure
    Strict-Transport-Security: max-age=63072000; includeSubDomains
    Transfer-Encoding: chunked
    X-Content-Type-Options: nosniff
    X-Is-Logged-In: 'true'
    X-Total-Count: '2'
    X-Transaction-ID: 09ee25ec974f
  status_code: 200

```
### Output Parameters

| Name | Type | Description |
|------|------|-------------|
| status_code | number |  |
| reason | string |  |
| json_body | object |  |
## Response Headers

| Header | Type | Description |
|--------|------|-------------|
| Server-Timing | string |  |
| Content-Encoding | string |  |
| X-Is-Logged-In | string |  |
| X-Transaction-ID | string |  |
| X-Total-Count | string |  |
| X-Content-Type-Options | string |  |
| Pragma | string |  |
| Cache-Control | string |  |
| Expires | string |  |
| Content-Type | string |  |
| Transfer-Encoding | string |  |
| Date | string |  |
| Keep-Alive | string |  |
| Connection | string |  |
| Server | string |  |
| Set-Cookie | string |  |
| Strict-Transport-Security | string |  |
## Error Handling

### Common Error Responses

| Status Code | Message | Description | Example |
|-------------|---------|-------------|---------|
| 400 | Bad Request | The request was invalid or cannot be processed. | Invalid search ID or parameters. |
| 401 | Unauthorized | Missing or incorrect authentication. | Invalid API token. |
| 403 | Forbidden | Access to the resource is denied. | No permissions for search. |
| 404 | Not Found | The requested item does not exist. | Search ID not found. |
| 500 | Internal Server Error | A server error occurred. | Unexpected failure in Splunk. |

### Error Example

```json
{
  "messages": [
    {
      "type": "ERROR",
      "text": "Search ID not found."
    }
  ],
  "status_code": 404,
  "reason": "Not Found"
}
```