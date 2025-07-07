# Access Layer - Update

**Description**: Updates an existing access layer in Check Point R80 by utilizing the provided unique identifier (UID).

## Endpoint

- **URL:** `/web_api/set-access-layer`
- **Method:** `POST`
## Inputs

- **json_body** (object): JSON Body
  - **uid** (string) – Required: Object's unique identifier
  - **applications-and-url-filtering** (boolean): Whether to enable Applications & URL Filtering blade on the layer
  - **content-awareness** (boolean): Whether to enable Content Awareness blade on the layer
  - **detect-using-x-forward-for** (boolean): Whether to use X-Forward-For HTTP header, which is added by the proxy server to keep track of the original source IP
  - **firewall** (boolean): Whether to enable Firewall blade on the layer
  - **implicit-cleanup-action** (string): The default "catch-all" action for traffic that does not match any explicit or implied rules in the layer. Valid values are "drop" or "accept"
  - **mobile-access** (boolean): Whether to enable Mobile Access blade on the layer
  - **shared** (boolean): Whether this layer is shared
  - **tags** (array): Collection of tag identifiers
  - **color** (string): Color of the object. Should be one of aquamarine, black, blue, crete blue, burlywood, cyan, dark green, khaki, orchid, dark orange, dark sea green, pink, turquoise, dark blue, firebrick, brown, forest green, gold, dark gold, gray, dark gray, light green, lemon chiffon, coral, sea green, sky blue, magenta, purple, slate blue, violet red, navy blue, olive, orange, red, sienna, yellow
  - **comments** (string): Comments string
  - **details-level** (string): The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object. Valid values are "uid", "standard", "full"
  - **ignore-warnings** (boolean): Apply changes ignoring warnings
  - **ignore-errors** (boolean): Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored
## Output

### Example

```json
[
  {
    "status_code": 409,
    "response_headers": {
      "Date": "Tue, 27 Dec 2022 15:53:31 GMT",
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
    "reason": "Conflict",
    "json_body": {
      "code": "generic_err_object_locked",
      "message": "Requested object with ObjId: [a40b877c-b723-4b0b-ac91-cab00bb40f06] name: [null] locked: [Locked for editing by admin]"
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **code** (string)
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