# Post Custom Endpoint

**Description**: Executes a POST request to a custom endpoint in ServiceNow v2, specified by the 'custom_endpoint' path parameter.

## Endpoint

- **URL:** `api/now/v2/{{custom_endpoint}}`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required: TODO: Add description
  - **custom_endpoint** (string) – Required: TODO: Add description
- **parameters** (object): TODO: Add description
  - **sysparm_display_value** (boolean): TODO: Add description
  - **sysparm_input_display_value** (boolean): TODO: Add description
- **json_body** (object): JSON Body
- **data_body** (object): Data Body
## Output

### Example

```json
[
  {}
]
```