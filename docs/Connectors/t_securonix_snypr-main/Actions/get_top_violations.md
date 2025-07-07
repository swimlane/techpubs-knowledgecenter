# Get Top Violations

**Description**: Get top violations in the specified time period and count of violators for each violation.

## Endpoint

- **URL:** `Snypr/ws/sccWidget/getTopViolations`
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
      "Date": "Thu, 25 Jan 2024 00:33:45 GMT",
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
          "Jun 11, 2018 11:25:55 AM",
          "Sep 9, 2018 11:25:55 AM"
        ],
        "Total records": 38,
        "Docs": [
          {
            "Policy id": 9237,
            "Policy name": "Email to Competitor Domain",
            "Criticality": "Medium",
            "Violation entity": "Activityaccount",
            "Policy category": "ALERT",
            "Threat indicator": "Email to Competitor Domain",
            "Generation time": 1533250072115,
            "No of violator": 14,
            "Description": "Email to Competitor Domain"
          },
          {
            "Policy id": 9236,
            "Policy name": "Abnormal number of emails sent to external domain as compared to peer members",
            "Criticality": "Low",
            "Violation entity": "Activityaccount",
            "Policy category": "ALERT",
            "Threat indicator": "Abnormal number of emails sent to external domain as compared to peer members",
            "Generation time": 1533171483400,
            "No of violator": 1,
            "Description": "Abnormal number of emails sent to external domain as compared to peer members"
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
      - **Policy id** (number)
      - **Policy name** (string)
      - **Criticality** (string)
      - **Violation entity** (string)
      - **Policy category** (string)
      - **Threat indicator** (string)
      - **Generation time** (number)
      - **No of violator** (number)
      - **Description** (string)
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