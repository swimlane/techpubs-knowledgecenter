# Oauth 2.0 Client Credentials

**Description**: Authenticates using oauth 2.0 client credentials

## Inputs

| Name | Type | Description | Required |
|------|------|-------------|----------|
| url | string | A URL to the target host. | Yes |
| token_url | string |  | Yes |
| client_id | string | The client ID | Yes |
| client_secret | string | The client secret. | Yes |
| scope | array | Permission scopes for this action. | No |
| verify_ssl | boolean | Verify SSL certificate | No |
| http_proxy | string | A proxy to route requests through. | No |
## Output

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