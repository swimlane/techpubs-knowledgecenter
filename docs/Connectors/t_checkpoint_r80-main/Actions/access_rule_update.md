# Access Rule - Update

**Description**: Updates an existing access rule in Check Point R80 using the specified UID and layer, with details provided via JSON body.

## Endpoint

- **URL:** `/web_api/set-access-rule`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required: JSON Body
  - **uid** (string) – Required: Object unique identifier
  - **layer** (string) – Required: Layer that the rule belongs to identified by the name or UID
  - **new-name** (string): New name of the object
  - **new-position** (string): New position in the rulebase. Valid values are "top" or "bottom"
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
      "Date": "Thu, 29 Dec 2022 15:26:32 GMT",
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
      "uid": "78f98014-b77c-4bb9-8e37-e410f3d3a412",
      "name": "Cleanup rule",
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
      "layer": "f8d1cd7f-4340-4546-8da5-d985e8c565c3",
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
          "posix": 1632855705231,
          "iso-8601": "2021-09-28T13:01-0600"
        },
        "last-modifier": "admin",
        "creation-time": {
          "posix": 1632855705231,
          "iso-8601": "2021-09-28T13:01-0600"
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