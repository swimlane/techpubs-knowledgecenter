# Siem Clicks Blocked

**Description**: Fetch events for clicks to malicious URLs that were blocked by ProofPoint within a specified time period.

## Endpoint

- **URL:** `/v2/siem/clicks/blocked`
- **Method:** `GET`
## Inputs

| Name | Type | Description | Required |
|------|------|-------------|----------|
| parameters | object | One of the following three query parameters describing the desired time range for the data must be supplied with each request interval, sinceSeconds, sinceTime. | Yes |
## Output

### Example

```json
[
    {
        "status_code": 204,
        "response_headers": {
            "Date": "Mon, 16 Oct 2023 09:02:15 GMT",
            "Connection": "keep-alive",
            "Strict-Transport-Security": "max-age=15724800; includeSubDomains"
        },
        "reason": "No Content",
        "response_text": ""
    }
]
```
### Output Parameters

| Name | Type | Description |
|------|------|-------------|
| status_code | number |  |
| reason | string |  |
| response_text | string |  |
## Response Headers

| Header | Type | Description |
|--------|------|-------------|
| Date | string |  |
| Connection | string |  |
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