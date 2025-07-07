# Access Layer - Create

**Description**: Creates a new access layer in Check Point R80 using the specified name from the JSON body input.

## Endpoint

- **URL:** `/web_api/add-access-layer`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required: JSON Body
  - **name** (string) – Required: Object name. Must be unique in the domain
  - **add-default-rule** (boolean): Indicates whether to include a cleanup rule in the new layer
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
    "status_code": 200,
    "response_headers": {
      "Date": "Tue, 27 Dec 2022 13:47:48 GMT",
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
      "uid": "a40b877c-b723-4b0b-ac91-cab00bb40f06",
      "name": "hernan-test-rule-1",
      "type": "access-layer",
      "domain": {
        "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
        "name": "SMC User",
        "domain-type": "domain"
      },
      "shared": false,
      "applications-and-url-filtering": true,
      "content-awareness": true,
      "mobile-access": true,
      "detect-using-x-forward-for": false,
      "firewall": true,
      "implicit-cleanup-action": "drop",
      "comments": "this is a comment for a rule",
      "color": "purple",
      "icon": "ApplicationFirewall/rulebase",
      "tags": [
        {
          "uid": "08cdbabc-728b-4a7c-9c71-d92a559eb8fa",
          "name": "a",
          "type": "tag",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "7da31f05-7833-480a-b0c9-af58dc321e10",
          "name": "is",
          "type": "tag",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "e684296c-c756-4e51-864c-844cdc99764b",
          "name": "this",
          "type": "tag",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "b9f9390d-d761-431b-82d6-a5191c4a1316",
          "name": "test",
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
          "posix": 1672148868674,
          "iso-8601": "2022-12-27T06:47-0700"
        },
        "last-modifier": "admin",
        "creation-time": {
          "posix": 1672148865533,
          "iso-8601": "2022-12-27T06:47-0700"
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
  - **detect-using-x-forward-for** (boolean)
  - **firewall** (boolean)
  - **implicit-cleanup-action** (string)
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