# Get Product List Alerts by Investigation

**Description**: Retrieve all Rapid7 InsightIDR alerts associated with a given investigation identifier, including path parameters and headers.

## Endpoint

- **URL:** `idr/v2/investigations/{{identifier}}/rapid7-product-alerts`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **identifier** (string) – Required
- **parameters** (object)
  - **multi-customer** (boolean)
- **headers** (object) – Required
  - **Accept-version** (string) – Required
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Tue, 25 Jul 2023 05:13:19 GMT",
      "Content-Type": "application/json",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "Cache-Control": "no-cache, no-store, max-age=0, must-revalidate",
      "Expires": "0",
      "Pragma": "no-cache",
      "X-Content-Type-Options": "nosniff",
      "X-Frame-Options": "DENY",
      "X-XSS-Protection": "1; mode=block",
      "vary": "Origin",
      "Access-Control-Allow-Credentials": "true"
    },
    "reason": "OK",
    "json_body": [
      {
        "threat_command_details": {
          "alert_id": "620ba5123b2aff3303ed65f3",
          "alert_type": "Phishing",
          "applicable_close_reasons": [
            "ProblemSolved",
            "InformationalOnly",
            "Other"
          ]
        },
        "type": "THREAT_COMMAND"
      }
    ]
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (array)
  - **threat_command_details** (object)
    - **alert_id** (string)
    - **alert_type** (string)
    - **applicable_close_reasons** (array)
  - **type** (string)
## Response Headers

| Header | Type |
|--------|------|
| Date | string |
| Content-Type | string |
| Transfer-Encoding | string |
| Connection | string |
| Cache-Control | string |
| Expires | string |
| Pragma | string |
| X-Content-Type-Options | string |
| X-Frame-Options | string |
| X-XSS-Protection | string |
| vary | string |
| Access-Control-Allow-Credentials | string |