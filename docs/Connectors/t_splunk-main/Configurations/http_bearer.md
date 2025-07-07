# HTTP Bearer Authentication

**Description**: Authenticates using bearer token such as a JWT, etc.

## Inputs

- **url** (string) – Required: A URL to the target host.
- **token** (string) – Required: The API key, token, etc.
- **splunk_enterprise_version** (string): Splunk Enterprise version to call updated endpoints as from 9.0.1 version, v1 instances of some endpoints are deprecated, and v2 instances of these endpoints are available.
- **verify_ssl** (boolean): Verify SSL certificate
- **http_proxy** (string): A proxy to route requests through.