# Patch Custom Endpoint

**Description**: Apply a PATCH request to a custom ServiceNow endpoint using specified path parameters with the v2 API.

## Endpoint

- **URL:** `api/now/v2/{{custom_endpoint}}`
- **Method:** `PATCH`
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