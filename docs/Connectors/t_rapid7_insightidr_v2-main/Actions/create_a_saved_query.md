# Create a Saved Query

**Description**: Initiates the creation of a saved query in Rapid7 InsightIDR using the provided 'saved_query' details.

## Endpoint

- **URL:** `/log_search/query/saved_queries`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required
  - **saved_query** (object) – Required
    - **name** (string) – Required: The name for the Saved Query.
    - **leql** (object) – Required
      - **during** (object)
        - **from** (number): The start of the time range for the query, as a UNIX timestamp in milliseconds.
        - **to** (number): The end of the time range for the query, as a UNIX timestamp in milliseconds.
        - **time_range** (string): Relative time range (instead of absolute from + to time range). Possible values are "yesterday", "today" and "last x timeunits" where x is the number of time unit back from the current server time. Supported time units (case insensitive) are min(s) or minute(s), hr(s) or hour(s), day(s), week(s), month(s) and year(s).
      - **statement** (string) – Required: The LEQL query run against the log(s). If empty, the query retrieves all log entries in the specified time range.
    - **logs** (array): The log keys of the logs which the query is run against.
## Output

### Example

```json
[
  {
    "status_code": 201,
    "response_headers": {
      "Date": "Fri, 21 Jun 2024 09:18:35 GMT",
      "Content-Type": "application/json",
      "Content-Length": "180",
      "Connection": "keep-alive",
      "Vary": "Origin, Accept-Encoding, Origin",
      "Location": "https://us3.api.insight.rapid7.com/log_search/query/saved_queries/00000000-0000-1618-0000-000000000000",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
      "R7-Correlation-Id": "3f4f3a96-4af9-4229-9303-30dd632beb93",
      "Access-Control-Allow-Credentials": "true",
      "Access-Control-Expose-Headers": "R7-Correlation-Id",
      "RateLimit-Limit": "1500",
      "RateLimit-Reset": "900",
      "RateLimit-Remaining": "1499",
      "X-RateLimit-Limit": "1500",
      "X-RateLimit-Reset": "900",
      "X-RateLimit-Remaining": "1499"
    },
    "reason": "Created",
    "json_body": {
      "saved_query": {
        "id": "00000000-0000-1618-0000-000000000000",
        "name": "saved-query-2",
        "leql": {
          "statement": "where(test)",
          "during": {
            "time_range": null,
            "to": null,
            "from": null
          }
        },
        "logs": [
          ""
        ]
      }
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **saved_query** (object)
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
| Location | string |
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