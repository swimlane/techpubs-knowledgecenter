# HTTP Basic Authentication

**Description**: Authenticates using username and password.

## Inputs

- **url** (string) – Required: A URL to the target host.
- **username** (string) – Required: Username
- **password** (string) – Required: Password
- **splunk_enterprise_version** (string): Splunk Enterprise version to call updated endpoints as from 9.0.1 version, v1 instances of some endpoints are deprecated, and v2 instances of these endpoints are available.
- **verify_ssl** (boolean): Verify SSL certificate
- **http_proxy** (string): A proxy to route requests through.