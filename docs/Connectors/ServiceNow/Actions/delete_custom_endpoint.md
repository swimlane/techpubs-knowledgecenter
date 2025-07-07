# Delete Custom Endpoint

**Description**: Removes a specified custom endpoint from ServiceNow using the provided 'custom_endpoint' path parameter.

## Endpoint

- **URL:** `api/now/v2/{{custom_endpoint}}`
- **Method:** `DELETE`
## Inputs

- **path_parameters** (object) – Required: TODO: Add description
  - **custom_endpoint** (string) – Required: TODO: Add description
- **parameters** (object): URL Query Parameters
- **json_body** (object): JSON Body
- **data_body** (object): Data Body
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "OK",
    "json_body": {}
  }
]
```
### Output Parameters

- **status_code** (number): TODO: Add description
- **reason** (string): TODO: Add description
- **json_body** (object): TODO: Add description