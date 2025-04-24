# Delete Custom Endpoint

**Description**: Removes a specified custom endpoint from ServiceNow using the provided 'custom_endpoint' path parameter.

## Endpoint

- **URL:** `api/now/v2/{{custom_endpoint}}`
- **Method:** `DELETE`
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