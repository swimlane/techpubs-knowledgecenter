# ServiceNow Post Custom Action

**Description**: Executes a custom action in ServiceNow using the 'mid_extension' path parameter provided by the user.

## Endpoint

- **URL:** `api/{{mid_extension}}/v2/{{end_extension}}`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required: TODO: Add description
  - **mid_extension** (string) – Required: TODO: Add description
  - **end_extension** (string) – Required: TODO: Add description
- **json_body** (object) – Required: TODO: Add description
  - **comments** (string): TODO: Add description
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

- **status_code** (number): TODO: Add description
- **reason** (string): TODO: Add description
- **json_body** (object): TODO: Add description
## Response Headers

| Header | Type | Description |
|--------|------|-------------|
| content-length | string | TODO: Add description |
| content-type | string | TODO: Add description |
| Date | string | TODO: Add description |