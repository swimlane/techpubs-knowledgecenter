# Get Alert

**Description**: Gets the list of Alerts

## Endpoint

- **URL:** `/rest/alert`
- **Method:** `GET`
## Inputs

- **parameters** (object)
  - **fields** (string): Specify the fields want to include in the response
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Mon, 15 Apr 2024 06:31:29 GMT",
      "Server": "Apache",
      "X-Frame-Options": "DENY",
      "Content-Security-Policy": "default-src 'self'; script-src 'self' pendo-io-static.storage.googleapis.com app.pendo.io cdn.pendo.io pendo-static-6165929460760576.storage.googleapis.com data.pendo.io cdn.metarouter.io e.metarouter.io api.amplitude.com cdn.amplitude.com *.cloudfront.net; connect-src 'self' app.pendo.io data.pendo.io pendo-static-6165929460760576.storage.googleapis.com cdn.metarouter.io e.metarouter.io api.amplitude.com cdn.amplitude.com *.cloudfront.net; img-src 'self' data: cdn.pendo.io app.pendo.io pendo-static-6165929460760576.storage.googleapis.com data.pendo.io; style-src 'self' app.pendo.io cdn.pendo.io pendo-static-6165929460760576.storage.googleapis.com; frame-ancestors app.pendo.io; form-action 'self'; block-all-mixed-content; Upgrade-Insecure-Requests: 1; object-src 'none'",
      "X-Content-Type-Options": "nosniff",
      "X-XSS-Protection": "1; mode=block",
      "Expect-CT": "max-age=31536000",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
      "Vary": "x-apikey",
      "Set-Cookie": "TNS_SESSIONID=07ece412570606c2d3fcf7cd39c26812; path=/; secure; HttpOnly; SameSite=Strict",
      "Expires": "Thu, 19 Nov 1981 08:52:00 GMT",
      "Cache-Control": "no-cache, no-store",
      "Pragma": "no-cache",
      "SecurityCenter": "5.19.1",
      "Content-Length": "249",
      "Keep-Alive": "timeout=15, max=100",
      "Connection": "Keep-Alive",
      "Content-Type": "application/json"
    },
    "reason": "OK",
    "json_body": {
      "type": "regular",
      "response": {
        "usable": [
          {
            "id": "2",
            "name": "Server Down",
            "description": "",
            "status": "0"
          }
        ],
        "manageable": [
          {
            "id": "2",
            "name": "Server Down",
            "description": "",
            "status": "0"
          }
        ]
      },
      "error_code": 0,
      "error_msg": "",
      "warnings": [],
      "timestamp": 1713162689
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **type** (string)
  - **response** (object)
    - **usable** (array)
      - **id** (string)
      - **name** (string)
      - **description** (string)
      - **status** (string)
    - **manageable** (array)
      - **id** (string)
      - **name** (string)
      - **description** (string)
      - **status** (string)
  - **error_code** (number)
  - **error_msg** (string)
  - **warnings** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **timestamp** (number)
## Response Headers

| Header | Type |
|--------|------|
| Date | string |
| Server | string |
| X-Frame-Options | string |
| Content-Security-Policy | string |
| X-Content-Type-Options | string |
| X-XSS-Protection | string |
| Expect-CT | string |
| Strict-Transport-Security | string |
| Vary | string |
| Set-Cookie | string |
| Expires | string |
| Cache-Control | string |
| Pragma | string |
| SecurityCenter | string |
| Content-Length | string |
| Keep-Alive | string |
| Connection | string |
| Content-Type | string |