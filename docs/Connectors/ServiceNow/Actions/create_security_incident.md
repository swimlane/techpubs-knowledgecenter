# Create Security Incident

**Description**: Creates a new security incident in ServiceNow based on the provided path parameters.

## Endpoint

- **URL:** `/api/now/table/{{security_incident}}`
- **Method:** `POST`
## Inputs

| Name | Type | Required |
|------|------|----------|
| path_parameters | object | Yes |
| json_body | object | No |
## Output

### Output Parameters

| Name | Type |
|------|------|
| status_code | number |
| reason | string |
| json_body | object |
## Response Headers

| Header | Type | Description |
|--------|------|-------------|
| Set-Cookie | string |  |
| Server-Timing | string |  |
| Content-Encoding | string |  |
| X-Is-Logged-In | string |  |
| X-Transaction-ID | string |  |
| Location | string |  |
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
| Strict-Transport-Security | string |  |