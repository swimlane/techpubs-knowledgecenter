# Host - Delete

**Description**: Removes an existing host object from Check Point R80 by its name or UID.

## Endpoint

- **URL:** `/web_api/delete-host`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required
  - **uid** (string): Object unique identifier.
  - **name** (string): Object name.
  - **details-level** (string): The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.
  - **ignore-warnings** (boolean): Apply changes ignoring warnings. Default value is false.
  - **ignore-errors** (boolean): Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored. Default value is false.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Fri, 30 Dec 2022 18:36:24 GMT",
      "Server": "CPWS",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
      "X-Frame-Options": "SAMEORIGIN",
      "Content-Type": "application/json",
      "X-UA-Compatible": "IE=EmulateIE8",
      "X-Forwarded-Host-Port": "443",
      "Keep-Alive": "timeout=15, max=99",
      "Connection": "Keep-Alive",
      "Transfer-Encoding": "chunked"
    },
    "reason": "OK",
    "json_body": {
      "message": "OK"
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **message** (string)
## Response Headers

| Header | Type |
|--------|------|
| Date | string |
| Server | string |
| Strict-Transport-Security | string |
| X-Frame-Options | string |
| Content-Type | string |
| X-UA-Compatible | string |
| X-Forwarded-Host-Port | string |
| Keep-Alive | string |
| Connection | string |
| Transfer-Encoding | string |