# Delete Custom Endpoint

**Description**: Removes a specified custom endpoint from ServiceNow using the provided 'custom_endpoint' path parameter.

## Endpoint

- **URL:** `api/now/v2/{{custom_endpoint}}`
- **Method:** `DELETE`
## Inputs

- **path_parameters** (object) – Required: Auto-generated description for `path_parameters`. Please update manually if needed.
  - **custom_endpoint** (string) – Required: Auto-generated description for `custom_endpoint`. Please update manually if needed.
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

- **status_code** (number): Auto-generated description for `status_code`. Please update manually if needed.
- **reason** (string): Auto-generated description for `reason`. Please update manually if needed.
- **json_body** (object): Auto-generated description for `json_body`. Please update manually if needed.