# Post Custom Endpoint

**Description**: Executes a POST request to a custom endpoint in ServiceNow v2, specified by the 'custom_endpoint' path parameter.

## Endpoint

- **URL:** `api/now/v2/{{custom_endpoint}}`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required: Auto-generated description for `path_parameters`. Please update manually if needed.
  - **custom_endpoint** (string) – Required: Auto-generated description for `custom_endpoint`. Please update manually if needed.
- **parameters** (object): Auto-generated description for `parameters`. Please update manually if needed.
  - **sysparm_display_value** (boolean): Auto-generated description for `sysparm_display_value`. Please update manually if needed.
  - **sysparm_input_display_value** (boolean): Auto-generated description for `sysparm_input_display_value`. Please update manually if needed.
- **json_body** (object): JSON Body
- **data_body** (object): Data Body
## Output

### Example

```json
[
  {}
]
```