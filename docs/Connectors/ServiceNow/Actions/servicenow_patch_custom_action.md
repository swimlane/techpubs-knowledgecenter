# ServiceNow Patch Custom Action

**Description**: Executes a custom PATCH action in ServiceNow using the 'mid_extension' path parameter.

## Endpoint

- **URL:** `api/{{mid_extension}}/v2/{{end_extension}}`
- **Method:** `PATCH`
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

| Header | Type | Description |
|--------|------|-------------|
| content-length | string |  |
| content-type | string |  |
| Date | string |  |