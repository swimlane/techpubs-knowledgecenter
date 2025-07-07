# ServiceNow Post Custom Action

**Description**: Executes a custom action in ServiceNow using the 'mid_extension' path parameter provided by the user.

## Endpoint

- **URL:** `api/{{mid_extension}}/v2/{{end_extension}}`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required: Structured object with nested properties.
  - **mid_extension** (string) – Required: Unique identifier.
  - **end_extension** (string) – Required: Text string.
- **json_body** (object) – Required: Structured object with nested properties.
  - **comments** (string): Text string.
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

- **status_code** (number): Status value or code.
- **reason** (string): Text string.
- **json_body** (object): Structured object with nested properties.
## Response Headers

| Header | Type | Description |
|--------|------|-------------|
| content-length | string | Text string. |
| content-type | string | Type of the resource or value. |
| Date | string | Timestamp in ISO 8601 format. |