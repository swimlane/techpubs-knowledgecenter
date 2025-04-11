# Update Incident

**Description**: Updates an existing incident in ServiceNow using the unique sys_id and additional data provided in a JSON body.

## Endpoint

- **URL:** `/api/now/table/incident/{{sys_id}}`
- **Method:** `PATCH`
## Inputs

| Name | Type | Required |
|------|------|----------|
| path_parameters | object | Yes |
| json_body | object | Yes |
## Output

### Output Parameters

| Name | Type |
|------|------|
| status_code | number |
| reason | string |
| response_text | string |
## Response Headers

| Header | Type | Description |
|--------|------|-------------|
| Set-Cookie | string |  |
| Server-Timing | string |  |
| Content-Security-Policy | string |  |
| Content-Length | string |  |
| Date | string |  |
| Keep-Alive | string |  |
| Connection | string |  |
| Server | string |  |
| Strict-Transport-Security | string |  |