# ServiceNow Get Custom Action

**Description**: Executes a custom action in ServiceNow by targeting specific API endpoints with 'mid_extension' and 'end_extension' path parameters.

## Endpoint

- **URL:** `api/{{mid_extension}}/v2/{{end_extension}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **mid_extension** (string) – Required
  - **end_extension** (string) – Required
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "content-length": "140",
      "content-type": "application/json",
      "Date": "Mon, 2 Sep 2024 20:37:23 GMT"
    },
    "reason": "OK",
    "json_body": {}
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
## Response Headers

- **content-length** (string)
- **content-type** (string)
- **Date** (string)