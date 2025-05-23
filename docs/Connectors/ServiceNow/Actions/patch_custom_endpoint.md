# Patch Custom Endpoint

**Description**: Apply a PATCH request to a custom ServiceNow endpoint using specified path parameters with the v2 API.

## Endpoint

- **URL:** `api/now/v2/{{custom_endpoint}}`
- **Method:** `PATCH`
## Inputs

| Name | Type | Description | Required |
|------|------|-------------|----------|
| path_parameters | object |  | Yes |
| parameters | object | URL Query Parameters | No |
| json_body | object | JSON Body | No |
| data_body | object | Data Body | No |
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

| Name | Type |
|------|------|
| status_code | number |
| reason | string |
| json_body | object |