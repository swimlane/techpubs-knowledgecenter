# Get Alerts

**Description**: Fetches alert events from Forti Analyzer, allowing for monitoring and analysis of security alerts.

## Endpoint

- **URL:** `/eventmgmt/alerts`
- **Method:** `GET`
## Inputs

| Name | Type | Required |
|------|------|----------|
| json_body | object | Yes |
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
| content-length | string |  |
| content-type | string |  |
| Date | string |  |