# Create Table Row

**Description**: Creates a new entry in the specified ServiceNow table using provided path parameters and display values.

## Endpoint

- **URL:** `api/now/v2/table/{{tableName}}`
- **Method:** `POST`
## Inputs

| Name | Type | Description | Required |
|------|------|-------------|----------|
| path_parameters | object |  | Yes |
| parameters | object |  | Yes |
| json_body | object |  | Yes |
## Output

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