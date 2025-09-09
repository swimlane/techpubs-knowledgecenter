# Microsoft Defender Oauth 2.0 Client Credentials

**Description**: Authenticates using oauth 2.0 client credentials

## Inputs

- **url** (string) – Required: A URL to the target host.
- **tenant_id** (string): The Tenant ID.
- **token_url** (string): Must start with https://login.microsoftonline.com/ and then continue with the tenant_id, and then be prepended with /oauth2/v2.0/token
- **client_id** (string) – Required: The client ID
- **client_secret** (string) – Required: The client secret.
- **scope** (array) – Required: List of permission scopes for this action.
- **verify_ssl** (boolean): Verify SSL certificate
- **http_proxy** (string): A proxy to route requests through.