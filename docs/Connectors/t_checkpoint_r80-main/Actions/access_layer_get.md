# Access Layer - Get

**Description**: Retrieve details of a specific access layer in Check Point R80 using the unique identifier (UID).

## Endpoint

- **URL:** `/web_api/show-access-layer`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required: JSON Body
  - **uid** (string) – Required: Object Unique Identifier
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Tue, 27 Dec 2022 13:16:19 GMT",
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
      "uid": "ed5316fb-8b21-4dc8-a30e-ad438434b605",
      "name": "19380cbe20c24459836e29ccfb846582",
      "type": "access-layer",
      "domain": {
        "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
        "name": "SMC User",
        "domain-type": "domain"
      },
      "shared": false,
      "applications-and-url-filtering": false,
      "content-awareness": false,
      "mobile-access": false,
      "firewall": true,
      "implicit-cleanup-action": "drop",
      "comments": "",
      "color": "black",
      "icon": "ApplicationFirewall/rulebase",
      "tags": [],
      "meta-info": {
        "lock": "locked by other session",
        "validation-state": "ok",
        "last-modify-time": {
          "posix": 1631557071554,
          "iso-8601": "2021-09-13T12:17-0600"
        },
        "last-modifier": "admin",
        "creation-time": {
          "posix": 1631557070914,
          "iso-8601": "2021-09-13T12:17-0600"
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
  - **shared** (boolean)
  - **applications-and-url-filtering** (boolean)
  - **content-awareness** (boolean)
  - **mobile-access** (boolean)
  - **firewall** (boolean)
  - **implicit-cleanup-action** (string)
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