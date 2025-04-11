# Get Alerts

**Description**: Fetches alert events from Forti Analyzer, allowing for monitoring and analysis of security alerts.

## Endpoint

- **URL:** `/eventmgmt/alerts`
- **Method:** `GET`
## Inputs

| Name | Type | Required |
|------|------|----------|
| json_body | object | Yes |
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "content-length": "140",
      "content-type": "application/json",
      "Date": "Thu, 2 May 2024 20:37:23 GMT"
    },
    "reason": "OK",
    "json_body": {}
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
| content-length | string |
| content-type | string |
| Date | string |