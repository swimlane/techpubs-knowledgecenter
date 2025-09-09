# Create User

**Description**: Creates a new user object in Azure Active Directory, including all necessary attributes.

## Endpoint

- **URL:** `/v1.0/users`
- **Method:** `POST`
## Inputs

- **json_body** (object)
  - **accountEnabled** (boolean)
  - **displayName** (string)
  - **onPremisesImmutableId** (string)
  - **mailNickname** (string)
  - **userPrincipalName** (string)
  - **passwordProfile** (object)
    - **forceChangePasswordNextSignIn** (boolean)
    - **forceChangePasswordNextSignInWithMfa** (boolean)
    - **password** (string)
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Fri, 18 Aug 2023 11:21:47 GMT",
      "Content-Type": "text/html; charset=utf-8",
      "Content-Length": "16586",
      "Connection": "keep-alive",
      "Cache-Control": "public, stale-while-revalidate=900, max-age=900",
      "Content-Encoding": "gzip",
      "Expires": "Fri, 18 Aug 2023 11:13:00 GMT",
      "Last-Modified": "Fri, 18 Aug 2023 10:55:00 GMT",
      "ETag": "\"Q5cbyW9tOsWs\"",
      "Vary": "Accept-Encoding, host",
      "x-content-type-options": "nosniff",
      "X-XSS-Protection": "1; mode=block",
      "x-ms-version": "12.43.2.1 (v12.42.0.1#6c4023fb99.230803-0127) Signed",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
      "nel": "{\"report_to\":\"network-errors\",\"max_age\":86400,\"success_fraction\":0.001,\"failure_fraction\":1.0}",
      "report-to": "{\"group\":\"network-errors\",\"max_age\":86400,\"endpoints\":[{\"url\":\"https://eafc.nelreports.net/api/report?cat=aportal\"}]}",
      "Content-Security-Policy": "frame-ancestors 'self'",
      "X-Frame-Options": "SAMEORIGIN",
      "Access-Control-Allow-Origin": "*",
      "Timing-Allow-Origin": "*",
      "x-ms-content-source": "DiskPersistentContentCache",
      "Referrer-Policy": "strict-origin-when-cross-origin",
      "Permissions-Policy": "accelerometer=(), ambient-light-sensor=(), battery=(), camera=(), gyroscope=(), magnetometer=(), screen-wake-lock=()",
      "X-UA-Compatible": "IE=edge",
      "x-azure-ref": "20230818T112147Z-01cdhmnvkd2gf03bhy2330g8u000000002vg0000000220k1",
      "X-Cache": "TCP_HIT",
      "Accept-Ranges": "bytes"
    },
    "reason": "OK",
    "response_text": ""
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **response_text** (string)
## Response Headers

| Header | Type |
|--------|------|
| Date | string |
| Content-Type | string |
| Content-Length | string |
| Connection | string |
| Cache-Control | string |
| Content-Encoding | string |
| Expires | string |
| Last-Modified | string |
| ETag | string |
| Vary | string |
| x-content-type-options | string |
| X-XSS-Protection | string |
| x-ms-version | string |
| Strict-Transport-Security | string |
| nel | string |
| report-to | string |
| Content-Security-Policy | string |
| X-Frame-Options | string |
| Access-Control-Allow-Origin | string |
| Timing-Allow-Origin | string |
| x-ms-content-source | string |
| Referrer-Policy | string |
| Permissions-Policy | string |
| X-UA-Compatible | string |
| x-azure-ref | string |
| X-Cache | string |
| Accept-Ranges | string |