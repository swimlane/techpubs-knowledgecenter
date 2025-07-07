# List All Users

**Description**: List all users in the user collection.

## Endpoint

- **URL:** `Snypr/ws/spotter/index/search?query=index=users`
- **Method:** `GET`
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Thu, 25 Jan 2024 00:29:53 GMT",
      "Content-Type": "text/plain",
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
      "totalDocuments": 1000,
      "events": [
        {
          "country": "United States",
          "userriskscore": "0.01",
          "firstname": "Titus",
          "employeetype": "Employee",
          "manageremployeeid": "301406",
          "masked": "false",
          "usertimezoneoffset": "CST6CDT",
          "createdate": "1696008076626",
          "title": "Senior Principal Application Architect",
          "employeeid": "\u00ef\u00bb\u00bf302481",
          "userid": "Titus.Berry",
          "lastname": "Berry",
          "division": "Arch & Enterprise Services",
          "tenantid": "5",
          "usercriticality": "Low",
          "managerlastname": "Perry",
          "workemail": "Titus.Berry@discprogres.com",
          "tenantname": "Financial Threat",
          "location": "Raleigh",
          "fullname": "Titus Berry",
          "department": "Application Architecture",
          "managerfirstname": "Leif",
          "status": "1"
        }
      ],
      "error": false,
      "available": false,
      "queryId": "spotterwebservicea98ad391-ed14-4ec1-ae7a-4295fff2fa23",
      "applicationTz": "CST6CDT",
      "inputParams": {
        "query": "index=users"
      },
      "index": "users",
      "nextCursorMarker": "AoEpMl5+MTA3NDAy"
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **totalDocuments** (number)
  - **events** (array)
    - **country** (string)
    - **userriskscore** (string)
    - **firstname** (string)
    - **employeetype** (string)
    - **manageremployeeid** (string)
    - **masked** (string)
    - **usertimezoneoffset** (string)
    - **createdate** (string)
    - **title** (string)
    - **employeeid** (string)
    - **userid** (string)
    - **lastname** (string)
    - **division** (string)
    - **tenantid** (string)
    - **usercriticality** (string)
    - **managerlastname** (string)
    - **workemail** (string)
    - **tenantname** (string)
    - **location** (string)
    - **fullname** (string)
    - **department** (string)
    - **managerfirstname** (string)
    - **status** (string)
  - **error** (boolean)
  - **available** (boolean)
  - **queryId** (string)
  - **applicationTz** (string)
  - **inputParams** (object)
    - **query** (string)
  - **index** (string)
  - **nextCursorMarker** (string)
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