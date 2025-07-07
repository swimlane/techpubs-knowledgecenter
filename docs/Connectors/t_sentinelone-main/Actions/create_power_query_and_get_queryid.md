# Create Power Query And Get Query ID

**Description**: Executes a Deep Visibility Power Query in SentinelOne, providing an initial status and a unique query ID for result retrieval. Requires fromDate, query, and toDate.

## Endpoint

- **URL:** `/web/api/v2.1/dv/events/pq`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required
  - **query** (string) – Required: Events matching the query search term will be returned.
  - **accountIds** (string): List of Account IDs to filter by.
  - **siteIds** (string): List of Site IDs to filter by.
  - **toDate** (string) – Required: Events created before or at this timestamp.
  - **limit** (number): Limit number of returned items (1-100000).
  - **fromDate** (string) – Required: Events created after this timestamp.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Server": "nginx",
      "Date": "Mon, 22 Apr 2024 08:49:49 GMT",
      "Content-Type": "application/json",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "X-RQID": "32b46d87-e912-4ed0-9012-4e617cc9a015",
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
        "columns": [],
        "data": [],
        "externalId": "{\"lrqToken\":\"074fcc66-9839-4209-a3e1-55252dc2f1c0\",\"target\":\"__E1__5eLScOxFsEPd7QExc0oKoVNPCQTtst5BSh8h7KH9lDo-\"}",
        "progress": 78,
        "queryId": "pqb57dd8d151c08304b0e56ec8b7d30b24",
        "recommendations": [],
        "status": "RUNNING"
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
    - **columns** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **data** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **externalId** (string)
    - **progress** (number)
    - **queryId** (string)
    - **recommendations** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **status** (string)
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