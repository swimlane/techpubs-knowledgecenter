# ServiceNow Patch Custom Action

**Description**: Executes a custom PATCH action in ServiceNow using the 'mid_extension' path parameter.

## Endpoint

- **URL:** `api/{{mid_extension}}/v2/{{end_extension}}`
- **Method:** `PATCH`
## Inputs

- **path_parameters** (object) – Required: Auto-generated description for `path_parameters`. Please update manually if needed.
  - **mid_extension** (string) – Required: Auto-generated description for `mid_extension`. Please update manually if needed.
  - **end_extension** (string) – Required: Auto-generated description for `end_extension`. Please update manually if needed.
- **json_body** (object) – Required: Auto-generated description for `json_body`. Please update manually if needed.
  - **comments** (string): Auto-generated description for `comments`. Please update manually if needed.
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

- **status_code** (number): Auto-generated description for `status_code`. Please update manually if needed.
- **reason** (string): Auto-generated description for `reason`. Please update manually if needed.
- **json_body** (object): Auto-generated description for `json_body`. Please update manually if needed.
## Response Headers

| Header | Type | Description |
|--------|------|-------------|
| content-length | string | Auto-generated description for `content-length`. Please update manually if needed. |
| content-type | string | Auto-generated description for `content-type`. Please update manually if needed. |
| Date | string | Auto-generated description for `Date`. Please update manually if needed. |