# Put Custom Endpoint

**Description**: Executes a PUT request to a ServiceNow custom endpoint using the specified path parameter.

## Endpoint

- **URL:** `api/now/v2/{{custom_endpoint}}`
- **Method:** `PUT`
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
  {}
]
```