# Host - Get

**Description**: Retrieves details of a specific host from Check Point R80 using the provided unique identifier (UID).

## Endpoint

- **URL:** `/web_api/show-host`
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
      "Date": "Fri, 30 Dec 2022 18:04:30 GMT",
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
      "uid": "5ccebaae-2138-41ff-bddf-442ce62f2442",
      "name": "1.1.1.1",
      "type": "host",
      "domain": {
        "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
        "name": "SMC User",
        "domain-type": "domain"
      },
      "ipv4-address": "1.1.1.1",
      "interfaces": [],
      "nat-settings": {
        "auto-rule": false
      },
      "groups": [],
      "comments": "",
      "color": "black",
      "icon": "Objects/host",
      "tags": [],
      "meta-info": {
        "lock": "unlocked",
        "validation-state": "ok",
        "last-modify-time": {
          "posix": 1596567905724,
          "iso-8601": "2020-08-04T13:05-0600"
        },
        "last-modifier": "admin",
        "creation-time": {
          "posix": 1596567905724,
          "iso-8601": "2020-08-04T13:05-0600"
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