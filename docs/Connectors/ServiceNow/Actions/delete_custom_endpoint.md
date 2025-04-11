# Delete Custom Endpoint

**Description**: Removes a specified custom endpoint from ServiceNow using the provided 'custom_endpoint' path parameter.

## Endpoint

- **URL:** `api/now/v2/{{custom_endpoint}}`
- **Method:** `DELETE`
## Inputs

| Name | Type | Description | Required |
|------|------|-------------|----------|
| path_parameters | object |  | Yes |
| parameters | object | URL Query Parameters | No |
| json_body | object | JSON Body | No |
| data_body | object | Data Body | No |
## Output

### Example

```json
- json_body: {}
  reason: OK
  response_headers: {}
  status_code: 200

```
### Output Parameters

| Name | Type | Description |
|------|------|-------------|
| status_code | number |  |
| reason | string |  |
| json_body | object |  |
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