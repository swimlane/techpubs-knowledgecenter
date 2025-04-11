# Get Table

**Description**: Retrieves records from a specified ServiceNow table using the 'tableName' path parameter.

## Endpoint

- **URL:** `api/now/v2/table/{{tableName}}`
- **Method:** `GET`
## Inputs

| Name | Type | Required |
|------|------|----------|
| path_parameters | object | Yes |
| parameters | object | No |
## Output

### Output Parameters

| Name | Type |
|------|------|
| status_code | number |
| reason | string |
| json_body | object |