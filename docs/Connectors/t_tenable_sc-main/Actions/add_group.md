# Add Group

**Description**: Adds a group

## Endpoint

- **URL:** `rest/group`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required
  - **name** (string) – Required
  - **description** (string)
  - **createDefaultObjects** (string)
  - **repositories** (array)
    - **id** (number)
  - **lces** (array)
    - **id** (number)
  - **definingAssets** (array)
    - **id** (number)
  - **assets** (array)
    - **id** (number)
  - **policies** (array)
    - **id** (number)
  - **queries** (array)
    - **id** (number)
  - **credentials** (array)
    - **id** (number)
  - **dashboardTabs** (array)
    - **id** (number)
  - **arcs** (array)
    - **id** (number)
  - **auditFiles** (array)
    - **id** (number)
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "OK",
    "json_body": {
      "type": "regular",
      "response": {
        "id": "5",
        "name": "Full Access Group test",
        "description": "",
        "createdTime": "1436551970",
        "modifiedTime": "1445892755",
        "lces": [
          {
            "id": "3",
            "name": "test LCE",
            "description": "Copied from Box for testing",
            "version": "4.6.0"
          },
          {
            "id": "4",
            "name": "LCE 1",
            "description": "Copied from Box for testing",
            "version": "4.4.1"
          },
          {
            "id": "5",
            "name": "LCE 2",
            "description": "Copied from Box for testing",
            "version": "4.4.0"
          }
        ],
        "repositories": [
          {
            "id": "38",
            "name": "ipv4",
            "description": "copied from QA",
            "lastVulnUpdate": "1445621650",
            "type": "Local",
            "dataFormat": "IPv4",
            "uuid": "49C61E1E-3D79-4345-AE79-CE3E5DF69B47"
          },
          {
            "id": "39",
            "name": "ipv6 rep",
            "description": "Copied from QA 2",
            "lastVulnUpdate": "1437805904",
            "type": "Local",
            "dataFormat": "IPv6",
            "uuid": "2253DAE5-880E-4796-B94C-1B880841BE64"
          },
          {
            "id": "44",
            "name": "Test w/pluginPrefs",
            "description": "",
            "lastVulnUpdate": "0",
            "type": "Local",
            "dataFormat": "mobile",
            "uuid": "79843218-F7CF-48C2-867D-54EA9A6B0225"
          },
          {
            "id": "57",
            "name": "test mobile airwatch rep",
            "description": "",
            "lastVulnUpdate": "0",
            "type": "Local",
            "dataFormat": "mobile",
            "uuid": "B0718AAC-2CDA-4A9C-B6F5-ED1F8EFFC755"
          }
        ],
        "definingAssets": [
          {
            "id": "0",
            "name": "All Defined Ranges",
            "description": "",
            "uuid": "0A18B330-B893-4080-96F2-220A45E0B203"
          }
        ],
        "userCount": 0,
        "users": [],
        "createDefaultObjects": "false",
        "assets": [],
        "policies": [],
        "queries": [],
        "credentials": [],
        "dashboardTabs": [],
        "auditFiles": [],
        "arcs": [
          {
            "id": "18",
            "name": "Database Settings",
            "description": "Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint cillum sint consectetur cupidatat"
          }
        ]
      },
      "error_code": 0,
      "error_msg": "",
      "warnings": [],
      "timestamp": 1445892755
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
    - **id** (string)
    - **name** (string)
    - **description** (string)
    - **createdTime** (string)
    - **modifiedTime** (string)
    - **lces** (array)
      - **id** (string)
      - **name** (string)
      - **description** (string)
      - **version** (string)
    - **repositories** (array)
      - **id** (string)
      - **name** (string)
      - **description** (string)
      - **lastVulnUpdate** (string)
      - **type** (string)
      - **dataFormat** (string)
      - **uuid** (string)
    - **definingAssets** (array)
      - **id** (string)
      - **name** (string)
      - **description** (string)
      - **uuid** (string)
    - **userCount** (number)
    - **users** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **createDefaultObjects** (string)
    - **assets** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **policies** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **queries** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **credentials** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **dashboardTabs** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **auditFiles** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **arcs** (array)
      - **id** (string)
      - **name** (string)
      - **description** (string)
  - **error_code** (number)
  - **error_msg** (string)
  - **warnings** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **timestamp** (number)