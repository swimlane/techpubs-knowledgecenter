# CyberArk Oauth 2.0 Client Credentials

**Description**: Authenticates using oauth 2.0 client credentials

## Inputs

- **url** (string) – Required: A URL to the target host.
- **identity_tenant_id** (string) – Required: Identity Tenant ID.
- **client_id** (string) – Required: User name. The user login name as displayed in the Identity Administration portal Users list - login_name@<suffix>.
- **client_secret** (string) – Required: Password. The access password defined for the user.
- **verify_ssl** (boolean): Verify SSL certificate
- **http_proxy** (string): A proxy to route requests through.