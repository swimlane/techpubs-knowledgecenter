# Get Alerts

**Description**: Fetches alert events from Forti Analyzer, allowing for monitoring and analysis of security alerts.

## Endpoint

- **URL:** `/eventmgmt/alerts`
- **Method:** `GET`
## Inputs

| Name | Type | Description | Required |
|------|------|-------------|----------|
| json_body | object |  | Yes |
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

| Name | Type | Description |
|------|------|-------------|
| status_code | number |  |
| reason | string |  |
| json_body | object |  |
## Response Headers

| Header | Type | Description |
|--------|------|-------------|
| content-length | string |  |
| content-type | string |  |
| Date | string |  |
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