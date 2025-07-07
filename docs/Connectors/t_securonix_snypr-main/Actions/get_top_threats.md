# Get Top Threats

**Description**: Get top threats in the specified time period and count of violators for each threat.

## Endpoint

- **URL:** `Snypr/ws/sccWidget/getTopThreats`
- **Method:** `GET`
## Inputs

- **parameters** (object) – Required
  - **dateunit** (string) – Required
  - **dateunitvalue** (number) – Required
  - **offset** (number) – Required
  - **max** (number) – Required
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Thu, 25 Jan 2024 00:34:04 GMT",
      "Content-Type": "application/json",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "Strict-Transport-Security": "max-age=31536000 ; includeSubDomains",
      "Cache-Control": "private, no-store, no-cache, must-revalidate",
      "X-FRAME-OPTIONS": "DENY",
      "Pragma": "no-cache",
      "X-XSS-Protection": "1 ;mode=block",
      "X-Content-Type-Options": "nosniff",
      "Content-Security-Policy": "frame-ancestors 'self' *.securonix.net; default-src 'self' *.securonix.net; object-src 'self' *.securonix.net data: blob:; script-src 'unsafe-inline' 'unsafe-eval' 'self' *.securonix.net https://edge.fullstory.com https://rs.fullstory.com http://iph.zoominsoftware.io/widget.js data: blob:; style-src 'self' *.securonix.net https://fonts.googleapis.com 'unsafe-inline'; font-src 'self' *.securonix.net https://fonts.gstatic.com 'unsafe-inline'; connect-src 'self' *.securonix.net https://edge.fullstory.com https://rs.fullstory.com https://securonix-be-prod.zoominsoftware.io http://documentation-be.securonix.com wss://saaspoc5t16expo.securonix.net:443 data: blob:; img-src 'self' *.securonix.net https://rs.fullstory.com data: https:; child-src 'self' *.securonix.net blob:;"
    },
    "reason": "",
    "json_body": {
      "Response": {
        "Date range": [
          "Jun 11, 2018 11:18:09 AM",
          "Sep 9, 2018 11:18:09 AM"
        ],
        "Total records": 8,
        "Docs": [
          {
            "Threat model id": 118,
            "Threat nodel name": "Patient Data Compromise",
            "Description": "No of Stages: 4, Risk Scoring Scheme:STATIC, Weight:100.0",
            "Criticality": "Low",
            "No of violator": 1,
            "Generation time": 1532388410500
          },
          {
            "Threat model id": 194,
            "Threat nodel name": "Privileged IT User-Sabotage",
            "Description": "No of Stages: 4, Risk Scoring Scheme:STATIC, Weight:100.0",
            "Criticality": "Medium",
            "No of violator": 1,
            "Generation time": 1532372629487
          }
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
  - **Response** (object)
    - **Date range** (array)
    - **Total records** (number)
    - **Docs** (array)
      - **Threat model id** (number)
      - **Threat nodel name** (string)
      - **Description** (string)
      - **Criticality** (string)
      - **No of violator** (number)
      - **Generation time** (number)
## Response Headers

| Header | Type |
|--------|------|
| Date | string |
| Content-Type | string |
| Transfer-Encoding | string |
| Connection | string |
| Strict-Transport-Security | string |
| Cache-Control | string |
| X-FRAME-OPTIONS | string |
| Pragma | string |
| X-XSS-Protection | string |
| X-Content-Type-Options | string |
| Content-Security-Policy | string |