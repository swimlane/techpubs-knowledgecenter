# Download From Cloud

**Description**: Download a specific threat file from SentinelOne cloud using the provided unique threat ID.

## Endpoint

- **URL:** `/web/api/v2.1/threats/{{threat_id}}/download-from-cloud`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **threat_id** (string) – Required: Threat ID.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Server": "nginx",
      "Date": "Sun, 21 Apr 2024 17:19:47 GMT",
      "Content-Type": "application/json",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "X-RQID": "6774d02e-05e6-4a51-8c4c-168411f6fd66",
      "Access-Control-Allow-Origin": "https://cns.na1.sentinelone.net",
      "Access-Control-Allow-Credentials": "true",
      "Vary": "Origin",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
      "X-Frame-Options": "SAMEORIGIN",
      "X-Content-Type-Options": "nosniff",
      "Content-Security-Policy": "default-src 'self' ; connect-src 'self' *.sentinelone.net cdn.pendo.io app.pendo.io *.pendo.io data.pendo.io *.scalyr.com *.storage.googleapis.com sentry.io *.sentry.io *.google-analytics.com *.gstatic.com unpkg.com cdn.auth0.com wss://*.sentinelone.net https://www.googletagmanager.com https://cdnjs.cloudflare.com https://dm64t97qsxvuz.cloudfront.net data: ; script-src 'self' 'unsafe-inline' 'unsafe-eval' *.sentinelone.net cdn.pendo.io app.pendo.io pendo-io-static.storage.googleapis.com *.storage.googleapis.com data.pendo.io https://www.google-analytics.com https://www.googletagmanager.com https://unpkg.com https://cdnjs.cloudflare.com https://dm64t97qsxvuz.cloudfront.net ; img-src 'self' *.sentinelone.net *.sentinelone.com dm64t97qsxvuz.cloudfront.net data: https://www.google-analytics.com cdn.pendo.io app.pendo.io *.storage.googleapis.com data.pendo.io ; style-src 'self' 'unsafe-inline' *.sentinelone.net app.pendo.io cdn.pendo.io *.storage.googleapis.com https://cdnjs.cloudflare.com https://dm64t97qsxvuz.cloudfront.net ; font-src 'self' data: *.sentinelone.net https://cdn.auth0.com https://dm64t97qsxvuz.cloudfront.net ; manifest-src 'self' https://dm64t97qsxvuz.cloudfront.net ; frame-src 'self' blob: https://receptive.io https://*.pendo.io https://pendo-io-extensions.storage.googleapis.com/ https://*.youtube.com *.sentinelone.net *.scalyr.com; frame-ancestors 'self' app.pendo.io *.sentinelone.net; object-src 'none'",
      "Cache-Control": "no-store",
      "Pragma": "no-cache",
      "Expires": "-1",
      "Content-Encoding": "gzip"
    },
    "reason": "OK",
    "json_body": {
      "data": {
        "downloadUrl": "https://mgmt-file-upload-us-east-1-prod.sentinelone.net/proxy/mgmt-file-upload-us-east-1-prod-pub.s3.amazonaws.com/pe/malicious/ee24d1d448fffea3983da1a51ff4b2a37426a5651b9d93aee5959389de743f07?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIASLITH25O4VE2XETW%2F20240421%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240421T171947Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&response-content-disposition=filename%3Dee24d1d448fffea3983da1a51ff4b2a37426a5651b9d93aee5959389de743f07.zip&X-Amz-Signature=0fb5573e7c8fde16f7dcf011f84c3a222e1bcdf276c55389287d81f1d87d984e",
        "fileName": "ee24d1d448fffea3983da1a51ff4b2a37426a5651b9d93aee5959389de743f07"
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
    - **downloadUrl** (string)
    - **fileName** (string)
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