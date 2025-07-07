# Access Rule - Create

**Description**: Creates a new access rule in Check Point R80 at a specified layer and position, requiring 'layer' and 'position' as inputs.

## Endpoint

- **URL:** `/web_api/add-access-rule`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required: JSON Body
  - **layer** (string) – Required: Layer that the rule belongs to identified by the name or UID
  - **position** (string) – Required: Position in the rulebase. Valid values are "top" or "bottom"
  - **name** (string): Rule name
  - **action** (string): One of "Accept", "Drop", "Ask", "Inform", "Reject", "User Auth", "Client Auth", "Apply Layer"
  - **content-negate** (boolean): True if negate is set for data
  - **enabled** (boolean): Enable/Disable the rule
  - **source-negate** (boolean): True if negate is set for source
  - **comments** (string): Comments string
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Thu, 29 Dec 2022 15:08:41 GMT",
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
      "uid": "40ea885a-3d4a-4991-93c0-831865bd45e8",
      "name": "Hernan Rule 2",
      "type": "access-rule",
      "domain": {
        "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
        "name": "SMC User",
        "domain-type": "domain"
      },
      "track": {
        "type": {
          "uid": "29e53e3d-23bf-48fe-b6b1-d59bd88036f9",
          "name": "None",
          "type": "Track",
          "domain": {
            "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
            "name": "Check Point Data",
            "domain-type": "data domain"
          }
        },
        "per-session": false,
        "per-connection": false,
        "accounting": false,
        "enable-firewall-session": false,
        "alert": "none"
      },
      "layer": "ad28d864-3189-4d33-bce1-e33b571d9f9d",
      "source": [
        {
          "uid": "97aeb369-9aea-11d5-bd16-0090272ccb30",
          "name": "Any",
          "type": "CpmiAnyObject",
          "domain": {
            "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
            "name": "Check Point Data",
            "domain-type": "data domain"
          }
        }
      ],
      "source-negate": false,
      "destination": [
        {
          "uid": "97aeb369-9aea-11d5-bd16-0090272ccb30",
          "name": "Any",
          "type": "CpmiAnyObject",
          "domain": {
            "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
            "name": "Check Point Data",
            "domain-type": "data domain"
          }
        }
      ],
      "destination-negate": false,
      "service": [
        {
          "uid": "97aeb369-9aea-11d5-bd16-0090272ccb30",
          "name": "Any",
          "type": "CpmiAnyObject",
          "domain": {
            "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
            "name": "Check Point Data",
            "domain-type": "data domain"
          }
        }
      ],
      "service-negate": false,
      "vpn": [
        {
          "uid": "97aeb369-9aea-11d5-bd16-0090272ccb30",
          "name": "Any",
          "type": "CpmiAnyObject",
          "domain": {
            "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
            "name": "Check Point Data",
            "domain-type": "data domain"
          }
        }
      ],
      "action": {
        "uid": "6c488338-8eec-4103-ad21-cd461ac2c473",
        "name": "Drop",
        "type": "RulebaseAction",
        "domain": {
          "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
          "name": "Check Point Data",
          "domain-type": "data domain"
        }
      },
      "action-settings": {},
      "content": [
        {
          "uid": "97aeb369-9aea-11d5-bd16-0090272ccb30",
          "name": "Any",
          "type": "CpmiAnyObject",
          "domain": {
            "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
            "name": "Check Point Data",
            "domain-type": "data domain"
          }
        }
      ],
      "content-negate": false,
      "content-direction": "any",
      "time": [
        {
          "uid": "97aeb369-9aea-11d5-bd16-0090272ccb30",
          "name": "Any",
          "type": "CpmiAnyObject",
          "domain": {
            "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
            "name": "Check Point Data",
            "domain-type": "data domain"
          }
        }
      ],
      "custom-fields": {
        "field-1": "",
        "field-2": "",
        "field-3": ""
      },
      "meta-info": {
        "lock": "locked by current session",
        "validation-state": "ok",
        "last-modify-time": {
          "posix": 1672326519643,
          "iso-8601": "2022-12-29T08:08-0700"
        },
        "last-modifier": "admin",
        "creation-time": {
          "posix": 1672326519643,
          "iso-8601": "2022-12-29T08:08-0700"
        },
        "creator": "admin"
      },
      "comments": "",
      "enabled": true,
      "install-on": [
        {
          "uid": "6c488338-8eec-4103-ad21-cd461ac2c476",
          "name": "Policy Targets",
          "type": "Global",
          "domain": {
            "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
            "name": "Check Point Data",
            "domain-type": "data domain"
          }
        }
      ]
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
  - **track** (object)
    - **type** (object)
      - **uid** (string)
      - **name** (string)
      - **type** (string)
      - **domain** (object)
        - **uid** (string)
        - **name** (string)
        - **domain-type** (string)
    - **per-session** (boolean)
    - **per-connection** (boolean)
    - **accounting** (boolean)
    - **enable-firewall-session** (boolean)
    - **alert** (string)
  - **layer** (string)
  - **source** (array)
    - **uid** (string)
    - **name** (string)
    - **type** (string)
    - **domain** (object)
      - **uid** (string)
      - **name** (string)
      - **domain-type** (string)
  - **source-negate** (boolean)
  - **destination** (array)
    - **uid** (string)
    - **name** (string)
    - **type** (string)
    - **domain** (object)
      - **uid** (string)
      - **name** (string)
      - **domain-type** (string)
  - **destination-negate** (boolean)
  - **service** (array)
    - **uid** (string)
    - **name** (string)
    - **type** (string)
    - **domain** (object)
      - **uid** (string)
      - **name** (string)
      - **domain-type** (string)
  - **service-negate** (boolean)
  - **vpn** (array)
    - **uid** (string)
    - **name** (string)
    - **type** (string)
    - **domain** (object)
      - **uid** (string)
      - **name** (string)
      - **domain-type** (string)
  - **action** (object)
    - **uid** (string)
    - **name** (string)
    - **type** (string)
    - **domain** (object)
      - **uid** (string)
      - **name** (string)
      - **domain-type** (string)
  - **action-settings** (object)
  - **content** (array)
    - **uid** (string)
    - **name** (string)
    - **type** (string)
    - **domain** (object)
      - **uid** (string)
      - **name** (string)
      - **domain-type** (string)
  - **content-negate** (boolean)
  - **content-direction** (string)
  - **time** (array)
    - **uid** (string)
    - **name** (string)
    - **type** (string)
    - **domain** (object)
      - **uid** (string)
      - **name** (string)
      - **domain-type** (string)
  - **custom-fields** (object)
    - **field-1** (string)
    - **field-2** (string)
    - **field-3** (string)
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
  - **comments** (string)
  - **enabled** (boolean)
  - **install-on** (array)
    - **uid** (string)
    - **name** (string)
    - **type** (string)
    - **domain** (object)
      - **uid** (string)
      - **name** (string)
      - **domain-type** (string)
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