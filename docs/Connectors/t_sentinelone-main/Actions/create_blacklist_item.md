# Create Blacklist Item

**Description**: Creates a blacklist item in SentinelOne with a SHA1 hash to specify scope filters for targeted protection.

## Endpoint

- **URL:** `web/api/v2.1/restrictions`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required
  - **filter** (object)
    - **tenant** (boolean)
    - **siteIds** (array)
  - **data** (object) – Required
    - **osType** (string) – Required
    - **type** (string) – Required
    - **description** (string)
    - **value** (string) – Required
    - **source** (string)
## Output

### Example

```json
[
  {
    "status_code": 400,
    "response_headers": {
      "Server": "nginx",
      "Date": "Wed, 16 Nov 2022 18:21:30 GMT",
      "Content-Type": "application/json",
      "Content-Length": "152",
      "Connection": "keep-alive",
      "Access-Control-Allow-Origin": "https://attivo-us.sentinelone.net",
      "Access-Control-Allow-Credentials": "true",
      "Vary": "Origin",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
      "X-Frame-Options": "SAMEORIGIN",
      "X-Content-Type-Options": "nosniff",
      "Content-Security-Policy": "default-src 'self' ; connect-src 'self' cdn.pendo.io app.pendo.io *.pendo.io data.pendo.io *.storage.googleapis.com sentry.io *.sentry.io *.google-analytics.com *.gstatic.com unpkg.com cdn.auth0.com wss://*.sentinelone.net https://www.googletagmanager.com https://cdnjs.cloudflare.com data: ; script-src 'self' 'unsafe-inline' 'unsafe-eval' cdn.pendo.io app.pendo.io pendo-io-static.storage.googleapis.com cdn.pendo.io *.storage.googleapis.com data.pendo.io https://www.google-analytics.com https://www.googletagmanager.com https://unpkg.com https://cdnjs.cloudflare.com ; img-src 'self' data: https://www.google-analytics.com cdn.pendo.io app.pendo.io *.sentinelone.com *.storage.googleapis.com data.pendo.io ; style-src 'self' 'unsafe-inline' app.pendo.io cdn.pendo.io *.storage.googleapis.com https://fonts.googleapis.com https://cdnjs.cloudflare.com ; font-src 'self' data: https://fonts.gstatic.com https://cdn.auth0.com ; frame-src 'self' blob: https://receptive.io https://*.pendo.io https://pendo-io-extensions.storage.googleapis.com/ https://*.youtube.com ; frame-ancestors 'self' app.pendo.io ; object-src 'none'"
    },
    "reason": "OK",
    "json_body": {
      "errors": [],
      "data": [
        {
          "scope": {
            "siteIds": [
              "225494730938493804"
            ],
            "tenant": true,
            "groupIds": [
              "225494730938493804"
            ],
            "accountIds": [
              "225494730938493804"
            ]
          },
          "userName": "string",
          "userId": "225494730938493804",
          "updatedAt": "2018-02-27T04:49:26.257525Z",
          "createdAt": "2018-02-27T04:49:26.257525Z",
          "notRecommended": "string",
          "osType": "windows_legacy",
          "source": "user",
          "description": "string",
          "value": "string",
          "type": "string",
          "scopeName": "string",
          "id": "225494730938493804"
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
  - **errors** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **data** (array)
    - **scope** (object)
      - **siteIds** (array)
      - **tenant** (boolean)
      - **groupIds** (array)
      - **accountIds** (array)
    - **userName** (string)
    - **userId** (string)
    - **updatedAt** (string)
    - **createdAt** (string)
    - **notRecommended** (string)
    - **osType** (string)
    - **source** (string)
    - **description** (string)
    - **value** (string)
    - **type** (string)
    - **scopeName** (string)
    - **id** (string)
## Response Headers

| Header | Type |
|--------|------|
| Server | string |
| Date | string |
| Content-Type | string |
| Content-Length | string |
| Connection | string |
| Access-Control-Allow-Origin | string |
| Access-Control-Allow-Credentials | string |
| Vary | string |
| Strict-Transport-Security | string |
| X-Frame-Options | string |
| X-Content-Type-Options | string |
| Content-Security-Policy | string |