# Application Site - Create

**Description**: Creates a new application site in Check Point R80 using the provided name, primary category, and URL list.

## Endpoint

- **URL:** `/web_api/add-application-site`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required: JSON Body
  - **name** (string) – Required: Object name. Must be unique in the domain
  - **primary-category** (string) – Required: Each application is assigned to one primary category based on its most defining aspect
  - **url-list** (array) – Required: URLs that determine this particular application
  - **additional-categories** (array): Used to configure or edit the additional categories of a custom application / site used in the Application and URL Filtering or Threat Prevention
  - **description** (string): A description for the application
  - **urls-defined-as-regular-expression** (boolean): States whether the URL is defined as a Regular Expression or not
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
      "Date": "Thu, 29 Dec 2022 23:30:01 GMT",
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
      "uid": "3217f158-a635-4f9f-8c9b-7f460c4baa54",
      "name": "Hernan example application site 1",
      "type": "application-site",
      "domain": {
        "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
        "name": "SMC User",
        "domain-type": "domain"
      },
      "application-id": 0,
      "primary-category": "Computers / Internet",
      "description": "",
      "risk": "Unknown",
      "user-defined": true,
      "additional-categories": [
        "Botnets"
      ],
      "url-list": [
        "http://example.com"
      ],
      "urls-defined-as-regular-expression": true,
      "groups": [],
      "comments": "",
      "color": "red",
      "icon": "Objects/application",
      "tags": [
        {
          "uid": "028ac4da-b1d0-42f3-a4ad-48928f6e6385",
          "name": "are",
          "type": "tag",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "a83f97da-e553-435c-ab30-b4ca3dbd8395",
          "name": "tags",
          "type": "tag",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "6a253b13-e093-424d-b1d5-444b78dd26e1",
          "name": "these",
          "type": "tag",
          "domain": {
            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
            "name": "SMC User",
            "domain-type": "domain"
          }
        },
        {
          "uid": "a3711df3-606b-43b3-aec0-d93efc880597",
          "name": "the",
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
          "posix": 1672356601259,
          "iso-8601": "2022-12-29T16:30-0700"
        },
        "last-modifier": "admin",
        "creation-time": {
          "posix": 1672356601259,
          "iso-8601": "2022-12-29T16:30-0700"
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
  - **application-id** (number)
  - **primary-category** (string)
  - **description** (string)
  - **risk** (string)
  - **user-defined** (boolean)
  - **additional-categories** (array)
  - **url-list** (array)
  - **urls-defined-as-regular-expression** (boolean)
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