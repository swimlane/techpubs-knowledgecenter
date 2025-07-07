# Application Site Category - Create

**Description**: Creates a new application site category in Check Point R80 with the specified name.

## Endpoint

- **URL:** `/web_api/add-application-site-category`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required: JSON Body
  - **name** (string) – Required: Object name. Must be unique in the domain
  - **description** (string): Description
  - **tags** (string): Collection of tag identifiers
  - **color** (string): Color of the object. Must be one of aquamarine, black, blue, crete blue, burlywood, cyan, dark green, khaki, orchid, dark orange, dark sea green, pink, turquoise, dark blue, firebrick, brown, forest green, gold, dark gold, gray, dark gray, light green, lemon chiffon, coral, sea green, sky blue, magenta, purple, slate blue, violet red, navy blue, olive, orange, red, sienna, yellow
  - **comments** (string): Comments string
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Thu, 29 Dec 2022 21:06:40 GMT",
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
      "uid": "2d07d799-8007-4ff8-9833-f29b5b664a1d",
      "name": "Hernan app site category 1",
      "type": "application-site-category",
      "domain": {
        "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
        "name": "SMC User",
        "domain-type": "domain"
      },
      "description": "",
      "user-defined": true,
      "groups": [],
      "comments": "",
      "color": "aquamarine",
      "icon": "Objects/category",
      "tags": [],
      "meta-info": {
        "lock": "unlocked",
        "validation-state": "ok",
        "last-modify-time": {
          "posix": 1672347999917,
          "iso-8601": "2022-12-29T14:06-0700"
        },
        "last-modifier": "admin",
        "creation-time": {
          "posix": 1672347999917,
          "iso-8601": "2022-12-29T14:06-0700"
        },
        "creator": "admin"
      },
      "read-only": true
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
  - **description** (string)
  - **user-defined** (boolean)
  - **groups** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **comments** (string)
  - **color** (string)
  - **icon** (string)
  - **tags** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
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