# Network - Create

**Description**: Creates a new network object in Check Point R80 using the provided name, subnet, and subnet mask.

## Endpoint

- **URL:** `/web_api/add-network`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required: JSON Body
  - **name** (string) – Required: Object name. Must be unique in the domain
  - **subnet-mask** (string) – Required: IPv4 network mask
  - **subnet** (string) – Required: IPv4 or IPv6 network address. If both addresses are required use subnet4 and subnet6 fields explicitly
  - **tags** (array): Collection of tag identifiers
  - **color** (string): Color of the object. Must be one of aquamarine, black, blue, crete blue, burlywood, cyan, dark green, khaki, orchid, dark orange, dark sea green, pink, turquoise, dark blue, firebrick, brown, forest green, gold, dark gold, gray, dark gray, light green, lemon chiffon, coral, sea green, sky blue, magenta, purple, slate blue, violet red, navy blue, olive, orange, red, sienna, yellow
  - **comments** (string): Comment string
  - **groups** (array): Collection of group identifiers
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Fri, 30 Dec 2022 19:29:11 GMT",
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
      "uid": "a11b304a-5465-44cc-b030-eb8684c74e62",
      "name": "Swimlane Network 1",
      "type": "network",
      "domain": {
        "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
        "name": "SMC User",
        "domain-type": "domain"
      },
      "broadcast": "allow",
      "subnet4": "192.0.2.0",
      "mask-length4": 24,
      "subnet-mask": "255.255.255.0",
      "nat-settings": {
        "auto-rule": false
      },
      "groups": [],
      "comments": "",
      "color": "light green",
      "icon": "NetworkObjects/network",
      "tags": [],
      "meta-info": {
        "lock": "unlocked",
        "validation-state": "ok",
        "last-modify-time": {
          "posix": 1672428551149,
          "iso-8601": "2022-12-30T12:29-0700"
        },
        "last-modifier": "admin",
        "creation-time": {
          "posix": 1672428551149,
          "iso-8601": "2022-12-30T12:29-0700"
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
  - **broadcast** (string)
  - **subnet4** (string)
  - **mask-length4** (number)
  - **subnet-mask** (string)
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