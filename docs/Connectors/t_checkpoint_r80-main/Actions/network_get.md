# Network - Get

**Description**: Retrieves details of a specific network from Check Point R80 using the provided unique identifier (UID).

## Endpoint

- **URL:** `/web_api/show-network`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required: JSON Body
  - **uid** (string) – Required: Unique Object Identifier
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Fri, 30 Dec 2022 19:19:19 GMT",
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
      "uid": "4f078348-5f64-45a2-b501-944b78511eba",
      "name": "22def595c2a64f8f976461beff69da69",
      "type": "network",
      "domain": {
        "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
        "name": "SMC User",
        "domain-type": "domain"
      },
      "broadcast": "allow",
      "subnet4": "192.168.1.0",
      "mask-length4": 24,
      "subnet-mask": "255.255.255.0",
      "nat-settings": {
        "auto-rule": false
      },
      "groups": [
        {
          "uid": "90d0997c-30a2-4ab3-b4f3-549da3c9ae39",
          "name": "10a4b9b7aaae469783c0b4c78b637dbc",
          "type": "group",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        }
      ],
      "comments": "An example comment",
      "color": "blue",
      "icon": "NetworkObjects/network",
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
          "posix": 1631573399886,
          "iso-8601": "2021-09-13T16:49-0600"
        },
        "last-modifier": "admin",
        "creation-time": {
          "posix": 1631573399886,
          "iso-8601": "2021-09-13T16:49-0600"
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
  - **broadcast** (string)
  - **subnet4** (string)
  - **mask-length4** (number)
  - **subnet-mask** (string)
  - **nat-settings** (object)
    - **auto-rule** (boolean)
  - **groups** (array)
    - **uid** (string)
    - **name** (string)
    - **type** (string)
    - **domain** (object)
      - **uid** (string)
      - **name** (string)
      - **domain-type** (string)
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