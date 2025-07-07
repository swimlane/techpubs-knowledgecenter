# Domain - Update

**Description**: Updates a specified domain in Check Point R80 using the provided UID. Ensure to include UID in the JSON body.

## Endpoint

- **URL:** `/web_api/set-dns-domain`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required: JSON Body
  - **uid** (string) – Required: Unique Object Identifier
  - **new-name** (string): DNS domain name. Should always start with a '.' character. Should be unique in the domain
  - **is-sub-domain** (boolean): Whether to match sub-domains in addition to the domain itself
  - **tags** (array): Collection of tag identifiers
  - **color** (string): Color of the object. Must be one of aquamarine, black, blue, crete blue, burlywood, cyan, dark green, khaki, orchid, dark orange, dark sea green, pink, turquoise, dark blue, firebrick, brown, forest green, gold, dark gold, gray, dark gray, light green, lemon chiffon, coral, sea green, sky blue, magenta, purple, slate blue, violet red, navy blue, olive, orange, red, sienna, yellow
  - **comments** (string): Comments string
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Fri, 30 Dec 2022 15:44:32 GMT",
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
      "uid": "540cbca6-4310-4d20-8b71-9dc24dc669a6",
      "name": ".269a0d7638494a48ba4f14a467532a41",
      "type": "dns-domain",
      "domain": {
        "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
        "name": "SMC User",
        "domain-type": "domain"
      },
      "is-sub-domain": false,
      "comments": "",
      "color": "blue",
      "icon": "Objects/domain",
      "tags": [
        {
          "uid": "f79739be-99c5-4b2e-affe-cc74b262ad9e",
          "name": "Example tag",
          "type": "tag",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        }
      ],
      "meta-info": {
        "lock": "locked by current session",
        "validation-state": "ok",
        "last-modify-time": {
          "posix": 1631552270100,
          "iso-8601": "2021-09-13T10:57-0600"
        },
        "last-modifier": "admin",
        "creation-time": {
          "posix": 1631551342883,
          "iso-8601": "2021-09-13T10:42-0600"
        },
        "creator": "admin"
      },
      "read-only": false
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **uid** (string)
  - **name** (string)
  - **type** (string)
  - **domain** (object)
    - **uid** (string)
    - **name** (string)
    - **domain-type** (string)
  - **is-sub-domain** (boolean)
  - **comments** (string)
  - **color** (string)
  - **icon** (string)
  - **tags** (array)
    - **uid** (string)
    - **name** (string)
    - **type** (string)
    - **domain** (object)
      - **uid** (string)
      - **name** (string)
      - **domain-type** (string)
  - **meta-info** (object)
    - **lock** (string)
    - **validation-state** (string)
    - **last-modify-time** (object)
      - **posix** (number)
      - **iso-8601** (string)
    - **last-modifier** (string)
    - **creation-time** (object)
      - **posix** (number)
      - **iso-8601** (string)
    - **creator** (string)
  - **read-only** (boolean)
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