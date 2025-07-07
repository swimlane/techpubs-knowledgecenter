# Ping A Power Query

**Description**: Initiate a follow-up ping on a SentinelOne Deep Visibility Power Query using the provided queryId to check for results.

## Endpoint

- **URL:** `/web/api/v2.1/dv/events/pq-ping`
- **Method:** `GET`
## Inputs

- **paramaters** (object)
  - **queryId** (string): Query ID query param.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Server": "nginx",
      "Date": "Mon, 22 Apr 2024 09:18:00 GMT",
      "Content-Type": "application/json",
      "Content-Length": "94",
      "Connection": "keep-alive",
      "Access-Control-Allow-Origin": "https://cns.na1.sentinelone.net",
      "Access-Control-Allow-Credentials": "true",
      "Vary": "Origin",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
      "X-Frame-Options": "SAMEORIGIN",
      "X-Content-Type-Options": "nosniff",
      "Content-Security-Policy": "default-src 'self' ; connect-src 'self' *.sentinelone.net cdn.pendo.io app.pendo.io *.pendo.io data.pendo.io *.scalyr.com *.storage.googleapis.com sentry.io *.sentry.io *.google-analytics.com *.gstatic.com unpkg.com cdn.auth0.com wss://*.sentinelone.net https://www.googletagmanager.com https://cdnjs.cloudflare.com https://dm64t97qsxvuz.cloudfront.net data: ; script-src 'self' 'unsafe-inline' 'unsafe-eval' *.sentinelone.net cdn.pendo.io app.pendo.io pendo-io-static.storage.googleapis.com *.storage.googleapis.com data.pendo.io https://www.google-analytics.com https://www.googletagmanager.com https://unpkg.com https://cdnjs.cloudflare.com https://dm64t97qsxvuz.cloudfront.net ; img-src 'self' *.sentinelone.net *.sentinelone.com dm64t97qsxvuz.cloudfront.net data: https://www.google-analytics.com cdn.pendo.io app.pendo.io *.storage.googleapis.com data.pendo.io ; style-src 'self' 'unsafe-inline' *.sentinelone.net app.pendo.io cdn.pendo.io *.storage.googleapis.com https://cdnjs.cloudflare.com https://dm64t97qsxvuz.cloudfront.net ; font-src 'self' data: *.sentinelone.net https://cdn.auth0.com https://dm64t97qsxvuz.cloudfront.net ; manifest-src 'self' https://dm64t97qsxvuz.cloudfront.net ; frame-src 'self' blob: https://receptive.io https://*.pendo.io https://pendo-io-extensions.storage.googleapis.com/ https://*.youtube.com *.sentinelone.net *.scalyr.com; frame-ancestors 'self' app.pendo.io *.sentinelone.net; object-src 'none'"
    },
    "reason": "OK",
    "json_body": {
      "data": {
        "columns": [
          {
            "name": "eventTime",
            "type": "UNKNOWN"
          },
          {
            "name": "agentUuid",
            "type": "UNKNOWN"
          },
          {
            "name": "siteId",
            "type": "UNKNOWN"
          }
        ],
        "data": [],
        "externalId": "{\"lrqToken\":\"6b1f9a70-c32b-4758-af04-dd25b16d24a1\",\"target\":\"__E1__5eLScOxFsEPd7QExc0oKoc5paFNtW9zRk4wbhhgZKCI-\"}",
        "progress": 100,
        "queryId": "pq782813055dddb600360cf99d47d0c16f",
        "recommendations": [
          "Result set limited to 1000 rows by default. To display more rows, add a command like \"| limit 10000\"."
        ],
        "status": "FINISHED"
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
      - **name** (string)
      - **type** (string)
    - **data** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **externalId** (string)
    - **progress** (number)
    - **queryId** (string)
    - **recommendations** (array)
    - **status** (string)
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