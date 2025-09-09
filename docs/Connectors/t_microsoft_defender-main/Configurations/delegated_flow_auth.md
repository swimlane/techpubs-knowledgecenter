# Microsoft Defender Password Grant (Delegated Auth)

**Description**: Authenticates on behalf of a user using oauth 2.0 credentials

## Inputs

- **url** (string) – Required: A URL to the target host.
- **login_url** (string)
- **tenant_id** (string) – Required
- **oauth_un** (string) – Required: The username for authentication
- **oauth_pwd** (string) – Required: The password for authentication
- **oauth_cl_id** (string) – Required: The client ID
- **oauth_cl_secret** (string) – Required: The client secret.
- **scope** (array): Permission scopes for this action.
- **verify_ssl** (boolean): Verify SSL certificate
- **http_proxy** (string): A proxy to route requests through.