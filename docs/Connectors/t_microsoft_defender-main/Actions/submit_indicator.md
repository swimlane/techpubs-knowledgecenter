# Submit Indicator

**Description**: Enhance tracking, alerting, and threat detection by submitting a new indicator to Microsoft Defender.

## Endpoint

- **URL:** `/api/indicators`
- **Method:** `POST`
## Inputs

- **json_body** (object)
  - **indicatorValue** (string)
  - **indicatorType** (string)
  - **action** (string)
  - **title** (string)
  - **expirationTime** (string)
  - **severity** (string)
  - **description** (string)
  - **recommendedActions** (string)
## Output

### Example

```json
[
  {
    "status_code": 405,
    "response_headers": {
      "Date": "Thu, 04 May 2023 18:07:32 GMT",
      "Content-Length": "0",
      "Connection": "keep-alive",
      "Allow": "POST",
      "Strict-Transport-Security": "max-age=15724800; includeSubDomains"
    },
    "reason": "Method Not Allowed",
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
| Allow | string |
| Strict-Transport-Security | string |