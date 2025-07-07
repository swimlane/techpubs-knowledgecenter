# Group - Get

**Description**: Retrieves details for a specified group in Check Point R80 using the unique identifier (UID) provided.

## Endpoint

- **URL:** `/web_api/show-group`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required: JSON Body
  - **uid** (string) – Required: Unique Object Identifier
  - **show-as-ranges** (boolean): When true, the group's matched content is displayed as ranges of IP addresses rather than network objects
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Fri, 30 Dec 2022 16:33:40 GMT",
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
      "uid": "b92f7002-60dc-49bf-9b96-3e3367068687",
      "name": "01138b85ae344cd5b6a07c82971bd7e6",
      "type": "group",
      "domain": {
        "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
        "name": "SMC User",
        "domain-type": "domain"
      },
      "members": [
        {
          "uid": "4c82e477-ea87-4bb8-8180-d5345522a57a",
          "name": "CP_default_Office_Mode_addresses_pool",
          "type": "network",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          },
          "subnet4": "172.16.10.0",
          "mask-length4": 24,
          "subnet-mask": "255.255.255.0"
        }
      ],
      "groups": [],
      "comments": "An example comment",
      "color": "blue",
      "icon": "General/group",
      "tags": [
        {
          "uid": "13ad28d0-b35c-44ca-af44-7b577ba66d0f",
          "name": "tag one",
          "type": "tag",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "bef0e53e-eec4-48f3-bc35-2ebb541735a9",
          "name": "tag two",
          "type": "tag",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        }
      ],
      "meta-info": {
        "lock": "unlocked",
        "validation-state": "ok",
        "last-modify-time": {
          "posix": 1631645349963,
          "iso-8601": "2021-09-14T12:49-0600"
        },
        "last-modifier": "admin",
        "creation-time": {
          "posix": 1631645349963,
          "iso-8601": "2021-09-14T12:49-0600"
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
  - **members** (array)
    - **uid** (string)
    - **name** (string)
    - **type** (string)
    - **domain** (object)
      - **uid** (string)
      - **name** (string)
      - **domain-type** (string)
    - **subnet4** (string)
    - **mask-length4** (number)
    - **subnet-mask** (string)
  - **groups** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
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