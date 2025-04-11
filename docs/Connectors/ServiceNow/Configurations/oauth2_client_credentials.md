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