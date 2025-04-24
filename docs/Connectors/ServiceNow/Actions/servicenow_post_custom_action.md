# ServiceNow Post Custom Action

**Description**: Executes a custom action in ServiceNow using the 'mid_extension' path parameter provided by the user.

## Endpoint

- **URL:** `api/{{mid_extension}}/v2/{{end_extension}}`
- **Method:** `POST`
## Inputs

| Name | Type | Description | Required |
|------|------|-------------|----------|
| path_parameters | object |  | Yes |
| json_body | object |  | Yes |
| parameters | object | URL Query Parameters | No |
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

| Name | Type |
|------|------|
| status_code | number |
| reason | string |
| json_body | object |
## Response Headers

| Header | Type |
|--------|------|
| content-length | string |
| content-type | string |
| Date | string |