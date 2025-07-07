# New Firewall Rule

**Description**: Create a SentinelOne Firewall Control rule to manage network traffic for defined scopes and OS, requiring a JSON body input.

## Endpoint

- **URL:** `web/api/v2.1/firewall-control`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required
  - **filter** (object)
    - **accountIds** (array)
    - **siteIds** (array)
    - **tenant** (boolean)
    - **groupIds** (array)
  - **data** (object)
    - **protocol** (string)
    - **application** (object)
      - **type** (string)
      - **values** (array)
    - **localHost** (object)
      - **type** (string)
      - **values** (array)
    - **remoteHost** (object)
      - **type** (string)
      - **values** (array)
    - **osTypes** (array)
    - **action** (string)
    - **localPort** (object)
      - **type** (string)
      - **values** (array)
    - **status** (string)
    - **remotePort** (object)
      - **type** (string)
      - **values** (array)
    - **osType** (string)
    - **location** (object)
      - **type** (string)
      - **values** (array)
        - **name** (string)
        - **id** (string)
    - **description** (string)
    - **direction** (string)
    - **remoteHosts** (array)
      - **type** (string)
      - **values** (array)
    - **tagIds** (array)
    - **tag** (string)
    - **name** (string)
## Output

### Example

```json
[
  {
    "status_code": 403,
    "response_headers": {
      "Server": "nginx",
      "Date": "Wed, 16 Nov 2022 17:50:40 GMT",
      "Content-Type": "application/json",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "Access-Control-Allow-Origin": "https://attivo-us.sentinelone.net",
      "Access-Control-Allow-Credentials": "true",
      "Vary": "Origin",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
      "X-Frame-Options": "SAMEORIGIN",
      "X-Content-Type-Options": "nosniff",
      "Content-Security-Policy": "default-src 'self' ; connect-src 'self' cdn.pendo.io app.pendo.io *.pendo.io data.pendo.io *.storage.googleapis.com sentry.io *.sentry.io *.google-analytics.com *.gstatic.com unpkg.com cdn.auth0.com wss://*.sentinelone.net https://www.googletagmanager.com https://cdnjs.cloudflare.com data: ; script-src 'self' 'unsafe-inline' 'unsafe-eval' cdn.pendo.io app.pendo.io pendo-io-static.storage.googleapis.com cdn.pendo.io *.storage.googleapis.com data.pendo.io https://www.google-analytics.com https://www.googletagmanager.com https://unpkg.com https://cdnjs.cloudflare.com ; img-src 'self' data: https://www.google-analytics.com cdn.pendo.io app.pendo.io *.sentinelone.com *.storage.googleapis.com data.pendo.io ; style-src 'self' 'unsafe-inline' app.pendo.io cdn.pendo.io *.storage.googleapis.com https://fonts.googleapis.com https://cdnjs.cloudflare.com ; font-src 'self' data: https://fonts.gstatic.com https://cdn.auth0.com ; frame-src 'self' blob: https://receptive.io https://*.pendo.io https://pendo-io-extensions.storage.googleapis.com/ https://*.youtube.com ; frame-ancestors 'self' app.pendo.io ; object-src 'none'",
      "Content-Encoding": "gzip"
    },
    "reason": "FORBIDDEN",
    "json_body": {
      "data": {
        "protocol": "string",
        "createdAt": "2018-02-27T04:49:26.257525Z",
        "location": {
          "type": "all",
          "values": [
            {
              "name": "office1",
              "scope": "global",
              "id": "225494730938493804"
            }
          ]
        },
        "tagIds": [
          "225494730938493804",
          "225494730938493915"
        ],
        "order": 0,
        "name": "string",
        "productId": "string",
        "creatorId": "225494730938493804",
        "updatedAt": "2018-02-27T04:49:26.257525Z",
        "ruleCategory": "firewall",
        "description": "string",
        "direction": "any",
        "localPort": {},
        "status": "Enabled",
        "scopeId": "225494730938493804",
        "id": "225494730938493804",
        "application": {},
        "creator": "string",
        "scope": "global",
        "osTypes": [
          "windows_legacy"
        ],
        "action": "Allow",
        "tags": [
          {
            "id": "225494730938493804",
            "name": "My Tag"
          }
        ],
        "remotePort": {},
        "editable": true,
        "osType": "windows_legacy",
        "remoteHost": {},
        "tagNames": [
          "string"
        ],
        "remoteHosts": [
          {
            "type": "any",
            "values": [
              "string"
            ]
          }
        ],
        "tag": "string",
        "localHost": {}
      }
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **data** (object)
    - **protocol** (string)
    - **createdAt** (string)
    - **location** (object)
      - **type** (string)
      - **values** (array)
        - **name** (string)
        - **scope** (string)
        - **id** (string)
    - **tagIds** (array)
    - **order** (number)
    - **name** (string)
    - **productId** (string)
    - **creatorId** (string)
    - **updatedAt** (string)
    - **ruleCategory** (string)
    - **description** (string)
    - **direction** (string)
    - **localPort** (object)
    - **status** (string)
    - **scopeId** (string)
    - **id** (string)
    - **application** (object)
    - **creator** (string)
    - **scope** (string)
    - **osTypes** (array)
    - **action** (string)
    - **tags** (array)
      - **id** (string)
      - **name** (string)
    - **remotePort** (object)
    - **editable** (boolean)
    - **osType** (string)
    - **remoteHost** (object)
    - **tagNames** (array)
    - **remoteHosts** (array)
      - **type** (string)
      - **values** (array)
    - **tag** (string)
    - **localHost** (object)
## Response Headers

| Header | Type |
|--------|------|
| Server | string |
| Date | string |
| Content-Type | string |
| Transfer-Encoding | string |
| Connection | string |
| Access-Control-Allow-Origin | string |
| Access-Control-Allow-Credentials | string |
| Vary | string |
| Strict-Transport-Security | string |
| X-Frame-Options | string |
| X-Content-Type-Options | string |
| Content-Security-Policy | string |
| Content-Encoding | string |