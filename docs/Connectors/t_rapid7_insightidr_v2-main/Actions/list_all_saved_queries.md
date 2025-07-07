# List All Saved Queries

**Description**: Retrieve all saved queries from Rapid7 InsightIDR for analysis or investigation purposes.

## Endpoint

- **URL:** `/log_search/query/saved_queries`
- **Method:** `GET`
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Fri, 21 Jun 2024 09:00:13 GMT",
      "Content-Type": "application/json",
      "Content-Length": "191",
      "Connection": "keep-alive",
      "Vary": "Origin, Accept-Encoding, Origin",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
      "R7-Correlation-Id": "14f165c3-d476-45e3-a9f1-13df3a33426b",
      "Access-Control-Allow-Credentials": "true",
      "Access-Control-Expose-Headers": "R7-Correlation-Id",
      "RateLimit-Limit": "1500",
      "RateLimit-Reset": "900",
      "RateLimit-Remaining": "1499",
      "X-RateLimit-Limit": "1500",
      "X-RateLimit-Reset": "900",
      "X-RateLimit-Remaining": "1499"
    },
    "reason": "OK",
    "json_body": {
      "saved_queries": [
        {
          "id": "00000000-0000-1616-0000-000000000000",
          "name": "Count of events",
          "leql": {
            "statement": "calculate(count)",
            "during": {
              "time_range": null,
              "to": null,
              "from": null
            }
          },
          "logs": []
        }
      ]
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **saved_queries** (array)
    - **id** (string)
    - **name** (string)
    - **leql** (object)
      - **statement** (string)
      - **during** (object)
        - **time_range** (object)
        - **to** (object)
        - **from** (object)
    - **logs** (array)
## Response Headers

| Header | Type |
|--------|------|
| Date | string |
| Content-Type | string |
| Content-Length | string |
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