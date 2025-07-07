# Host - Update

**Description**: Updates an existing host in Check Point R80 using the provided unique identifier (UID).

## Endpoint

- **URL:** `/web_api/set-host`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required: JSON Body
  - **uid** (string) – Required: Unique Object Identifier
  - **new-name** (string): Object name. Must be unique in the domain
  - **ip-address** (string): IPv4 or IPv6 address. If both addresses are required use ipv4-address and ipv6-address fields explicitly
  - **color** (string): Color of the object. Must be one of aquamarine, black, blue, crete blue, burlywood, cyan, dark green, khaki, orchid, dark orange, dark sea green, pink, turquoise, dark blue, firebrick, brown, forest green, gold, dark gold, gray, dark gray, light green, lemon chiffon, coral, sea green, sky blue, magenta, purple, slate blue, violet red, navy blue, olive, orange, red, sienna, yellow
  - **tags** (array): Collection of tag identifiers
  - **comments** (string): Comment string
  - **groups** (object): Collection of group identifiers
    - **add** (array)
    - **remove** (array)
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Fri, 30 Dec 2022 18:33:42 GMT",
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
      "uid": "def1f565-7732-49e4-a766-c25e91629a26",
      "name": "Swimlane host 1",
      "type": "host",
      "domain": {
        "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
        "name": "SMC User",
        "domain-type": "domain"
      },
      "ipv4-address": "192.168.1.102",
      "interfaces": [],
      "nat-settings": {
        "auto-rule": false
      },
      "groups": [],
      "comments": "",
      "color": "light green",
      "icon": "Objects/host",
      "tags": [],
      "meta-info": {
        "lock": "unlocked",
        "validation-state": "ok",
        "last-modify-time": {
          "posix": 1672425222731,
          "iso-8601": "2022-12-30T11:33-0700"
        },
        "last-modifier": "admin",
        "creation-time": {
          "posix": 1672424949489,
          "iso-8601": "2022-12-30T11:29-0700"
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
  - **ipv4-address** (string)
  - **interfaces** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **nat-settings** (object)
    - **auto-rule** (boolean)
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