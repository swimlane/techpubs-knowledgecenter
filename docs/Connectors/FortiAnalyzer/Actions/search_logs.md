# Search Logs

**Description**: Initiates a task to search logs in Forti Analyzer with specified parameters, requiring a 'params' JSON body input.

## Endpoint

- **URL:** `/logview/logsearch`
- **Method:** `POST`
## Inputs

| Name | Type | Required |
|------|------|----------|
| json_body | object | Yes |
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "OK",
    "json_body": {
      "id": "string",
      "jsonrpc": "2.0",
      "result": {
        "tid": 0
      }
    }
  }
]
```
### Output Parameters

| Name | Type |
|------|------|
| status_code | number |
| reason | string |
| json_body | object |