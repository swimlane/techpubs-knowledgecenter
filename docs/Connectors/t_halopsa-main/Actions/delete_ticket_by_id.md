# Delete Ticket by ID

**Description**: Removes a ticket and its related objects from HaloPSA using the provided unique ID.

## Endpoint

- **URL:** `/api/Tickets/{{id}}`
- **Method:** `DELETE`
## Inputs

- **parameters** (object)
  - **reason** (string): The reason for Ticket's deletion.
- **path_parameters** (object) – Required
  - **id** (string) – Required: The Ticket's ID.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Content-Type": "text/html; charset=utf-8",
      "x-hsci-cache-time": "2024-10-21T12:01:22.328Z",
      "Content-Encoding": "gzip",
      "Expires": "Mon, 21 Oct 2024 12:08:57 GMT",
      "Cache-Control": "max-age=0, no-cache, no-store",
      "Pragma": "no-cache",
      "Date": "Mon, 21 Oct 2024 12:08:57 GMT"
    },
    "reason": "OK",
    "json_body": {}
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
## Response Headers

| Header | Type |
|--------|------|
| Content-Type | string |
| x-hsci-cache-time | string |
| Content-Encoding | string |
| Expires | string |
| Cache-Control | string |
| Pragma | string |
| Date | string |