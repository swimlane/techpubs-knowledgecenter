# Get User

**Description**: Retrieves detailed properties and relationships of a user in Azure Active Directory using their unique ID.

## Endpoint

- **URL:** `/v1.0/users/{{id}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **id** (string) – Required
- **parameters** (object)
  - **$select** (string): Filters properties (columns).
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Wed, 23 Aug 2023 13:20:02 GMT",
      "Content-Type": "text/html; charset=utf-8",
      "Content-Length": "16595",
      "Connection": "keep-alive",
      "Cache-Control": "public, stale-while-revalidate=900, max-age=900",
      "Content-Encoding": "gzip",
      "Expires": "Wed, 23 Aug 2023 13:26:00 GMT",
      "Last-Modified": "Wed, 23 Aug 2023 13:08:00 GMT",
      "ETag": "\"WHuRpQeAYNiY\"",
      "Vary": "Accept-Encoding, host",
      "x-content-type-options": "nosniff",
      "X-XSS-Protection": "1; mode=block",
      "x-ms-version": "12.43.4.1 (v12.42.0.1#162d343f82.230814-2250) Signed",
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
      "x-azure-ref": "20230823T132002Z-5u109qe2td3xf64dz2k6r7keq00000000c4000000000ydtx",
      "X-Cache": "TCP_HIT",
      "Accept-Ranges": "bytes"
    },
    "reason": "OK",
    "response_text": {
      "businessPhones": [
        "+1 425 555 0109"
      ],
      "displayName": "Adele Vance",
      "givenName": "Adele",
      "jobTitle": "Retail Manager",
      "mail": "AdeleV@contoso.onmicrosoft.com",
      "mobilePhone": "+1 425 555 0109",
      "officeLocation": "18/2111",
      "preferredLanguage": "en-US",
      "surname": "Vance",
      "userPrincipalName": "AdeleV@contoso.onmicrosoft.com",
      "id": "87d349ed-44d7-43e1-9a83-5f2406dee5bd"
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **response_text** (object)
  - **businessPhones** (array)
  - **displayName** (string)
  - **givenName** (string)
  - **jobTitle** (string)
  - **mail** (string)
  - **mobilePhone** (string)
  - **officeLocation** (string)
  - **preferredLanguage** (string)
  - **surname** (string)
  - **userPrincipalName** (string)
  - **id** (string)
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