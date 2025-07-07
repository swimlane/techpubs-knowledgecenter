# Get Asset

**Description**: Gets the Asset associated with id or uuid

## Endpoint

- **URL:** `rest/asset/{{id}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **id** (string) – Required
- **parameters** (object)
  - **fields** (string)
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
        "id": "33",
        "name": "test",
        "type": "combination",
        "description": "",
        "tags": "",
        "context": "",
        "status": "0",
        "templateID": "-1",
        "createdTime": "1412171859",
        "modifiedTime": "1412171859",
        "typeFields": {
          "combinations": {
            "operator": "intersection",
            "operand1": {
              "id": "28",
              "name": "Test 1",
              "description": "",
              "uuid": "370CDC1B-6AA9-4897-844C-01C4CAF80220"
            },
            "operand2": {
              "id": "29",
              "name": "Test 2",
              "description": "",
              "uuid": "359C3A46-CE56-420C-8305-6498A72AA3F6"
            }
          }
        },
        "repositories": [
          {
            "ipCount": "1",
            "repository": {
              "id": "37",
              "name": "ag repo1",
              "description": "",
              "type": "Local",
              "uuid": "488A8EE7-69F3-4E49-A53F-0B1DB6CF8209"
            }
          },
          {
            "ipCount": "1",
            "repository": {
              "id": "38",
              "name": "jm ipv4",
              "description": "",
              "type": "Local",
              "uuid": "D7CFE6CF-8A69-4859-B9D0-9C6F05D1672D"
            }
          },
          {
            "ipCount": "0",
            "repository": {
              "id": "39",
              "name": "ipv6 rep",
              "description": "",
              "type": "Local",
              "uuid": "7C187636-3180-4E56-8E59-688AC2A7E831"
            }
          }
        ],
        "ipCount": 0,
        "groups": [],
        "assetDataFields": [],
        "viewableIPs": [
          {
            "repository": {
              "id": "37",
              "name": "ag repo1",
              "description": "",
              "type": "Local",
              "uuid": "488A8EE7-69F3-4E49-A53F-0B1DB6CF8209"
            },
            "ipList": "192.168.1.1\n",
            "ipCount": "1"
          },
          {
            "repository": {
              "id": "38",
              "name": "jm ipv4",
              "description": "",
              "type": "Local",
              "uuid": "D7CFE6CF-8A69-4859-B9D0-9C6F05D1672D"
            },
            "ipList": "192.168.1.1\n",
            "ipCount": "1"
          },
          {
            "repository": {
              "id": "39",
              "name": "ipv6 rep",
              "description": "",
              "type": "Local",
              "uuid": "7C187636-3180-4E56-8E59-688AC2A7E831"
            },
            "ipList": "",
            "ipCount": "0"
          }
        ],
        "creator": {
          "id": "1",
          "username": "head",
          "firstname": "Security Manager",
          "lastname": "",
          "uuid": "48F26F3B-6A79-4153-96DB-4C63D1BF3D46"
        },
        "owner": {
          "id": "1",
          "username": "head",
          "firstname": "Security Manager",
          "lastname": "",
          "uuid": "48F26F3B-6A79-4153-96DB-4C63D1BF3D46"
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
      "error_code": 0,
      "error_msg": "",
      "warnings": [],
      "timestamp": 1412273575
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
    - **type** (string)
    - **description** (string)
    - **tags** (string)
    - **context** (string)
    - **status** (string)
    - **templateID** (string)
    - **createdTime** (string)
    - **modifiedTime** (string)
    - **typeFields** (object)
      - **combinations** (object)
        - **operator** (string)
        - **operand1** (object)
          - **id** (string)
          - **name** (string)
          - **description** (string)
          - **uuid** (string)
        - **operand2** (object)
          - **id** (string)
          - **name** (string)
          - **description** (string)
          - **uuid** (string)
    - **repositories** (array)
      - **ipCount** (string)
      - **repository** (object)
        - **id** (string)
        - **name** (string)
        - **description** (string)
        - **type** (string)
        - **uuid** (string)
    - **ipCount** (number)
    - **groups** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **assetDataFields** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **viewableIPs** (array)
      - **repository** (object)
        - **id** (string)
        - **name** (string)
        - **description** (string)
        - **type** (string)
        - **uuid** (string)
      - **ipList** (string)
      - **ipCount** (string)
    - **creator** (object)
      - **id** (string)
      - **username** (string)
      - **firstname** (string)
      - **lastname** (string)
      - **uuid** (string)
    - **owner** (object)
      - **id** (string)
      - **username** (string)
      - **firstname** (string)
      - **lastname** (string)
      - **uuid** (string)
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