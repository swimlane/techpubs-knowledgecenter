# Forensics Campaign

**Description**: Retrieve aggregate forensics data for a specified campaign in ProofPoint using the campaignId parameter.

## Endpoint

- **URL:** `/v2/forensics`
- **Method:** `GET`
## Inputs

| Name | Type | Description | Required |
|------|------|-------------|----------|
| parameters | object |  | Yes |
## Output

### Example

```json
[
    {
        "status_code": 200,
        "response_headers": {
            "Date": "Wed, 18 Oct 2023 13:42:53 GMT",
            "Content-Type": "application/json",
            "Content-Length": "188",
            "Connection": "keep-alive",
            "X-Content-Type-Options": "nosniff",
            "Vary": "Accept-Encoding, User-Agent",
            "Content-Encoding": "gzip",
            "Strict-Transport-Security": "max-age=15724800; includeSubDomains"
        },
        "reason": "OK",
        "json_body": {
            "generated": "2023-10-18T13:42:53.056Z",
            "reports": [
                {
                    "scope": "CAMPAIGN",
                    "id": "e144426d-7bcd-4695-98a7-c9f6551f3d48",
                    "name": "Ursnif \"2000\" | US Targeting | URLs | 3 July 2019",
                    "forensics": []
                }
            ]
        }
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
| Date | string |  |
| Content-Type | string |  |
| Content-Length | string |  |
| Connection | string |  |
| X-Content-Type-Options | string |  |
| Vary | string |  |
| Content-Encoding | string |  |
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