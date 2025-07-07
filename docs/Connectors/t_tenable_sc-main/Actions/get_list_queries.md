# Get List Queries

**Description**: Gets the list of Queries

## Endpoint

- **URL:** `/rest/query`
- **Method:** `GET`
## Inputs

- **parameters** (object)
  - **type** (string)
  - **fields** (string): Specify the fields want to include in the response
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Mon, 15 Apr 2024 06:40:02 GMT",
      "Server": "Apache",
      "X-Frame-Options": "DENY",
      "Content-Security-Policy": "default-src 'self'; script-src 'self' pendo-io-static.storage.googleapis.com app.pendo.io cdn.pendo.io pendo-static-6165929460760576.storage.googleapis.com data.pendo.io cdn.metarouter.io e.metarouter.io api.amplitude.com cdn.amplitude.com *.cloudfront.net; connect-src 'self' app.pendo.io data.pendo.io pendo-static-6165929460760576.storage.googleapis.com cdn.metarouter.io e.metarouter.io api.amplitude.com cdn.amplitude.com *.cloudfront.net; img-src 'self' data: cdn.pendo.io app.pendo.io pendo-static-6165929460760576.storage.googleapis.com data.pendo.io; style-src 'self' app.pendo.io cdn.pendo.io pendo-static-6165929460760576.storage.googleapis.com; frame-ancestors app.pendo.io; form-action 'self'; block-all-mixed-content; Upgrade-Insecure-Requests: 1; object-src 'none'",
      "X-Content-Type-Options": "nosniff",
      "X-XSS-Protection": "1; mode=block",
      "Expect-CT": "max-age=31536000",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
      "Vary": "x-apikey",
      "Set-Cookie": "TNS_SESSIONID=f65d532d29c8460000085c28c1f12c58; path=/; secure; HttpOnly; SameSite=Strict",
      "Expires": "Thu, 19 Nov 1981 08:52:00 GMT",
      "Cache-Control": "no-cache, no-store",
      "Pragma": "no-cache",
      "SecurityCenter": "5.19.1",
      "Content-Length": "3793",
      "Keep-Alive": "timeout=15, max=100",
      "Connection": "Keep-Alive",
      "Content-Type": "application/json"
    },
    "reason": "OK",
    "json_body": {
      "type": "regular",
      "response": {
        "usable": [
          {
            "id": "406",
            "name": "query test",
            "description": "",
            "tool": "sumid",
            "type": "vuln",
            "tags": "",
            "context": "",
            "browseColumns": "",
            "browseSortColumn": "",
            "browseSortDirection": "ASC",
            "createdTime": "1633112397",
            "modifiedTime": "1633112397",
            "status": "0",
            "groups": [],
            "filters": [],
            "canUse": "true",
            "canManage": "true",
            "creator": {
              "id": "1",
              "username": "admin-swimlane",
              "firstname": "Travis",
              "lastname": "Riley"
            },
            "owner": {
              "id": "1",
              "username": "admin-swimlane",
              "firstname": "Travis",
              "lastname": "Riley"
            },
            "ownerGroup": {
              "id": "0",
              "name": "Full Access",
              "description": "Full Access group"
            },
            "targetGroup": {
              "id": -1,
              "name": "",
              "description": ""
            }
          },
          {
            "id": "407",
            "name": "sada",
            "description": "asda",
            "tool": "sumid",
            "type": "vuln",
            "tags": "",
            "context": "",
            "browseColumns": "",
            "browseSortColumn": "",
            "browseSortDirection": "ASC",
            "createdTime": "1633114343",
            "modifiedTime": "1633114343",
            "status": "0",
            "groups": [],
            "filters": [],
            "canUse": "true",
            "canManage": "true",
            "creator": {
              "id": "1",
              "username": "admin-swimlane",
              "firstname": "Travis",
              "lastname": "Riley"
            },
            "owner": {
              "id": "1",
              "username": "admin-swimlane",
              "firstname": "Travis",
              "lastname": "Riley"
            },
            "ownerGroup": {
              "id": "0",
              "name": "Full Access",
              "description": "Full Access group"
            },
            "targetGroup": {
              "id": -1,
              "name": "",
              "description": ""
            }
          },
          {
            "id": "570",
            "name": "Vulnerability Detail list",
            "description": "",
            "tool": "vulndetails",
            "type": "vuln",
            "tags": "",
            "context": "",
            "browseColumns": "",
            "browseSortColumn": "",
            "browseSortDirection": "ASC",
            "createdTime": "1634010317",
            "modifiedTime": "1634010317",
            "status": "0",
            "groups": [],
            "filters": [],
            "canUse": "true",
            "canManage": "true",
            "creator": {
              "id": "1",
              "username": "admin-swimlane",
              "firstname": "Travis",
              "lastname": "Riley"
            },
            "owner": {
              "id": "1",
              "username": "admin-swimlane",
              "firstname": "Travis",
              "lastname": "Riley"
            },
            "ownerGroup": {
              "id": "0",
              "name": "Full Access",
              "description": "Full Access group"
            },
            "targetGroup": {
              "id": -1,
              "name": "",
              "description": ""
            }
          }
        ],
        "manageable": [
          {
            "id": "406",
            "name": "query test",
            "description": "",
            "tool": "sumid",
            "type": "vuln",
            "tags": "",
            "context": "",
            "browseColumns": "",
            "browseSortColumn": "",
            "browseSortDirection": "ASC",
            "createdTime": "1633112397",
            "modifiedTime": "1633112397",
            "status": "0",
            "groups": [],
            "filters": [],
            "canUse": "true",
            "canManage": "true",
            "creator": {
              "id": "1",
              "username": "admin-swimlane",
              "firstname": "Travis",
              "lastname": "Riley"
            },
            "owner": {
              "id": "1",
              "username": "admin-swimlane",
              "firstname": "Travis",
              "lastname": "Riley"
            },
            "ownerGroup": {
              "id": "0",
              "name": "Full Access",
              "description": "Full Access group"
            },
            "targetGroup": {
              "id": -1,
              "name": "",
              "description": ""
            }
          },
          {
            "id": "407",
            "name": "sada",
            "description": "asda",
            "tool": "sumid",
            "type": "vuln",
            "tags": "",
            "context": "",
            "browseColumns": "",
            "browseSortColumn": "",
            "browseSortDirection": "ASC",
            "createdTime": "1633114343",
            "modifiedTime": "1633114343",
            "status": "0",
            "groups": [],
            "filters": [],
            "canUse": "true",
            "canManage": "true",
            "creator": {
              "id": "1",
              "username": "admin-swimlane",
              "firstname": "Travis",
              "lastname": "Riley"
            },
            "owner": {
              "id": "1",
              "username": "admin-swimlane",
              "firstname": "Travis",
              "lastname": "Riley"
            },
            "ownerGroup": {
              "id": "0",
              "name": "Full Access",
              "description": "Full Access group"
            },
            "targetGroup": {
              "id": -1,
              "name": "",
              "description": ""
            }
          },
          {
            "id": "570",
            "name": "Vulnerability Detail list",
            "description": "",
            "tool": "vulndetails",
            "type": "vuln",
            "tags": "",
            "context": "",
            "browseColumns": "",
            "browseSortColumn": "",
            "browseSortDirection": "ASC",
            "createdTime": "1634010317",
            "modifiedTime": "1634010317",
            "status": "0",
            "groups": [],
            "filters": [],
            "canUse": "true",
            "canManage": "true",
            "creator": {
              "id": "1",
              "username": "admin-swimlane",
              "firstname": "Travis",
              "lastname": "Riley"
            },
            "owner": {
              "id": "1",
              "username": "admin-swimlane",
              "firstname": "Travis",
              "lastname": "Riley"
            },
            "ownerGroup": {
              "id": "0",
              "name": "Full Access",
              "description": "Full Access group"
            },
            "targetGroup": {
              "id": -1,
              "name": "",
              "description": ""
            }
          }
        ]
      },
      "error_code": 0,
      "error_msg": "",
      "warnings": [],
      "timestamp": 1713163202
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **type** (string)
  - **response** (object)
    - **usable** (array)
      - **id** (string)
      - **name** (string)
      - **description** (string)
      - **tool** (string)
      - **type** (string)
      - **tags** (string)
      - **context** (string)
      - **browseColumns** (string)
      - **browseSortColumn** (string)
      - **browseSortDirection** (string)
      - **createdTime** (string)
      - **modifiedTime** (string)
      - **status** (string)
      - **groups** (array)
        - **file_name** (string) – Required
        - **file** (string) – Required
      - **filters** (array)
        - **file_name** (string) – Required
        - **file** (string) – Required
      - **canUse** (string)
      - **canManage** (string)
      - **creator** (object)
        - **id** (string)
        - **username** (string)
        - **firstname** (string)
        - **lastname** (string)
      - **owner** (object)
        - **id** (string)
        - **username** (string)
        - **firstname** (string)
        - **lastname** (string)
      - **ownerGroup** (object)
        - **id** (string)
        - **name** (string)
        - **description** (string)
      - **targetGroup** (object)
        - **id** (number)
        - **name** (string)
        - **description** (string)
    - **manageable** (array)
      - **id** (string)
      - **name** (string)
      - **description** (string)
      - **tool** (string)
      - **type** (string)
      - **tags** (string)
      - **context** (string)
      - **browseColumns** (string)
      - **browseSortColumn** (string)
      - **browseSortDirection** (string)
      - **createdTime** (string)
      - **modifiedTime** (string)
      - **status** (string)
      - **groups** (array)
        - **file_name** (string) – Required
        - **file** (string) – Required
      - **filters** (array)
        - **file_name** (string) – Required
        - **file** (string) – Required
      - **canUse** (string)
      - **canManage** (string)
      - **creator** (object)
        - **id** (string)
        - **username** (string)
        - **firstname** (string)
        - **lastname** (string)
      - **owner** (object)
        - **id** (string)
        - **username** (string)
        - **firstname** (string)
        - **lastname** (string)
      - **ownerGroup** (object)
        - **id** (string)
        - **name** (string)
        - **description** (string)
      - **targetGroup** (object)
        - **id** (number)
        - **name** (string)
        - **description** (string)
  - **error_code** (number)
  - **error_msg** (string)
  - **warnings** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **timestamp** (number)
## Response Headers

| Header | Type |
|--------|------|
| Date | string |
| Server | string |
| X-Frame-Options | string |
| Content-Security-Policy | string |
| X-Content-Type-Options | string |
| X-XSS-Protection | string |
| Expect-CT | string |
| Strict-Transport-Security | string |
| Vary | string |
| Set-Cookie | string |
| Expires | string |
| Cache-Control | string |
| Pragma | string |
| SecurityCenter | string |
| Content-Length | string |
| Keep-Alive | string |
| Connection | string |
| Content-Type | string |