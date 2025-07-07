# Get Custom Endpoint

**Description**: Retrieves data from a specified ServiceNow custom endpoint using the 'custom_endpoint' path parameter.

## Endpoint

- **URL:** `api/now/v2/{{custom_endpoint}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required: Structured object with nested properties.
  - **custom_endpoint** (string) – Required: Text string.
- **parameters** (object): Structured object with nested properties.
  - **display_value** (boolean): True or False value.
  - **sysparm_limit** (number): Numerical value.
- **json_body** (object): JSON Body
- **data_body** (object): Data Body
## Output

### Example

```json
[
  {}
]
```