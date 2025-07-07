# Get Custom Endpoint

**Description**: Retrieves data from a specified ServiceNow custom endpoint using the 'custom_endpoint' path parameter.

## Endpoint

- **URL:** `api/now/v2/{{custom_endpoint}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **custom_endpoint** (string) – Required
- **parameters** (object)
  - **display_value** (boolean)
  - **sysparm_limit** (number)
- **json_body** (object): JSON Body
- **data_body** (object): Data Body
## Output

### Example

```json
[
  {}
]
```