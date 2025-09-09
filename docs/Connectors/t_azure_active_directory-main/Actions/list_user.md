# List User

**Description**: Retrieve a comprehensive list of user objects from Azure Active Directory, including names and roles.

## Endpoint

- **URL:** `/v1.0/users`
- **Method:** `GET`
## Inputs

- **parameters** (object)
  - **$count** (string): Retrieves the total count of matching resources.
  - **$expand** (string): Retrieves related resources.
  - **$filter** (string): Use the `filter` query parameter to retrieve just a subset of a collection. For guidance on using `filter`, see https://learn.microsoft.com/en-us/graph/filter-query-parameter.
  - **$orderby** (string): Orders results.
  - **$search** (string): Returns results based on search criteria.
  - **$select** (string): Filters properties (columns).
  - **$top** (number): Sets the page size of results.
- **headers** (object)
  - **ConsistencyLevel** (string): This header and $count are required when using $search, or in specific usage of $filter.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Wed, 23 Aug 2023 13:46:59 GMT",
      "Content-Type": "text/html; charset=utf-8",
      "Content-Length": "16609",
      "Connection": "keep-alive",
      "Cache-Control": "public, stale-while-revalidate=900, max-age=900",
      "Content-Encoding": "gzip",
      "Expires": "Wed, 23 Aug 2023 13:41:00 GMT",
      "Last-Modified": "Wed, 23 Aug 2023 13:23:00 GMT",
      "ETag": "\"SovJwPdQDurP\"",
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
      "x-azure-ref": "20230823T134659Z-yv6774vfkd39t3p2zw0xbwzk4c00000000n000000001758a",
      "X-Cache": "TCP_HIT",
      "Accept-Ranges": "bytes"
    },
    "reason": "OK",
    "response_text": [
      {
        "businessPhones": [],
        "displayName": "Conf Room Adams",
        "givenName": null,
        "jobTitle": null,
        "mail": "Adams@contoso.com",
        "mobilePhone": null,
        "officeLocation": null,
        "preferredLanguage": null,
        "surname": null,
        "userPrincipalName": "Adams@contoso.com",
        "id": "6ea91a8d-e32e-41a1-b7bd-d2d185eed0e0"
      },
      {
        "businessPhones": [
          "425-555-0100"
        ],
        "displayName": "MOD Administrator",
        "givenName": "MOD",
        "jobTitle": null,
        "mail": null,
        "mobilePhone": "425-555-0101",
        "officeLocation": null,
        "preferredLanguage": "en-US",
        "surname": "Administrator",
        "userPrincipalName": "admin@contoso.com",
        "id": "4562bcc8-c436-4f95-b7c0-4f8ce89dca5e"
      }
    ]
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **response_text** (array)
  - **businessPhones** (array)
  - **displayName** (string)
  - **givenName** (string)
  - **jobTitle** (object)
  - **mail** (object)
  - **mobilePhone** (string)
  - **officeLocation** (object)
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