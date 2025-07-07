# Get Top Violators

**Description**: Get top violators in the specified time period and risk score of each violator.

## Endpoint

- **URL:** `Snypr/ws/sccWidget/getTopViolators`
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
      "Date": "Thu, 25 Jan 2024 00:33:27 GMT",
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
          "Jun 11, 2018 11:28:44 AM",
          "Sep 9, 2018 11:28:44 AM"
        ],
        "Total records": 10,
        "Docs": [
          {
            "Name": "212274BB375846F85252DBD2CCBE7AE4 8E2657AD25B3904CCC449C202598B9B0 ",
            "Violator entity": "Users",
            "Risk score": 202.4,
            "Generation time": 1529035574167,
            "Department": "E2DE4125FB3335921E1CC05ED00C504A1E0BBBA898C335B9BA10B29F657B9401\t"
          },
          {
            "Name": "ACF8393CF33B5115506E12D9520EDD15 0CC721E95079DA18955B82AA67F5A4F9 ",
            "Violator entity": "Users",
            "Risk score": 140.48,
            "Generation time": 1532053492068,
            "Department": "6A2B422B8F594566BA327664B83594383D1FDE1BF5ED4FC39165D247B21CBF50\t"
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
      - **Name** (string)
      - **Violator entity** (string)
      - **Risk score** (number)
      - **Generation time** (number)
      - **Department** (string)
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