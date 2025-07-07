# List All Policies

**Description**: List of Policies (aka rules) configured in SNYPR to detect Violators, Violations and Threats. Response includes all policies available in the system.

## Endpoint

- **URL:** `Snypr/ws/policy/getAllPolicies`
- **Method:** `GET`
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Thu, 25 Jan 2024 00:32:56 GMT",
      "Content-Type": "application/xml",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "Strict-Transport-Security": "max-age=31536000 ; includeSubDomains",
      "Cache-Control": "private, no-store, no-cache, must-revalidate",
      "X-FRAME-OPTIONS": "DENY",
      "Pragma": "no-cache",
      "X-XSS-Protection": "1 ;mode=block",
      "X-Content-Type-Options": "nosniff",
      "Content-Security-Policy": "frame-ancestors 'self' *.securonix.net; default-src 'self' *.securonix.net; object-src 'self' *.securonix.net data: blob:; script-src 'unsafe-inline' 'unsafe-eval' 'self' *.securonix.net https://edge.fullstory.com https://rs.fullstory.com http://iph.zoominsoftware.io/widget.js data: blob:; style-src 'self' *.securonix.net https://fonts.googleapis.com 'unsafe-inline'; font-src 'self' *.securonix.net https://fonts.gstatic.com 'unsafe-inline'; connect-src 'self' *.securonix.net https://edge.fullstory.com https://rs.fullstory.com https://securonix-be-prod.zoominsoftware.io http://documentation-be.securonix.com wss://saaspoc5t16expo.securonix.net:443 data: blob:; img-src 'self' *.securonix.net https://rs.fullstory.com data: https:; child-src 'self' *.securonix.net blob:;",
      "Set-Cookie": "JSESSIONID=610ACE2E3BABF8B2A161B50770A84799; Path=/Snypr; Secure; HttpOnly"
    },
    "reason": "",
    "json_body": {
      "policies": {
        "policy": [
          {
            "createdBy": "admin",
            "createdOn": "2022-12-09T18:04:38Z",
            "criticality": "None",
            "description": "Description: Data downloaded from FTP ports may be indicative of malicious insider/cyber aggregation activity which can later be used for exfiltration.\r\nTechnique Used: Behavior Anomaly for Data Download Activity",
            "hql": null,
            "id": "1927",
            "name": "Abnormal amount of data aggregated from FTP ports - Next Gen Firewall"
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
  - **policies** (object)
    - **policy** (array)
      - **createdBy** (string)
      - **createdOn** (string)
      - **criticality** (string)
      - **description** (string)
      - **hql** (object)
      - **id** (string)
      - **name** (string)
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
| Set-Cookie | string |