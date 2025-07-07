# Delete a Saved Query

**Description**: Removes a specified saved query from Rapid7 InsightIDR using the provided unique saved_query_id.

## Endpoint

- **URL:** `/log_search/query/saved_queries/{{saved_query_id}}`
- **Method:** `DELETE`
## Inputs

- **path_parameters** (object) – Required
  - **saved_query_id** (string) – Required: The ID of the saved query.
## Output

### Example

```json
[
  {
    "status_code": 204,
    "response_headers": {
      "Date": "Fri, 21 Jun 2024 09:07:47 GMT",
      "Connection": "keep-alive",
      "Vary": "Origin, Origin",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
      "R7-Correlation-Id": "5d143985-8028-4204-a2f9-f18e1848b30b",
      "Access-Control-Allow-Credentials": "true",
      "Access-Control-Expose-Headers": "R7-Correlation-Id",
      "RateLimit-Limit": "1500",
      "RateLimit-Reset": "445",
      "RateLimit-Remaining": "1497",
      "X-RateLimit-Limit": "1500",
      "X-RateLimit-Reset": "445",
      "X-RateLimit-Remaining": "1497"
    },
    "reason": "No Content",
    "response_text": ""
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **response_text** (string)
## Response Headers

| Header | Type |
|--------|------|
| Date | string |
| Connection | string |
| Vary | string |
| Strict-Transport-Security | string |
| R7-Correlation-Id | string |
| Access-Control-Allow-Credentials | string |
| Access-Control-Expose-Headers | string |
| RateLimit-Limit | string |
| RateLimit-Reset | string |
| RateLimit-Remaining | string |
| X-RateLimit-Limit | string |
| X-RateLimit-Reset | string |
| X-RateLimit-Remaining | string |