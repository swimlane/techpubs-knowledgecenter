# Patch Custom Endpoint

**Description**: Apply a PATCH request to a custom ServiceNow endpoint using specified path parameters with the v2 API.

## Endpoint

- **URL:** `api/now/v2/{{custom_endpoint}}`
- **Method:** `PATCH`
## Inputs

- **path_parameters** (object) – Required: Structured object with nested properties.
  - **custom_endpoint** (string) – Required: Text string.
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

- **status_code** (number): Status value or code.
- **reason** (string): Text string.
- **json_body** (object): Structured object with nested properties.