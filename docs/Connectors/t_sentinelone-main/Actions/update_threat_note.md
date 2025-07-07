# Update Threat Note

**Description**: Updates a specific threat note in SentinelOne using threat_id and note_id with provided data content.

## Endpoint

- **URL:** `web/api/v2.1/threats/{{threat_id}}/notes/{{note_id}}`
- **Method:** `PUT`
## Inputs

- **path_parameters** (object) – Required
  - **threat_id** (string) – Required
  - **note_id** (string) – Required
- **json_body** (object) – Required
  - **data** (object) – Required
    - **text** (string) – Required
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Server": "nginx",
      "Date": "Wed, 16 Nov 2022 14:40:53 GMT",
      "Content-Type": "application/json",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "X-RQID": "83d1f963-2f8f-4f59-86dc-29b6bba6c497",
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
        "createdAt": "2022-11-14T21:12:44.060516Z",
        "edited": true,
        "id": "1553834980127175650",
        "text": "this is a text",
        "updatedAt": "2022-11-16T14:40:53.549560Z"
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
    - **createdAt** (string)
    - **edited** (boolean)
    - **id** (string)
    - **text** (string)
    - **updatedAt** (string)
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