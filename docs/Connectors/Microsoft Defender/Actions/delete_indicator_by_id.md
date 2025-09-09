# Delete Indicator by ID

**Description**: Removes a specified security indicator from Microsoft Defender using the unique ID.

## Endpoint

- **URL:** `/api/indicators/{{id}}`
- **Method:** `DELETE`
## Inputs

- **path_parameters** (object) – Required
  - **id** (string) – Required
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Thu, 30 May 2024 10:21:38 GMT",
      "Content-Length": "0",
      "Connection": "keep-alive",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains"
    },
    "reason": "OK",
    "response_text": ""
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **response_text** (string)
## Response Headers

| Header | Type |
|--------|------|
| Date | string |
| Content-Length | string |
| Connection | string |
| Strict-Transport-Security | string |