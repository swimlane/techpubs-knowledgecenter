# ServiceNow Get Custom Action

**Description**: Executes a custom action in ServiceNow by targeting specific API endpoints with 'mid_extension' and 'end_extension' path parameters.

## Endpoint

- **URL:** `api/{{mid_extension}}/v2/{{end_extension}}`
- **Method:** `GET`
## Inputs

| Name | Type | Description | Required |
|------|------|-------------|----------|
| path_parameters | object |  | Yes |
## Output

### Output Parameters

| Name | Type | Description |
|------|------|-------------|
| status_code | number |  |
| reason | string |  |
| json_body | object |  |
## Response Headers

| Header | Type | Description |
|--------|------|-------------|
| content-length | string |  |
| content-type | string |  |
| Date | string |  |