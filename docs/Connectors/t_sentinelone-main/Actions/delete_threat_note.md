# Delete Threat Note

**Description**: Removes a specific note from a threat within SentinelOne using provided threat and note IDs.

## Endpoint

- **URL:** `web/api/v2.1/threats/{{threat_id}}/notes/{{note_id}}`
- **Method:** `DELETE`
## Inputs

- **path_parameters** (object) – Required
  - **threat_id** (string) – Required
  - **note_id** (string) – Required
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Server": "nginx",
      "Date": "Wed, 16 Nov 2022 14:50:43 GMT",
      "Content-Type": "application/json",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "X-RQID": "d005d0b4-d6c5-43f2-9a96-25ce505a3c7c",
      "Access-Control-Allow-Origin": "https://attivo-us.sentinelone.net",
      "Access-Control-Allow-Credentials": "true",
      "Vary": "Origin",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
      "X-Frame-Options": "SAMEORIGIN",
      "X-Content-Type-Options": "nosniff",
      "Content-Security-Policy": "default-src 'self' ; connect-src 'self' cdn.pendo.io app.pendo.io *.pendo.io data.pendo.io *.storage.googleapis.com sentry.io *.sentry.io *.google-analytics.com *.gstatic.com unpkg.com cdn.auth0.com wss://*.sentinelone.net https://www.googletagmanager.com https://cdnjs.cloudflare.com data: ; script-src 'self' 'unsafe-inline' 'unsafe-eval' cdn.pendo.io app.pendo.io pendo-io-static.storage.googleapis.com cdn.pendo.io *.storage.googleapis.com data.pendo.io https://www.google-analytics.com https://www.googletagmanager.com https://unpkg.com https://cdnjs.cloudflare.com ; img-src 'self' data: https://www.google-analytics.com cdn.pendo.io app.pendo.io *.sentinelone.com *.storage.googleapis.com data.pendo.io ; style-src 'self' 'unsafe-inline' app.pendo.io cdn.pendo.io *.storage.googleapis.com https://fonts.googleapis.com https://cdnjs.cloudflare.com ; font-src 'self' data: https://fonts.gstatic.com https://cdn.auth0.com ; frame-src 'self' blob: https://receptive.io https://*.pendo.io https://pendo-io-extensions.storage.googleapis.com/ https://*.youtube.com ; frame-ancestors 'self' app.pendo.io ; object-src 'none'",
      "Cache-Control": "no-store",
      "Pragma": "no-cache",
      "Expires": "-1",
      "Content-Encoding": "gzip"
    },
    "reason": "OK",
    "json_body": {
      "data": {
        "success": true
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
    - **success** (boolean)
## Response Headers

| Header | Type |
|--------|------|
| Server | string |
| Date | string |
| Content-Type | string |
| Transfer-Encoding | string |
| Connection | string |
| X-RQID | string |
| Access-Control-Allow-Origin | string |
| Access-Control-Allow-Credentials | string |
| Vary | string |
| Strict-Transport-Security | string |
| X-Frame-Options | string |
| X-Content-Type-Options | string |
| Content-Security-Policy | string |
| Cache-Control | string |
| Pragma | string |
| Expires | string |
| Content-Encoding | string |