# Application Site - Get

**Description**: Retrieve detailed information of a specific application site in Check Point R80 using its unique identifier (UID).

## Endpoint

- **URL:** `/web_api/show-application-site`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required: JSON Body
  - **uid** (string) – Required: Unique Object ID
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Thu, 29 Dec 2022 23:10:12 GMT",
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
      "uid": "00fa9e3c-36ef-0f65-e053-08241dc22da2",
      "name": "#hashtags",
      "type": "application-site",
      "domain": {
        "uid": "8bf4ac51-2df7-40e1-9bce-bedbedbedbed",
        "name": "APPI Data",
        "domain-type": "data domain"
      },
      "application-id": 10075536,
      "primary-category": "Twitter Clients",
      "description": "Hashtags are a community-driven convention for adding additional context and metadata to your tweets. They're like tags on Flickr, only added inline to your post. You create a hashtag simply by prefixing a word with a hash symbol: #hashtag.",
      "risk": "Very Low",
      "user-defined": false,
      "additional-categories": [
        "Share links",
        "Twitter Clients",
        "Very Low Risk"
      ],
      "groups": [],
      "comments": "",
      "color": "black",
      "icon": "@app/10075536_2",
      "tags": [],
      "meta-info": {
        "lock": "unlocked",
        "validation-state": "ok",
        "last-modify-time": {
          "posix": 1579506039190,
          "iso-8601": "2020-01-20T00:40-0700"
        },
        "last-modifier": "System",
        "creation-time": {
          "posix": 1579506039190,
          "iso-8601": "2020-01-20T00:40-0700"
        },
        "creator": "System"
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
  - **application-id** (number)
  - **primary-category** (string)
  - **description** (string)
  - **risk** (string)
  - **user-defined** (boolean)
  - **additional-categories** (array)
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