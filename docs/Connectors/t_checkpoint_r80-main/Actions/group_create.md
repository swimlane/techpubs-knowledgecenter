# Group - Create

**Description**: Creates a new group in Check Point R80 using the specified name from the JSON body input.

## Endpoint

- **URL:** `/web_api/add-group`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required: JSON Body
  - **name** (string) – Required: Object name. Must be unique in the domain
  - **members** (array): Collection of Network objects identified by the name or UID
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
      "Date": "Fri, 30 Dec 2022 16:58:04 GMT",
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
      "uid": "0897ebc6-7f8b-4019-96b9-0efef1cc1d0a",
      "name": "Swimlane group 1",
      "type": "group",
      "domain": {
        "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
        "name": "SMC User",
        "domain-type": "domain"
      },
      "members": [
        {
          "uid": "5ccebaae-2138-41ff-bddf-442ce62f2442",
          "name": "1.1.1.1",
          "type": "host",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          },
          "ipv4-address": "1.1.1.1"
        },
        {
          "uid": "c9869133-4ff0-4fe4-a072-bcec7162073d",
          "name": "1.2.3.4",
          "type": "host",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          },
          "ipv4-address": "1.2.3.4"
        }
      ],
      "groups": [],
      "comments": "",
      "color": "cyan",
      "icon": "General/group",
      "tags": [],
      "meta-info": {
        "lock": "unlocked",
        "validation-state": "ok",
        "last-modify-time": {
          "posix": 1672419484547,
          "iso-8601": "2022-12-30T09:58-0700"
        },
        "last-modifier": "admin",
        "creation-time": {
          "posix": 1672419484547,
          "iso-8601": "2022-12-30T09:58-0700"
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
  - **members** (array)
    - **uid** (string)
    - **name** (string)
    - **type** (string)
    - **domain** (object)
      - **uid** (string)
      - **name** (string)
      - **domain-type** (string)
    - **ipv4-address** (string)
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