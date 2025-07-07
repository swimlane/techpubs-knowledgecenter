# HaloPSA Oauth 2.0 Password Grant

**Description**: Authenticates using oauth 2.0 client credentials

## Inputs

- **url** (string) – Required: A URL to the target host.
- **tenant_id** (string): The Tenant ID.
- **oauth2_username** (string) – Required: The username for authentication
- **oauth2_password** (string) – Required: The password for authentication
- **client_id** (string) – Required: The client ID
- **scope** (array) – Required: Permission scopes for this action.
- **verify_ssl** (boolean): Verify SSL certificate
- **http_proxy** (string): A proxy to route requests through.