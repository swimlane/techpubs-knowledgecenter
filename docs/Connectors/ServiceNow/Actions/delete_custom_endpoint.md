# Delete Custom Endpoint

**Description**: Removes a specified custom endpoint from ServiceNow using the provided 'custom_endpoint' path parameter.

## Endpoint

- **URL:** `api/now/v2/{{custom_endpoint}}`
- **Method:** `DELETE`
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