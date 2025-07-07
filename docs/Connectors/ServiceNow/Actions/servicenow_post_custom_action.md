# ServiceNow Post Custom Action

**Description**: Executes a custom action in ServiceNow using the 'mid_extension' path parameter provided by the user.

## Endpoint

- **URL:** `api/{{mid_extension}}/v2/{{end_extension}}`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required
  - **mid_extension** (string) – Required
  - **end_extension** (string) – Required
- **json_body** (object) – Required
  - **comments** (string)
- **parameters** (object): URL Query Parameters
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